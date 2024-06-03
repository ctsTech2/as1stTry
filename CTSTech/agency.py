from agency_swarm import Agency
from CTSTechCEO import CTSTechCEO
from Designer import Designer
from WebDeveloper import WebDeveloper
from Copywriter import Copywriter

# Instantiate the agents
ctstech_ceo = CTSTechCEO()
designer = Designer()
web_developer = WebDeveloper()
copywriter = Copywriter()

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
