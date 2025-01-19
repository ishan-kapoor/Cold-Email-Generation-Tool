# Cold Email Generation Tool

A **Streamlit-based AI tool** for generating personalized cold emails by combining job description scraping, portfolio matching, and AI-driven email generation.

---

## Features

- **Web Scraping**: Extract job descriptions from websites automatically.
- **Portfolio Matching**: Find and use the most relevant projects and skills from your portfolio.
- **AI-Powered Email Generation**: Create professional emails tailored to job postings.

---

## Project Structure

```plaintext
.
├── main.py              # Main Streamlit app
├── portfolio.py         # Portfolio functions (load and query portfolio)
├── chains.py            # AI processing and chain logic
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables
├── resources/
│   └── my_portfolio.csv # Portfolio CSV file
└── README.md            # Documentation


## Installation and Setup

1. Clone the Repository
Clone the repository to your local machine:
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

2. Install Dependencies
Install all required Python libraries using pip:
    pip install -r requirements.txt

3. Configure the Environment
Add your Groq API key to a .env file:
    GROQ_API_KEY=your-groq-api-key

4. Add Your Portfolio
Prepare a CSV file named my_portfolio.csv in the resources directory. The file should contain the following columns:
    Techstack: Skills or technologies (e.g., Python, JavaScript).
    Links: URLs showcasing your work or projects.


## Features

- **Web Scraping**: Extract job descriptions from websites automatically.
- **Portfolio Matching**: Find and use the most relevant projects and skills from your portfolio.
- **AI-Powered Email Generation**: Create professional emails tailored to job postings.

---

## Usage

1. Run the Application: Start the Streamlit app by running: streamlit run main.py

2. Use the Tool:
    Enter the URL of a job posting.
    The tool scrapes and processes the job description.
    Matches relevant portfolio links.
    Generates a professional email tailored to the job.

##Example Workflow
Job Description Scraping: Extract job details from the provided URL.
Portfolio Matching: Select projects matching the job's requirements.
Cold Email Generation: Create a personalized email with your contact details, skills, and portfolio links.

Dependencies
This project uses the following libraries:

    langchain
    langchain-groq
    langchain_community
    chromadb
    beautifulsoup4
    pandas
    streamlit
    python-dotenv
    Install all dependencies with: pip install -r requirements.txt

Future Enhancements
    Support for additional vector databases.
    More flexible portfolio matching algorithms.
    Enhanced email templates for different job roles.



Contact
Developer: Ishan Kapoor
Email: ishankpor@gmail.com
Phone: +91-97112-54075
