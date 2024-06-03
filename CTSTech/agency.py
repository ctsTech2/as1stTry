from agency_swarm import Agency
from ToolMaker import ToolMaker
from CTSTechCEO import CTSTechCEO
from Designer import Designer
from WebDeveloper import WebDeveloper
from Copywriter import Copywriter
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the OpenAI API key is set
if 'OPENAI_API_KEY' not in os.environ:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

# Instantiate the agents
ctstech_ceo = CTSTechCEO()
designer = Designer()
web_developer = WebDeveloper()
copywriter = Copywriter()
tool_creator = ToolCreator()

# Create the agency with the defined agents
agency = Agency(
    [
        ctstech_ceo, 
        designer, 
        web_developer, 
        copywriter,
        [ctstech_ceo, designer], 
        [designer, web_developer], 
        [designer, copywriter]
    ],
    shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
    max_prompt_tokens=25000,  # default tokens in conversation for all agents
    temperature=0.3  # default temperature for all agents
)

if __name__ == '__main__':
    agency.demo_gradio()
