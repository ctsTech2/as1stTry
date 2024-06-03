from agency_swarm.tools import BaseTool
from pydantic import Field

class FileReadWrite(BaseTool):
    """
    This tool reads and writes files for managing tool configurations and scripts. 
    It accepts parameters such as file path and content for writing, and file path for reading.
    """

    file_path: str = Field(
        ..., description="The path of the file to read from or write to."
    )
    content: str = Field(
        None, description="The content to write to the file. If None, the tool will read from the file."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will either read from or write to the file specified by the file_path.
        """
        if self.content is not None:
            # Write content to the file
            try:
                with open(self.file_path, 'w') as file:
                    file.write(self.content)
                return f"Content written to {self.file_path} successfully."
            except Exception as e:
                return f"Failed to write to {self.file_path}. Error: {str(e)}"
        else:
            # Read content from the file
            try:
                with open(self.file_path, 'r') as file:
                    content = file.read()
                return content
            except Exception as e:
                return f"Failed to read from {self.file_path}. Error: {str(e)}"