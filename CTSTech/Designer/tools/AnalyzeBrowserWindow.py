from agency_swarm.tools import BaseTool
from pydantic import Field
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnalyzeBrowserWindow(BaseTool):
    """
    This tool analyzes the current browser window, including its dimensions, viewport size, and any relevant user interface elements.
    The tool returns a detailed report of the browser window's properties, which can be used to inform design decisions.
    """

    url: str = Field(
        ..., description="The URL of the webpage to analyze."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        # Initialize the WebDriver (assuming ChromeDriver is in PATH)
        driver = webdriver.Chrome()

        # Open the specified URL
        driver.get(self.url)

        # Get the dimensions of the browser window
        window_size = driver.get_window_size()
        window_width = window_size['width']
        window_height = window_size['height']

        # Get the dimensions of the viewport
        viewport_width = driver.execute_script("return window.innerWidth;")
        viewport_height = driver.execute_script("return window.innerHeight;")

        # Get relevant user interface elements (example: title and meta description)
        title = driver.title
        meta_description = driver.find_element(By.NAME, "description").get_attribute("content") if driver.find_elements(By.NAME, "description") else "No meta description found"

        # Close the WebDriver
        driver.quit()

        # Create a detailed report
        report = {
            "window_width": window_width,
            "window_height": window_height,
            "viewport_width": viewport_width,
            "viewport_height": viewport_height,
            "title": title,
            "meta_description": meta_description
        }

        # Return the report as a string
        return str(report)