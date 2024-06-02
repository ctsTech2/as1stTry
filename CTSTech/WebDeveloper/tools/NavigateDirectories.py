from agency_swarm.tools import BaseTool
from pydantic import Field
import os

class NavigateDirectories(BaseTool):
    """
    This tool allows the agent to navigate through directories. It provides functionalities to change the current directory,
    list the contents of a directory, and check the current directory path.
    """

    action: str = Field(
        ..., description="The action to perform: 'change_dir', 'list_contents', or 'current_path'."
    )
    target_directory: str = Field(
        None, description="The target directory for 'change_dir' action. Not required for other actions."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        if self.action == 'change_dir':
            if self.target_directory:
                try:
                    os.chdir(self.target_directory)
                    return f"Changed directory to {self.target_directory}"
                except FileNotFoundError:
                    return f"Directory {self.target_directory} not found"
                except NotADirectoryError:
                    return f"{self.target_directory} is not a directory"
                except PermissionError:
                    return f"Permission denied to change to {self.target_directory}"
            else:
                return "Target directory must be specified for 'change_dir' action"

        elif self.action == 'list_contents':
            try:
                contents = os.listdir(os.getcwd())
                return f"Contents of the current directory: {contents}"
            except PermissionError:
                return "Permission denied to list contents of the current directory"

        elif self.action == 'current_path':
            current_path = os.getcwd()
            return f"Current directory path: {current_path}"

        else:
            return "Invalid action specified. Use 'change_dir', 'list_contents', or 'current_path'."