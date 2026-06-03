from langchain_ollama import ChatOllama

# import prompt template
from langchain.prompts import ChatPromptTemplate

# create llm object
llm = ChatOllama(model="llama3.1")

# define a prompt template
# {topic}: variable which will be replaced before sending to the LLM
template = "explain {topic} in 2 bullet points"

# create an prompt template
prompt_template = ChatPromptTemplate.from_template(template=template)

while True:
    # get the topic input from user
    topic = input("enter your topic of interest >> ")
    if topic == "quit":
        break

    # create the prompt by replacing the topic variable
    prompt = prompt_template.invoke({"topic": topic})
    # print(f"prompt = {prompt}")

    # send the prompt and stream the result
    for chunk in llm.stream(prompt):
        print(chunk.content, end="")
    
    print("")