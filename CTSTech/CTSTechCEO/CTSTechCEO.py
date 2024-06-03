from agency_swarm.agents import Agent

class CTSTechCEO(Agent):
    def __init__(self):
        super().__init__(
            name="CTSTechCEO",
            description="This agent oversees the entire agency and ensures that all projects align with the agency's goals and mission. It can communicate with the Designer.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message

