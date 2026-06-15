import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


model = ChatOpenAI(
    model="gpt-5.4-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)