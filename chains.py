import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

model = ChatGroq(model="llama-3.3-70b-versatile")

def scrape_job(job_url):
    loader = WebBaseLoader(job_url)
    page_data = loader.load().pop().page_content
    return page_data

def extract_job_data(page_data):
    prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        The scraped text is from a career's page from a website.
        Your job is to extract the job postings and return them in JSON format containing the following keys: 'role', 'experience', 'skills', and 'description'.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):
        """
    )
    chain = prompt_extract | model
    res = chain.invoke(input={'page_data': page_data})
    json_parser = JsonOutputParser()
    return json_parser.parse(res.content)

def generate_email(job_description, link_list):
    prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}

        ### INSTRUCTION:
        You are Ishan Kapoor, an aspiring AI Engineer passionate about leveraging artificial intelligence to solve real-world problems...
        ### OUTPUT (NO PREAMBLE):
        """
    )
    chain = prompt_email | model
    res = chain.invoke({"job_description": str(job_description), "link_list": link_list})
    return res.content
