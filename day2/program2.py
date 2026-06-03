# connect to LM studio LLM

from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
import os

# since ChatOpenAI requires api_key 
os.environ['OPENAI_API_KEY'] = "dummy-key"

# create an object of ChatOpenAI to connect to LM studio 
LM_STUDIO_BASE_URL = "http://localhost:1234/v1"
llm = ChatOpenAI(
    model="llama-3.2-3b-instruct", 
    base_url=LM_STUDIO_BASE_URL)

# create a prompt
prompt = "who is the fastest animal in jungle"

# send the prompt and get the result
# result = llm.invoke(prompt)
# print(result.content)

# send the prompt and stream the result
for chunk in llm.stream(prompt):
    print(chunk.content, end="")