from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Connect to LM Studio local server
llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",   # any string works
    model="local-model"    # model name is ignored by LM Studio
)

# Prompt template
template = "Explain {topic} in 2 bullet points"

prompt_template = ChatPromptTemplate.from_template(template)

while True:
    topic = input("Enter your topic of interest >> ")

    if topic.lower() == "quit":
        break

    # Create prompt
    prompt = prompt_template.invoke({"topic": topic})

    # Stream response
    for chunk in llm.stream(prompt):
        print(chunk.content, end="", flush=True)

    print("\n")