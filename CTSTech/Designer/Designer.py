from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class Designer(Agent):
    def __init__(self):
        super().__init__(
            name="Designer",
            description="This agent is responsible for the visual design and user experience. It can communicate with the Web Developer and Copywriter.",
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

