# import the ChatOpenAI class
from langchain_openai import ChatOpenAI

# import os to load the environment variables
import os

# import dotenv to load environment variables
from dotenv import load_dotenv

# this function will load all the key-value pairs from .env file as well
load_dotenv()

# set the API Key for OpenAI GPT
# os.environ['OPENAI_API_KEY'] = ''
# print(os.environ)

# create an object of ChatOpenAI to communicate with GPT
model = ChatOpenAI(model="gpt-5", temperature=0.7, max_completion_tokens=100)

# create a prompt (input for LLM)
prompt = "what is special on Sept 2"

# send an input to the GPT using a prompt
# result = model.invoke(prompt)

# wait till the entire result is available
# print(result)
# print(result.content)

# do not wait for the entire result, instead print the result as it gets generated
for chunk in model.stream(prompt):
    print(chunk.content)

