from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
import os

api_url = "https://api.example.com/create_tool"
api_key = os.getenv("API_KEY")

class CreateToolAPI(BaseTool):
    """
    This tool creates new tools using the provided APIs. It accepts parameters such as agent name, tool name, requirements, details, mode, and agency name.
    """

    agent_name: str = Field(
        ..., description="The name of the agent for whom the tool is being created."
    )
    tool_name: str = Field(
        ..., description="The name of the tool to be created."
    )
    requirements: str = Field(
        ..., description="The requirements for the tool."
    )
    details: str = Field(
        ..., description="Detailed description of the tool."
    )
    mode: str = Field(
        ..., description="The mode in which the tool will operate."
    )
    agency_name: str = Field(
        ..., description="The name of the agency to which the tool belongs."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        payload = {
            "agent_name": self.agent_name,
            "tool_name": self.tool_name,
            "requirements": self.requirements,
            "details": self.details,
            "mode": self.mode,
            "agency_name": self.agency_name
        }
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(api_url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return f"Tool '{self.tool_name}' created successfully for agent '{self.agent_name}' in agency '{self.agency_name}'."
        else:
            return f"Failed to create tool. Status code: {response.status_code}, Response: {response.text}"