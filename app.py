import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain_community.chat_models.perplexity import ChatPerplexity
from langchain.chains import SequentialChain

# -------------------- Streamlit App Configuration --------------------
st.set_page_config(page_title="AI Hedge Fund Analysis", layout="wide")

# local_image = Image.open("Hedge_fund.jpg")  

# fixed_height = 700 # desired height in pixels
# fixed_width = 10000 # desired width in pixels
# width, height = local_image.size
# aspect_ratio = width / height
# new_width = fixed_width
# resized_image = local_image.resize((new_width, fixed_height))

# st.image(resized_image, caption="")

st.title("AI Hedge Fund Analysis")
st.write("Enter a ticker symbol below to run the analysis:")

ticker_input = st.text_input("Ticker Symbol (e.g. MSFT)", value="MSFT")
run_button = st.button("Run Analysis")

# -------------------- Load Environment Variables --------------------
load_dotenv()  # Load variables from .env file
PPLX_API_KEY = os.getenv("PPLX_API_KEY")

# -------------------- AI Hedge Fund Analysis Setup --------------------
llm_model = ChatPerplexity(
    model="sonar-reasoning",
    temperature=0.5,
    pplx_api_key=PPLX_API_KEY
)

# 1. Financial Data Analysis
financial_data_chain = LLMChain(
    llm=llm_model,
    prompt=PromptTemplate(
        input_variables=["ticker"],
        template=(
            "📈 For {ticker}, provide detailed and up-to-date financial data including current stock price, "
            "volume, key financial ratios (e.g., P/E, P/B, dividend yield), recent price trends, and relevant market indicators."
        )
    ),
    output_key="financial_data"
)

# 2. News Sentiment Analysis
news_sentiment_chain = LLMChain(
    llm=llm_model,
    prompt=PromptTemplate(
        input_variables=["ticker"],
        template=(
            "📰 For {ticker}, analyze recent news articles, social media posts, and expert commentary. "
            "Summarize the prevailing sentiment, highlight any key events, and note emerging trends that may impact the stock."
        )
    ),
    output_key="news_sentiment"
)

# 3. Macro-Economic Environment Analysis
macro_environment_chain = LLMChain(
    llm=llm_model,
    prompt=PromptTemplate(
        input_variables=["ticker"],
        template=(
            "🌐 For {ticker}, analyze the current macro-economic environment. Include key indicators such as GDP growth, "
            "inflation rates, interest rates, unemployment trends, and central bank policies. "
            "Summarize how these factors could impact the overall market and the asset."
        )
    ),
    output_key="macro_environment"
)

# 4. Technical Analysis
technical_analysis_chain = LLMChain(
    llm=llm_model,
    prompt=PromptTemplate(
        input_variables=["ticker"],
        template=(
            "📉 For {ticker}, analyze historical price trends, moving averages, and key technical indicators (e.g., RSI, MACD, Bollinger Bands). "
            "Identify support/resistance levels and potential technical entry/exit signals."
        )
    ),
    output_key="technical_analysis"
)

# 5. Quantitative Strategy Development
quantitative_strategy_chain = LLMChain(
    llm=llm_model,
    prompt=PromptTemplate(
        input_variables=["financial_data", "news_sentiment", "macro_environment", "technical_analysis"],
        template=(
            "📊 Using the following data:\n"
            "Financial Data:\n{financial_data}\n"
            "News Sentiment:\n{news_sentiment}\n"
            "Macro-Economic Analysis:\n{macro_environment}\n"
            "Technical Analysis:\n{technical_analysis}\n\n"
            "Develop a sophisticated trading strategy. Outline a clear asset allocation, specify entry and exit points, "
            "detail risk management measures, and provide estimated expected returns. Incorporate algorithmic signals if applicable."
        )
    ),
    output_key="trading_strategy"
)

# 6. Portfolio Optimization
portfolio_optimization_chain = LLMChain(
    llm=llm_model,
    prompt=PromptTemplate(
        input_variables=["trading_strategy"],
        template=(
            "📂 Based on the trading strategy below:\n{trading_strategy}\n\n"
            "Suggest an optimal portfolio allocation. Consider diversification, risk minimization, and asset correlation. "
            "Provide recommended asset weights and allocation adjustments to maximize risk-adjusted returns."
        )
    ),
    output_key="portfolio_optimization"
)

