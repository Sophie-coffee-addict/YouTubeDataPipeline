import os  # Import the os module to access environment variables and interact with the operating system
import pandas as pd  # Import pandas for data manipulation and saving the data as CSV
from datetime import datetime as dt  # Import datetime to handle date formatting
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file
from googleapiclient.discovery import build  # Import the YouTube API client
from utils.comments import process_comments  # Import a custom function to process comments
from nltk.sentiment import SentimentIntensityAnalyzer  # NLTK for sentiment analysis
import matplotlib.pyplot as plt # Import matplotlib for data visualization
import seaborn as sns # Import seaborn for data visualization

# Load environment variables from a .env file (where the API key is stored)
load_dotenv()

# Get the YouTube API key from the environment variable
API_KEY = os.environ.get('API_KEY')

# Set up the YouTube API service details
api_service_name = "youtube"
api_version = "v3"

# Build a YouTube API client using the API key
youtube = build(api_service_name, api_version, developerKey=API_KEY)

# Get the current date, formatted as 'YYYY-MM-DD' for the output CSV file
today = dt.today().strftime('%Y-%m-%d')

# Initialize the NLTK Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Function to retrieve comments for a specific video ID
def get_comments(video_id):
    comments_list = []  # Initialize an empty list to store the comments
    
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

# Function to analyze sentiment for each comment
def analyze_sentiments(comments_list):
    sentiments = []
    
    # Perform sentiment analysis on each comment's text
    for comment in comments_list:
        # Debug: Print the entire comment to see its structure
        print("Comment Data:", comment)

        # Check for 'text' field (instead of 'snippet')
        comment_text = comment.get('text')
        if comment_text:
            print(f"Analyzing Comment: {comment_text}")  # Debug: Print the comment text being analyzed
            sentiment_score = sia.polarity_scores(comment_text)['compound']  # Compound score gives overall sentiment
            comment['sentiment'] = sentiment_score  # Add sentiment score to the comment data
            sentiments.append(sentiment_score)  # Add sentiment score to the list for visualization
        else:
            print("Warning: Missing 'text' in comment data.")  # Debug: Warn if text is missing
    
    print("Sentiments:", sentiments)
    
    return comments_list, sentiments

# Function to visualize sentiment distribution
def visualize_sentiments(sentiments):
    if not sentiments:  # Check if the sentiment list is empty
        print("No sentiments to plot.")
        return
    
    plt.figure(figsize=(10, 6))
    sns.histplot(sentiments, kde=True)
    plt.title('Sentiment Score Distribution')
    plt.xlabel('Sentiment Score')
    plt.savefig('sentiment.png')
    plt.show()
    print(f"Sentiment score distribution saved to 'sentiment.png'")

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
        print(f"Analyzing {len(comments_list)} comments for sentiment...")
        analyzed_comments, sentiments = analyze_sentiments(comments_list)  # Analyze sentiments

        # Debug: Print out the length of sentiments to verify it's not empty
        print(f"Number of sentiments: {len(sentiments)}")

        # Save comments along with sentiment scores to a CSV file
        save_comments_to_csv(analyzed_comments, video_id)

        # Visualize sentiment distribution
        print("Visualizing sentiments...")
        visualize_sentiments(sentiments)
    else:
        print(f"No comments found for video {video_id}")

# Script entry point
if __name__ == "__main__":
    video_id = 'tR0ed5XnfHQ' 
    main(video_id)
