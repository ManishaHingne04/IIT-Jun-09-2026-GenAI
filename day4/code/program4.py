from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# load all the keys from .env file
load_dotenv()

# create llm
llm = ChatOpenAI(model="gpt-5")

# create the prompt
template = """
You are a helpful assistant. Answer user's question:
{question}
"""

while True:
    message = input("user> ")
    prompt_template = ChatPromptTemplate.from_template(template=template)
    prompt = prompt_template.invoke({"question": message})

    # send the prompt and get the result
    result = llm.invoke(prompt)
    print(result.content)
    print("\n")