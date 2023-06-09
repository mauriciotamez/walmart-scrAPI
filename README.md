# Walmart Scraping Script

This script is a Python program that utilizes the Selenium and BeautifulSoup libraries to perform web scraping on the Walmart Mexico website. It extracts department names, URLs, and corresponding subdepartments from the website.

## Project Build

This project utilizes a Python script, `build_docker_image.py`, to automate the build process,
and a `run_docker_image.py` to run the docker image on localhost port 8000.

The script executes specific commands to build the project, including Docker commands.

## Requirements

Before going to the installation process, ensure that the following requirements are met:

- Python 3 or higher is installed on your system.
- Docker is installed and properly configured on your system.

If you do not have this installed on your system please refer to:

[Docker installation](https://docs.docker.com/get-docker/)

[Python installation](https://www.python.org/downloads/)

## Installation

1. Clone the project repository:

   ```shell
   git clone https://github.com/mauriciotamez/walmart-scrAPI.git

2. Navigate to the project directory:

   ```shell
   cd walmartscrappy

To run the build process for the project, follow these steps:

1. Open a terminal or command prompt and navigate to your project.

   ```shell
   cd walmartscrappy

2. Execute the build_docker_image.py script using the Python interpreter:

   ```shell
   python build_docker_image.py

This will execute the build script and perform the necessary steps to build the project.

## Run the docker image.

1. Execute the run_docker_image.pyscript using the Python interpreter:

   ```shell
   python run_docker_image.py

This will execute the run script and you should look something like `Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)` on your shell.

## Usage.

The image that you are running now has only one endpoint.

 GET : `http://localhost:8000/departments`

This will return all departments from walmart with their respective subdepartments in a JSON response.
    
    
## Description

The script performs the following steps:

1. Imports the necessary libraries and modules, including  `selenium`, `BeautifulSoup`, `os`, and `logging`.

2. Sets up Firefox options for the Selenium WebDriver. In this script, it is configured to run in headless mode, meaning the browser window will not be displayed during execution.

3. Sets the logging level and disables logging for the WebDriver Manager to avoid unnecessary log output.

4. Creates a WebDriver service using the GeckoDriverManager to manage the Firefox WebDriver.

5. Creates a WebDriver instance using the Firefox browser and the configured options.

6. Defines the URL to be scraped and visits the webpage using the WebDriver.

7. Locates the department wrapper element on the page using CSS selectors.

8. Extracts department information by iterating through each department element and its corresponding HTML tags.

9. Uses BeautifulSoup to parse the HTML and extract the department name and URL.

10. Checks if the department name has already been processed to avoid duplicates.

11. Extracts subdepartments for each department by finding the relevant HTML elements and extracting the subcategory name and URL.

12. Constructs a dictionary for each category, including the department name, URL, and subdepartments, and appends it to the list of categories.

13. Quits the WebDriver, closing the browser window.


## Additional Notes

- Make sure Docker is running and properly configured on your system before executing the ``` build_docker_image.py``` script. If Docker is not installed, refer to the official Docker documentation for installation instructions specific to your operating system.

- The ```build_docker_image.py``` script provided in this project is just an example. You can modify it according to your specific build requirements, including additional commands or customizations.


### License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it according to the terms of the license.

**Note:** This script is provided as an example and should be used responsibly and in accordance with the website's terms of service. Make sure to respect the website's policies and ensure that your scraping activities are legal and ethical.














