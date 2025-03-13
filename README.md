![Hedge](https://github.com/user-attachments/assets/982b97cc-7c8c-45b6-b468-58417da8b5e0)



# Agentic-AI-Hedge-Fund



## Overview

This Streamlit application, `AI Hedge Fund Analysis`, leverages the power of Large Language Models (LLMs) through the Perplexity API to provide a comprehensive analysis of a given stock ticker. It simulates a hedge fund analysis process, covering various aspects from financial data and news sentiment to trading strategy development and risk assessment.

Test out the webapp at: https://pj-agentic-ai-hedge-fund.streamlit.app/

## **Application Features**
The AI Hedge Fund Analysis tool comprises the following specialized agents:

### **1. 📈 Financial Data Agent**
- Gathers key financial metrics, including:
  - Stock price, trading volume
  - Financial ratios (P/E, P/B, dividend yield)
  - Relevant market indicators and price trends

### **2. 📰 News Sentiment Agent**
- Analyzes recent news articles, social media trends, and expert opinions
- Summarizes prevailing sentiment
- Highlights key events that may impact stock performance

### **3. 🌐 Macro-Economic Environment Agent**
- Evaluates economic factors such as:
  - GDP growth, inflation, interest rates
  - Unemployment trends, central bank policies
- Assesses how these factors influence the stock and broader market

### **4. 📉 Technical Analysis Agent**
- Examines historical price trends and key technical indicators:
  - Moving averages, RSI, MACD, Bollinger Bands
- Identifies support/resistance levels and potential trade signals

### **5. 📊 Quantitative Strategy Agent**
- Develops a sophisticated trading strategy based on:
  - Financial data, sentiment analysis, macro trends, and technical indicators
- Outlines asset allocation, entry/exit points, and risk management

### **6. 📂 Portfolio Optimization Agent**
- Suggests optimal asset allocation and diversification
- Maximizes risk-adjusted returns by considering:
  - Diversification strategies
  - Asset correlation

### **7. ⚖️ Regulatory Compliance Agent**
- Assesses potential legal and regulatory risks
- Ensures the trading strategy adheres to financial regulations
- Highlights concerns such as market manipulation or compliance violations

### **8. ⚠️ Risk Assessment Agent**
- Identifies key risks such as:
  - Market volatility, liquidity concerns, unexpected market events
- Summarizes risk exposure in a structured format
- Determines if the strategy aligns with acceptable risk tolerance

### **9. 🔍 Summary Agent**
- Synthesizes all analyses into a concise report
- Summarizes key insights, potential risks, and recommended actions
- Provides a final decision-making overview for investors

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




