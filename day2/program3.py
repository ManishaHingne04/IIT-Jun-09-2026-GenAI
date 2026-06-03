# load the class ChatOllama to load the model using Ollama
from langchain_ollama import ChatOllama

# create the model
llm = ChatOllama(model="llama3.1")

# create prompt
prompt = "explain LLM in 2 bullet points"

# send the prompt and get the response
# result = llm.invoke(prompt)
# print(result.content)

# send the prompt and stream the result
for chunk in llm.stream(prompt):
    print(chunk.content, end="")