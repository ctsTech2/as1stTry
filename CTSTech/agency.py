from agency_swarm import Agency
from Copywriter import Copywriter
from WebDeveloper import WebDeveloper
from Designer import Designer
from CTSTechCEO import CTSTechCEO

ctstech_ceo = CTSTechCEO()
designer = Designer()
web_developer = WebDeveloper()
copywriter = Copywriter()

agency = Agency([ctstech_ceo, [ctstech_ceo, designer],
                 [designer, web_developer],
                 [designer, copywriter]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()