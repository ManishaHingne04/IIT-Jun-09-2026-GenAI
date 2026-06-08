from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# load all the keys from .env file
load_dotenv()

# define the prompt for blog article generation
template = """
You are an expert SEO content writer. Write a comprehensive, SEO-optimized blog article on the topic: "{topic}".  

Requirements:  
1. Generate an SEO title (max 60 characters) containing the keyword.  
2. Write a meta description (150–160 characters) including the keyword.  
3. Suggest a URL slug.  
4. Provide 5–10 related LSI keywords.  
5. Structure the blog with:  
   - Introduction (engaging, mention the main keyword).  
   - Well-organized sections with H2/H3 headings using keyword variations.  
   - Actionable insights, examples, or explanations.  
   - Conclusion with a call to action.  
6. Keep paragraphs short (2–4 sentences) and use bullet points or lists when helpful.  
7. Include 3–5 FAQs with concise answers that use the main keyword and related terms.  
8. Maintain a conversational yet professional tone.  
"""

# create prompt template
prompt_template = ChatPromptTemplate.from_template(template)

# create prompt
TOPIC = "Large Language Model affecting the developers ability to develop code"
prompt = prompt_template.invoke({"topic": TOPIC})

# create llm
llm = ChatOpenAI(model="gpt-5")

# send the prompt and get the result
result = llm.invoke(prompt)
print(result.content)