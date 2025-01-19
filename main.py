import streamlit as st
import pandas as pd
from portfolio import load_portfolio, query_portfolio
from chains import scrape_job, extract_job_data, generate_email

st.title("AI-Powered Job Application Tool")

# Load portfolio
portfolio_path = "./resources/my_portfolio.csv"
df_portfolio = load_portfolio(portfolio_path)

st.sidebar.header("Portfolio")
st.sidebar.write(df_portfolio)

# Input: Job URL
job_url = st.text_input("Enter Job URL", placeholder="https://jobs.example.com")

if st.button("Scrape and Process"):
    if job_url:
        with st.spinner("Processing..."):
            job_data = scrape_job(job_url)
            extracted_data = extract_job_data(job_data)
            st.write("Extracted Job Data:", extracted_data)

            # Query portfolio
            tech_stack = extracted_data.get('skills', '').split(', ')
            links = query_portfolio(df_portfolio, tech_stack)

            # Generate email
            email = generate_email(
                job_description=extracted_data,
                link_list=links
            )
            st.write("Generated Email:")
            st.code(email, language='plaintext')
    else:
        st.warning("Please enter a job URL.")
