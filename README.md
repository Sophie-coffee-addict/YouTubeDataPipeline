# YouTubeDataPipeline
A Python-based ETL pipeline that uses the YouTube Data API to extract and save video comments to a CSV file for further analysis and insights

### Project Background
Maggie has been a YouTuber that I knew for many years and her videos have helped me so much. <br>Recently, I've been diving into Python, had a good, fun reading of Head First Python, and thought I'd play around with Python and real-life data. Turns out, it feels so much fun and great to generate insights from data for future content improvement. 
<br>I have emailed the insights generated to Maggie and hopefully it would be helpful to her : )
<br>This project is also inspired by my friend Meiqiao : )

### A Quick Peek of the Insights Report <br>
<br><img width="772" alt="image" src="https://github.com/user-attachments/assets/5cf612d8-2f1f-4707-9e8b-76664fd1e522">

<br>For a view of the full report, click here: <br>
https://github.com/user-attachments/files/17220116/insights_report.pdf


### Key Learnings from This Project
1. **API Integration**: Gained hands-on experience extracting data from YouTube's API and insights analysis with OpenAI API.
2. **Sentiment Analysis**: Used NLTK's Vader lexicon (for English) and SnowNLP (for Chinese) to perform sentiment analysis on YouTube comments, identifying trends in audience sentiment.
3. **Data Visualisation**: Created visual representations of sentiment distribution using `matplotlib` and `seaborn`, making insights more accessible.
4. **Debugging and Problem-Solving**: Resolved key issues like missing data fields (`snippet` errors); SSL certificate verification errors during API interactions; plt.show() blocking the script running...
5. **Automation**: Automated the entire process: saving YouTube comments and sentiment scores to a CSV file, generating insights using ChatGPT, and saving the insights report into a PDF file.


### Value Created
- **Audience Insights**: Generated insights into audience sentiment by analysing YouTube comments, providing creators with actionable feedback.
- **Sentiment Tracking**: Enabled continuous tracking of comment sentiment, helping creators understand how their audience reacts to specific content.
- **Efficient Feedback Pipeline**: Automated the extraction and analysis of user comments, allowing for faster feedback loops and potential content improvement.

  
### How to Use it
**Prerequisites**
- **Python 3.x**
- **YouTube Data API key**
- **OpenAI API key**


### How to Get a YouTube Data API Key
1. Go to the **Google Cloud Console**: https://console.cloud.google.com/  
3. Click on **Select a project** > **NEW PROJECT**.
   <br><img width="394" alt="image" src="https://github.com/user-attachments/assets/8d565ef2-80fa-45ae-b811-87ee517a80b3">  <br>
   <br><img width="763" alt="image" src="https://github.com/user-attachments/assets/2ccf81be-afee-4dda-b35e-cbac75b1e5c3">  <br>  
4. Name your project, and click **CREATE**.
   <br><img width="570" alt="image" src="https://github.com/user-attachments/assets/da291616-b2e1-490a-bb2f-a23881ab76bf">  <br>
5. Once the project is created, navigate to the API & services section.
   <br><img width="477" alt="image" src="https://github.com/user-attachments/assets/fc328ccf-d647-4fd4-83a0-73f1d13dd855">  <br>
6. Enable the YouTube Data API v3 by searching for it under Library.
   <br><img width="432" alt="image" src="https://github.com/user-attachments/assets/f696e465-fe8b-49b8-b952-405b1364eea8">  <br>
   <br><img width="810" alt="image" src="https://github.com/user-attachments/assets/fc219168-7a06-4297-a7f0-89f298773c5a">  <br>
7. Go to **Credentials** and click **CREATE CREDENTIALS** -> **API Key**.
   <br><img width="967" alt="image" src="https://github.com/user-attachments/assets/5919721a-38fd-4273-9120-97218adc6fa7">  <br>
8. Copy your API key and store it securely (you will need it in the **.env** file).

### How to Get an OpenAI API Key
1. Visit openai.com
2. Click **Products** > **API login**.
   <br><img width="565" alt="image" src="https://github.com/user-attachments/assets/c22e68da-b72e-4dd1-9e9a-229f2615954e">  <br>
3. On the left pane, click **API keys** > **Create new secret key**.
   <br><img width="1253" alt="image" src="https://github.com/user-attachments/assets/edc6fc21-6780-4f6d-9f79-3cd7625200c1">  <br>
   
Note: If you don't want the comments and sentiment analysis process to be automated, you can manually feed them into AI with your customised prompts.   <br>

### Dependencies
Install the following dependencies using pip:<br>
```bash
pip3 install pandas nltk matplotlib seaborn google-api-python-client python-dotenv
```

### Setup
1. **Clone the repository**
```bash
git clone https://github.com/Sophie-coffee-addict/youtube_data_pipeline.git
cd youtube_data_pipeline
```

2. **Set up the environment variables**
Create a .env file in the root directory of your project and add your YouTube Data API key :<br>
```bash
YOUTUBE_API_KEY=your_youtube_data_api_key
OPENAI_API_KEY=your_openai_api_key
```

3. Download NLTK and SnowNLP (if there are Chinese texts to be analysed):
Make sure to download the required NLTK data (VADER lexicon) for sentiment analysis by running:
```bash
python3 -m nltk.downloader vader_lexicon
pip3 install snownlp
```

4. Install the FPDF library to save insights into a PDF file:
```bash
pip3 install fpdf
```

### How to Run the Pipeline
1. **Run the Pipeline**
You can run the pipeline using the following command:
```bash
python3 yt_comments.py
```

The video ID can be set within the main() function of the yt_comments.py file:
```bash
if __name__ == "__main__":
    video_id = 'your_video_ID'  # the bit after "=" in the video link
    main(video_id)
```
<br><img width="286" alt="image" src="https://github.com/user-attachments/assets/9a9948b3-9467-437e-9ea2-c5ca9c426a3d">

2. **What Happens Next**
- Extract Comments: The script will extract all comments from the video.
- Sentiment Analysis: It performs sentiment analysis on the comments.
- A CSV file (comments_<video_id>_<date>.csv) containing the comments and sentiment scores.
<br><img width="561" alt="image" src="https://github.com/user-attachments/assets/0c696cda-15d5-40c2-9f16-a3f5dcc380f2">
- A PNG image (sentiment.png) of the sentiment score distribution.
<br><img width="872" alt="image" src="https://github.com/user-attachments/assets/67063dcb-5c3a-4865-ba1f-dc347b99d214">
- The comments and sentiment score distribution are fed to ChatGPT with the preset prompts to generate an insights report.
- The report is saved into a PDF file.

3.**What You Get**
Generated Reports: It will automatically generate:
- A CSV file (comments_<video_id>_<date>.csv) containing the comments and sentiment scores.
- A PNG image (sentiment.png) of the sentiment score distribution.
- A PDF file (insights_report.pdf) with detailed insights and visualizations.

### Project Structure
<br><img width="231" alt="image" src="https://github.com/user-attachments/assets/9aa9c333-9805-44b9-9dae-8a18db08f771">









