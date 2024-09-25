# YouTubeDataPipeline
A Python-based ETL pipeline that uses the YouTube Data API to extract and save video comments to a CSV file for further analysis and insights

### Project Background
Maggie has been a YouTuber that I knew for many years and her videos have helped me so much to get to the almost native level of oral English. <br>Recently, I've been diving into Python, had a good, fun reading of Head First Python, and thought I'd play around with Python and real-life data. Turns out, it feels so much fun and great to generate insights from data for future improvement. 
<br>Next up, I'll email the insights generated to Maggie and hopefully it would be helpful to her : )
<br>This project is also inspired by my friend Meiqiao : )

### A Quick Peak of the Insights Report
<br><img width="730" alt="image" src="https://github.com/user-attachments/assets/a73fcb8f-2bb0-4462-bf6c-53f7dc505cf2">

<br>For a view of the full report, click here:
https://github.com/user-attachments/files/17023495/Actionable.Insights.for.Future.YouTube.Videos.pdf


### Key Learnings from This Project
1. **API Integration**: Gained hands-on experience extracting data from YouTube's API, handling pagination, and managing API responses.
2. **Sentiment Analysis**: Used NLTK's Vader lexicon to perform sentiment analysis on YouTube comments, identifying trends in audience sentiment.
3. **Data Visualisation**: Created visual representations of sentiment distribution using `matplotlib` and `seaborn`, making insights more accessible.
4. **Debugging and Problem-Solving**: Resolved key issues like missing data fields (`snippet` errors) and SSL certificate verification errors during API interactions.
5. **Automation**: Automated the process of saving YouTube comments and sentiment scores to CSV files for further analysis.


### Value Created
- **Audience Insights**: Generated insights into audience sentiment by analysing YouTube comments, providing creators with actionable feedback.
- **Sentiment Tracking**: Enabled continuous tracking of comment sentiment, helping creators understand how their audience reacts to specific content.
- **Efficient Feedback Pipeline**: Automated the extraction and analysis of user comments, allowing for faster feedback loops and potential content improvement.

  
### How to Use it
**Prerequisites**
- **Python 3.x**
- **YouTube Data API key**


### How to Get a YouTube Data API Key
1. Go to the **Google Cloud Console**: https://console.cloud.google.com/  
3. Click on **Select Project** > **NEW PROJECT**.
   <br><img width="394" alt="image" src="https://github.com/user-attachments/assets/8d565ef2-80fa-45ae-b811-87ee517a80b3">  
   <br><img width="763" alt="image" src="https://github.com/user-attachments/assets/2ccf81be-afee-4dda-b35e-cbac75b1e5c3">  
4. Name your project, and click **CREATE**.
   <br><img width="570" alt="image" src="https://github.com/user-attachments/assets/da291616-b2e1-490a-bb2f-a23881ab76bf">  
5. Once the project is created, navigate to the API & services section.
   <br><img width="477" alt="image" src="https://github.com/user-attachments/assets/fc328ccf-d647-4fd4-83a0-73f1d13dd855">  
6. Enable the YouTube Data API v3 by searching for it under Library.
   <br><img width="432" alt="image" src="https://github.com/user-attachments/assets/f696e465-fe8b-49b8-b952-405b1364eea8">
   <br><img width="810" alt="image" src="https://github.com/user-attachments/assets/fc219168-7a06-4297-a7f0-89f298773c5a">
7. Go to **Credentials** and click **CREATE CREDENTIALS** -> **API Key**.
   <br><img width="967" alt="image" src="https://github.com/user-attachments/assets/5919721a-38fd-4273-9120-97218adc6fa7">  
8. Copy your API key and store it securely (you will need it in the **.env** file).


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
API_KEY=your_youtube_data_api_key
```

3. Download NLTK Data
Make sure to download the required NLTK data (VADER lexicon) for sentiment analysis by running:
```bash
python3 -m nltk.downloader vader_lexicon
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
<br><img width="711" alt="image" src="https://github.com/user-attachments/assets/64db7ea1-86e0-4ca0-9dc7-62fa4b26084d">
- A PNG image (sentiment.png) of the sentiment score distribution.
<br><img width="862" alt="image" src="https://github.com/user-attachments/assets/32ea1524-3c9d-48aa-904b-d711984ce6da">
Then, I fed the comments and the sentiment score distribution to ChatGPT with the following prompts for insight analysis:
<br>"Based on the following YouTube comments, generate an insights report. Focus on key trends, common themes, suggestions for future content, and areas where improvements can be made."
<br>"Based on the following sentiment score distribution, analyse the data and provide insights. Focus on overall trends, any noticeable patterns, and suggestions for interpreting the data."


### Project Structure
<br><img width="231" alt="image" src="https://github.com/user-attachments/assets/9aa9c333-9805-44b9-9dae-8a18db08f771">









