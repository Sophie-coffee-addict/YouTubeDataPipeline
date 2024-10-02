import os  # Import the os module to access environment variables and interact with the operating system
import openai  # Import the OpenAI library to interact with the GPT-3 API
import pandas as pd  # Import pandas for data manipulation and saving the data as CSV
from fpdf import FPDF # Import FPDF for generating the PDF report
from datetime import datetime as dt  # Import datetime to handle date formatting
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file
from googleapiclient.discovery import build  # Import the YouTube API client
from utils.comments import process_comments  # Import a custom function to process comments
from nltk.sentiment import SentimentIntensityAnalyzer  # NLTK for sentiment analysis
import matplotlib.pyplot as plt # Import matplotlib for data visualisation
import seaborn as sns # Import seaborn for data visualisation
import snownlp  # For Chinese sentiment analysis
import re  # Regular expressions for detecting languages

# Load environment variables from a .env file (where the API keys are stored)
load_dotenv()

# Get the YouTube API key from the environment variable
YOUTUBE_VIDEO_API_KEY = os.environ.get('YOUTUBE_VIDEO_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Set up the YouTube API service details
api_service_name = "youtube"
api_version = "v3"

# Build a YouTube API client using the API key
youtube = build(api_service_name, api_version, developerKey=YOUTUBE_VIDEO_API_KEY)

# Get the current date, formatted as 'YYYY-MM-DD' for the output CSV file
today = dt.today().strftime('%Y-%m-%d')

# Initialise the NLTK Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Initialise OpenAI API key
openai.api_key = OPENAI_API_KEY
print(f"Loaded OpenAI API Key: {OPENAI_API_KEY}")


# Function to retrieve comments for a specific video ID
def get_comments(video_id):
    comments_list = []  # Initialise an empty list to store the comments
    
    # First API request to get the top-level comment threads for the video
    request = youtube.commentThreads().list(
        part="id, snippet, replies",  # Get the comment ID, snippet (text), and any replies
        videoId=video_id,  # The ID of the video for which to fetch comments
        textFormat="plainText",  # Return the comments in plain text format
    )

    # Execute the request and store the response
    response = request.execute()

    # Process the first batch of comments and add to the comments list
    comments_list.extend(process_comments(response['items']))

    # Loop to handle pagination if there are more comments (handled by 'nextPageToken')
    while response.get('nextPageToken', None):
        # Request the next page of comments using the nextPageToken
        request = youtube.commentThreads().list(
            part='id,replies,snippet',
            videoId=video_id,
            pageToken=response['nextPageToken']  # Use the next page token to get the next batch of comments
        )
        # Execute the request and process the next batch of comments
        response = request.execute()
        comments_list.extend(process_comments(response['items']))

    # Print out how many comments were fetched for the given video
    print(f'Finished fetching comments for video {video_id}. {len(comments_list)} comments found.')

    # Return the list of processed comments
    return comments_list

# Function to detect if a comment is in Chinese
def is_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

# Function to clean mixed language comments (optional)
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove non-word characters (optional)
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Function to analyse sentiment for each comment
def analyse_sentiments(comments_list):
    sentiments = []
    
    # Perform sentiment analysis on each comment's text
    for comment in comments_list:
        # Debug: Print the entire comment to see its structure
        #print("Comment Data:", comment)

        # Check for 'text' field (instead of 'snippet')
        comment_text = comment.get('text')
        if comment_text:
            # Clean the comment text
            comment_text = clean_text(comment_text)
            #print(f"Analysing Comment: {comment_text}")  # Debug: Print the comment text being analysed
            
            if is_chinese(comment_text):  
                # If the text is in Chinese, use SnowNLP for sentiment analysis
                sentiment_score = snownlp.SnowNLP(comment_text).sentiments  # SnowNLP gives a score between 0-1
                sentiment_score = sentiment_score * 2 - 1  # Convert to VADER-like range (-1 to 1)
            else:  
                # If the text is in English, use NLTK's VADER for sentiment analysis
                sentiment_score = sia.polarity_scores(comment_text)['compound']  
            comment['sentiment'] = sentiment_score
            sentiments.append(sentiment_score)
        else:
            print("Warning: Missing 'text' in comment data.")  # Debug: Warn if text is missing
    
    #print("Sentiments:", sentiments)
    
    return comments_list, sentiments

# Function to visualise sentiment distribution
def visualise_sentiments(sentiments):
    if not sentiments:  # Check if the sentiment list is empty
        print("No sentiments to plot.")
        return
    
    plt.figure(figsize=(10, 6))
    sns.histplot(sentiments, kde=True)
    plt.title('Sentiment Score Distribution')
    plt.xlabel('Sentiment Score')
    plt.savefig('sentiment.png')
    #plt.show() -- this really blocks the script, so it's better to save the plot to a file
    print(f"Sentiment score distribution saved to 'sentiment.png'")

# Function to generate insights from the comments
def generate_insights_report(comments):
    prompt = (
        "Based on the following YouTube comments, generate an insights report. "
        "Focus on key trends, common themes, suggestions for future content, "
        "and areas where improvements can be made.\n\n"
        f"Comments: {comments}"
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        report = response.choices[0].message['content'].strip()
        print("OpenAI API call succeeded.")
        return report
    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return "Failed to generate insights."

# Function to generate insights from the sentiment score distribution
def generate_sentiment_insights(sentiments):
    prompt = (
        "Based on the following sentiment score distribution, analyse the data and provide insights. "
        "Focus on overall trends, any noticeable patterns, and suggestions for interpreting the data.\n\n"
        f"Sentiment Scores: {sentiments}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        insights = response.choices[0].message['content'].strip()
        print("OpenAI API call succeeded for sentiment insights.")
        return insights
    except Exception as e:
        print(f"Error during OpenAI API call for sentiment insights: {e}")
        return "Failed to generate sentiment insights."

# Function to save the report to a PDF
def save_report_to_pdf(comment_insights, sentiment_insights, filename="insights_report.pdf"):
    print("Inside save_report_to_pdf function...")  # Debug: Check if the function is called
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "YouTube Comments Insights Report", ln=True, align='C')
    
    # Section 1: Comments Insights
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "1. Insights from YouTube Comments", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, comment_insights)
    
    # Section 2: Sentiment Score Distribution (Image)
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "2. Sentiment Score Distribution", ln=True)
    pdf.image('sentiment.png', x=10, y=None, w=180)
    
    # Section 3: Sentiment Score Insights
    pdf.ln(85)  # Add space below the image
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "3. Insights from Sentiment Score Distribution", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, sentiment_insights)
    
    # Save PDF
    pdf.output(filename)
    print(f"PDF report generated and saved as {filename}")

