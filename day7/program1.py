from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# load all the keys from .env file
load_dotenv()

# user prompt
prompt = "what is Agentic AI?"

# create LLM object
llm = ChatOpenAI(model="gpt-5", temperature=0.3)

# send the prompt and get the result
result = llm.invoke(prompt)
print(result.content)

