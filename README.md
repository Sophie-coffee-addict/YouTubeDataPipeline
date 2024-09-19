# YouTubeDataPipeline
A Python-based ETL pipeline that uses the YouTube Data API to extract and save video comments to a CSV file for further analysis and insights

### Project Background
Maggie has been a YouTuber that I knew for many years and her videos have helped me so much to get to the almost native level of oral English. <br>Recently, I've been diving into Python, had a good, fun reading of Head First Python, and thought I'd play around with Python and real-life data. Turns out, it feels so much fun and great to generate insights from data for future improvement. 
<br>Next up, I'll email the insights generated to Maggie and hopefully it would be helpful to her : )
<br>This project is also inspired by my friend Meiqiao : )
<br>For a view of the full report, click here:
https://github.com/user-attachments/files/17023495/Actionable.Insights.for.Future.YouTube.Videos.pdf


### Key Learnings from This Project
1. **API Integration**: Gained hands-on experience extracting data from YouTube's API, handling pagination, and managing API responses.
2. **Sentiment Analysis**: Used NLTK's Vader lexicon to perform sentiment analysis on YouTube comments, identifying trends in audience sentiment.
3. **Data Visualization**: Created visual representations of sentiment distribution using `matplotlib` and `seaborn`, making insights more accessible.
4. **Debugging and Problem-Solving**: Resolved key issues like missing data fields (`snippet` errors) and SSL certificate verification errors during API interactions.
5. **Automation**: Automated the process of saving YouTube comments and sentiment scores to CSV files for further analysis.


### Value Created
- **Audience Insights**: Generated insights into audience sentiment by analyzing YouTube comments, providing creators with actionable feedback.
- **Sentiment Tracking**: Enabled continuous tracking of comment sentiment, helping creators understand how their audience reacts to specific content.
- **Efficient Feedback Pipeline**: Automated the extraction and analysis of user comments, allowing for faster feedback loops and potential content improvement.

  
### How to Use it
**Prerequisites**
- **Python 3.x**
- **YouTube Data API key**


### How to Get a YouTube Data API Key
1. Go to the **Google Cloud Console**: https://console.cloud.google.com/  
3. Click on **Select Project** > **NEW PROJECT**
   <img width="394" alt="image" src="https://github.com/user-attachments/assets/8d565ef2-80fa-45ae-b811-87ee517a80b3">  
   <img width="763" alt="image" src="https://github.com/user-attachments/assets/2ccf81be-afee-4dda-b35e-cbac75b1e5c3">  
4. Name your project, and click **CREATE**.
   <img width="570" alt="image" src="https://github.com/user-attachments/assets/da291616-b2e1-490a-bb2f-a23881ab76bf">  
5. Once the project is created, navigate to the API & Services section.
   <img width="477" alt="image" src="https://github.com/user-attachments/assets/fc328ccf-d647-4fd4-83a0-73f1d13dd855">  
6. Enable the YouTube Data API v3 by searching for it under Library.
   <img width="432" alt="image" src="https://github.com/user-attachments/assets/f696e465-fe8b-49b8-b952-405b1364eea8">
   <img width="810" alt="image" src="https://github.com/user-attachments/assets/fc219168-7a06-4297-a7f0-89f298773c5a">
7. Go to **Credentials** and click **CREATE CREDENTIALS** -> **API Key**.
    <img width="967" alt="image" src="https://github.com/user-attachments/assets/5919721a-38fd-4273-9120-97218adc6fa7">  
8. Copy your API key and store it securely (you will need it in the **.env** file).