# Save comments and their sentiment scores to a CSV file
def save_comments_to_csv(comments_list, video_id):
    df = pd.DataFrame(comments_list)  # Convert the list of comments to a DataFrame
    csv_filename = f'comments_{video_id}_{today}.csv'
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')  # Save as CSV, ensuring proper encoding for special characters
    print(f"Comments saved to {csv_filename}")

# Main function to orchestrate the fetching, analysis, and saving of comments
def main(video_id):
    print(f"Fetching comments for video: {video_id}...")
    comments_list = get_comments(video_id)  # Fetch comments
    
    if comments_list:
        print(f"Analysing {len(comments_list)} comments for sentiment...")
        analysed_comments, sentiments = analyse_sentiments(comments_list)  # Analyse sentiments

        # Debug: Print out the length of sentiments to verify it's not empty
        print(f"Number of sentiments: {len(sentiments)}")

        # Save comments along with sentiment scores to a CSV file
        save_comments_to_csv(analysed_comments, video_id)

        # Visualise sentiment distribution
        print("Visualising sentiments...")
        visualise_sentiments(sentiments)

        # Generate insights for the comments
        comments_text = " ".join([comment['text'] for comment in analysed_comments])
        comment_insights = generate_insights_report(comments_text)
        print(f"Comment Insights: {comment_insights}")  # debug: print the generated comment insights

        # Generate insights for sentiment score distribution
        sentiment_insights = generate_sentiment_insights(sentiments)
        print(f"Sentiment Insights: {sentiment_insights}")  # debug: print the generated sentiment insights

        # Save all insights to a PDF report
        save_report_to_pdf(comment_insights, sentiment_insights)
        print("Insights report generated and saved as 'insights_report.pdf'")
        
    else:
        print(f"No comments found for video {video_id}")

# Script entry point
if __name__ == "__main__":
    # Specify the YouTube video ID for which you want to fetch comments：
    video_id = 'tR0ed5XnfHQ' 
    main(video_id)
