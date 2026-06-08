from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyMuPDFLoader
from dotenv import load_dotenv

# load the keys from .env file
load_dotenv()

def load_resume(file_name):
    # create the pdf document loader
    loader = PyMuPDFLoader(file_path=file_name)

    # read the contents from the file
    contents = ""
    pages = loader.load()

    # read the contents from every page
    for page in pages:
        contents += page.page_content

    # send the contents to the caller
    return contents.replace("•", "")

def create_cover_letter(resume_file_name):
    # load the contents from the file
    resume_contents = load_resume(file_name=resume_file_name)

    # create llm
    MODEL = "gpt-5"
    llm = ChatOpenAI(model=MODEL)

    # job details details
    JOB_POSITION = "professor"
    COMPANY_NAME = "sunbeam"

    # person details
    NAME = "amit"
    ADDRESS = "pune"
    EMAIL = "pythoncpp@gmail.com"

    # create a prompt
    template = """
    You are a helpful assistant who can write better resume covering letter.
    Following is the resume of {person_name}, who lives at address {address} and have an email {email}.
    The person wants to apply for {job_position} in {company_name}.

    {resume}

    Write a covering letter for the person to send the company to apply for the job.
    """

    # create prompt template
    prompt_template = ChatPromptTemplate.from_template(template=template)
    
    # create the prompt
    prompt = prompt_template.invoke({
        "person_name": NAME,
        "address": ADDRESS,
        "email": EMAIL,
        "job_position": JOB_POSITION,
        "company_name": COMPANY_NAME,
        "resume": resume_contents
    })

    # send the prompt and get the result
    result = llm.invoke(prompt)
    print(result.content)

create_cover_letter(resume_file_name="amit-kulkarni.pdf")