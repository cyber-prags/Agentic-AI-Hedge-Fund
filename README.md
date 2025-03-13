![Hedge](https://github.com/user-attachments/assets/982b97cc-7c8c-45b6-b468-58417da8b5e0)



# Agentic-AI-Hedge-Fund



## Overview

This Streamlit application, `AI Hedge Fund Analysis`, leverages the power of Large Language Models (LLMs) through the Perplexity API to provide a comprehensive analysis of a given stock ticker. It simulates a hedge fund analysis process, covering various aspects from financial data and news sentiment to trading strategy development and risk assessment.

Test out the webapp at: https://pj-agentic-ai-hedge-fund.streamlit.app/

The application is designed to:

1.  **Gather and analyze financial data:** Retrieve and present key financial metrics for a given stock.
2.  **Perform news sentiment analysis:** Analyze recent news and social media to gauge market sentiment.
3.  **Assess the macro-economic environment:** Evaluate how broader economic factors might impact the stock.
4.  **Conduct technical analysis:** Analyze historical price trends and technical indicators.
5.  **Develop a quantitative trading strategy:** Formulate a trading plan based on the analysis.
6.  **Optimize portfolio allocation:** Suggest optimal asset weights and diversification.
7.  **Evaluate regulatory compliance:** Identify potential regulatory risks.
8.  **Assess overall risk:** Summarize potential risks and evaluate risk tolerance.
9.  **Provide a comprehensive summary:** Offer a concise overview of the entire analysis.

## Project Structure

-   `app.py`: The main Streamlit application file containing the entire logic.
-   `.env`: A file to store the Perplexity API key (should not be committed to version control).
-   `Hedge_fund.jpg` (optional): An image for the Streamlit app.

## Dependencies

-   `streamlit`: For building the web application.
-   `os`: For interacting with the operating system.
-   `PIL (Pillow)`: For image processing (optional).
-   `dotenv`: For loading environment variables.
-   `langchain`: For working with Large Language Models.
-   `langchain_community`: for using the Perplexity Chat model.

Install the dependencies using:

```bash
pip install streamlit pillow python-dotenv langchain langchain_community
```

## Setup and Configuration
*Clone the Repository:*
```
Bash


git clone <repository_url>
cd <repository_directory>
```

Create a ```.env``` file:
- Obtain a Perplexity API key from the Perplexity AI platform.
- Create a .env file in the project root directory.
- Add the API key to the .env file:
```PPLX_API_KEY=<your_perplexity_api_key>
```

*Run the Streamlit Application:*
```
Bash

streamlit run app.py
```

This will open the application in your web browser.




