from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# load all the keys from .env file
load_dotenv()

# create llm
llm = ChatOpenAI(model="gpt-5")

# create a list of messages having the history of user's chat
messages = []

# set the llm tone
messages.append({
    "role": "system",
    "content": "You are a helpful assistant. Answer the users question."
})

# tuple format
# messages.append(("system", "You are a helpful assistant. Answer the users question."))

while True:
    message = input("user > ")
    if message == 'quit':
        break

    # create the prompt
    messages.append({
        "role": "user", 
        "content": message
    })
    
    # send the prompt and get the result
    result = llm.invoke(messages)
    print("")
    print(f"ai > {result}")
    print("\n")

    # add the answer from ai in the messages
    messages.append({
        "role": "ai", 
        "content": result.content
    })