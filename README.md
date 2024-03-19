# Weather City App

This application consumes a Weather REST API to fetch weather data for a given city.

## Installation

To install the required dependencies, run the following command in your terminal:

pip install -r requirements.txt

This command will install the necessary Python packages listed in the requirements.txt file.

# Configuration

Before running the application, create a .env file in the project directory and set the API_URL variable to the localhost URL of the REST API that is running locally. 

- `API_URL`: This is where you put the localhost to your REST API

Here is an example:
API_URL=http://localhost:8000

# Usage
To run the application, execute the following command in your terminal:
python app.py

This command will start the application.

Once the application is running, you can search for weather data by entering a city name. The application will display the weather information for the specified city. To quit the application, simply type 'quit' and press Enter.