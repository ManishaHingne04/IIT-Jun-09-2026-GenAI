## installation

```bash

# install required packages
> pip3 install langchain langchain-openai langchain-ollama python-dotenv

```

## API keys

- to create new API Key for OpenAI ChatGPT
  - https://platform.openai.com/api-keys

## Ollama

```bash

# get the models installed by ollama
> ollama ls

# download a model
# to get the list of models to download: https://ollama.com/search
# > ollama pull <model name>
> ollama pull llama3.1

# get information of selected model
# > ollama show <model name>
> ollama show llama3.1

# load the model
# > ollama run <model name>
> ollama run llama3.1

# remove a model
# > ollama rm <model name>
> ollama rm llama3.1

```