# 7. Regulatory Compliance Analysis
regulatory_compliance_chain = LLMChain(
    llm=llm_model,
    prompt=PromptTemplate(
        input_variables=["trading_strategy", "portfolio_optimization"],
        template=(
            "⚖️ Evaluate the following trading strategy:\n{trading_strategy}\n\n"
            "and the portfolio optimization recommendations:\n{portfolio_optimization}\n\n"
            "Identify potential regulatory and compliance risks, including any legal or market manipulation concerns. "
            "Provide recommendations to ensure the strategy adheres to financial regulations and minimizes regulatory risk."
        )
    ),
    output_key="regulatory_compliance"
)

# 8. Risk Assessment
risk_assessment_chain = LLMChain(
    llm=llm_model,
    prompt=PromptTemplate(
        input_variables=["trading_strategy", "portfolio_optimization"],
        template=(
            "⚠️ Evaluate the following trading strategy and portfolio optimization:\n"
            "Trading Strategy:\n{trading_strategy}\n"
            "Portfolio Optimization:\n{portfolio_optimization}\n\n"
            "Identify potential risks such as market volatility, liquidity issues, or unexpected market events. "
            "Summarize your risk assessment in 4 concise bullet points, and conclude with a final bullet point stating whether the overall strategy meets acceptable risk tolerance."
        )
    ),
    output_key="risk_assessment"
)

# 9. Summary Agent
summary_chain = LLMChain(
    llm=llm_model,
    prompt=PromptTemplate(
        input_variables=[
            "financial_data",
            "news_sentiment",
            "macro_environment",
            "technical_analysis",
            "trading_strategy",
            "portfolio_optimization",
            "regulatory_compliance",
            "risk_assessment"
        ],
        template=(
            "🔍 Summarize the overall analysis results below:\n"
            "Financial Data: {financial_data}\n"
            "News Sentiment: {news_sentiment}\n"
            "Macro-Economic Environment: {macro_environment}\n"
            "Technical Analysis: {technical_analysis}\n"
            "Trading Strategy: {trading_strategy}\n"
            "Portfolio Optimization: {portfolio_optimization}\n"
            "Regulatory Compliance: {regulatory_compliance}\n"
            "Risk Assessment: {risk_assessment}\n\n"
            "Provide a concise summary of the key insights, potential risks, and recommended actions."
        )
    ),
    output_key="analysis_summary"
)

# Sequential orchestration of agents (steps 1-8)
ai_hedge_fund_chain = SequentialChain(
    chains=[
        financial_data_chain,
        news_sentiment_chain,
        macro_environment_chain,
        technical_analysis_chain,
        quantitative_strategy_chain,
        portfolio_optimization_chain,
        regulatory_compliance_chain,
        risk_assessment_chain
    ],
    input_variables=["ticker"],
    output_variables=[
        "financial_data",
        "news_sentiment",
        "macro_environment",
        "technical_analysis",
        "trading_strategy",
        "portfolio_optimization",
        "regulatory_compliance",
        "risk_assessment"
    ],
    verbose=True
)

# -------------------- Run the Analysis and Display Results --------------------
if run_button and ticker_input:
    with st.spinner("Running analysis, please wait..."):
        try:
            results = ai_hedge_fund_chain({"ticker": ticker_input})
            # Run the summary agent
            summary_results = summary_chain({
                "financial_data": results["financial_data"],
                "news_sentiment": results["news_sentiment"],
                "macro_environment": results["macro_environment"],
                "technical_analysis": results["technical_analysis"],
                "trading_strategy": results["trading_strategy"],
                "portfolio_optimization": results["portfolio_optimization"],
                "regulatory_compliance": results["regulatory_compliance"],
                "risk_assessment": results["risk_assessment"]
            })
        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")
        else:
            st.success("Analysis complete!")
            
            # Display each section in an expander for a clean layout
            with st.expander("📈 Financial Data"):
                st.write(results["financial_data"])
            with st.expander("📰 News Sentiment"):
                st.write(results["news_sentiment"])
            with st.expander("🌐 Macro-Economic Environment"):
                st.write(results["macro_environment"])
            with st.expander("📉 Technical Analysis"):
                st.write(results["technical_analysis"])
            with st.expander("📊 Trading Strategy"):
                st.write(results["trading_strategy"])
            with st.expander("📂 Portfolio Optimization"):
                st.write(results["portfolio_optimization"])
            with st.expander("⚖️ Regulatory Compliance"):
                st.write(results["regulatory_compliance"])
            with st.expander("⚠️ Risk Assessment"):
                st.write(results["risk_assessment"])
            
            # Display the overall summary with a nice graphic separator
            st.markdown("---")
            st.markdown("### 🔍 Overall Analysis Summary")
            st.write(summary_results["analysis_summary"])
