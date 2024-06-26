from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class WebDeveloper(Agent):
    def __init__(self):
        super().__init__(
            name="WebDeveloper",
            description="This agent focuses on implementing the design and functionality of the websites. It navigates directories, writes, reads, and modifies files, and executes terminal commands.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message

