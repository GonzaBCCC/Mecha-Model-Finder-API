# Mecha-Model-Finder-API
This is a full-stack web application designed to showcase a comprehensive development workflow, from data collection and API design to front-end application development. The project focuses on creating and managing a database of anime model kits.
# Project Description
This full-stack app showcases a custom RESTful API for anime model kit data. It features a Python back end with full CRUD functionality, complemented by a JavaScript front end for data display and management. The project also includes a safe Python scraper to populate the database.
# Technical Stack
* __Back-end:__ Python with Flask
* __Front-end:__ HTML, CSS (Tailwind CSS), and JavaScript
* __Data Collection:__ Python with requests and BeautifulSoup
* __Database:__ In-memory dictionary (for this demonstration)

# Key Features
* __RESTful API:__ A well-structured API with endpoints for retrieving, creating, updating, and deleting model kit data.
* __Safe Web Scraper:__ A Python script designed to ethically scrape public data, demonstrating responsible data collection practices.
* __Dynamic Front-end:__ A single-page application that interacts with the API to search, display, and manage model kit data.
* __Responsive Design:__ The front-end is built with Tailwind CSS, ensuring a clean and professional look on all devices.
* __CORS Enabled:__ The API includes a CORS policy to allow cross-origin requests from the front-end application.
# Getting Started
## Prequisites
* Python 3.x
* pip package manager
## Installation
1. Clone this repository
```python
git clone [https://github.com/GonzaBCCC/Mecha-Model-Finder-API.git](https://github.com/GonzaBCCC/Mecha-Model-Finder-API.git)
cd Mecha-Model-Finder-API
```

2. Install the required Python packages:
```python
pip install Flask Flask-Cors requests beautifulsoup4
```
## Running the Project
1. Start the API:
Open a terminal in the project directory and run the Flask application:
```python
python scalemates_api.py
```
The API will be running at ```http://127.0.0.1:5000```.
2. View the Front-end:
Open the ```index.html``` file in your web browser. You can use a local web server for a better experience, but simply opening the file will also work.
# How to Use the API
You can interact with the API using a tool like Postman or curl.
* ```GET http://127.0.0.1:5000/kits``` - Retrieve all kits.
* ```GET http://127.0.0.1:5000/kits/<kit_id>``` - Retrieve a single kit by its ID.
* ```POST http://127.0.0.1:5000/kits``` - Create a new kit. (Requires JSON body)
* ```PUT http://127.0.0.1:5000/kits/<kit_id>``` - Update an existing kit. (Requires JSON body)
* ```DELETE http://127.0.0.1:5000/kits/<kit_id>``` - Delete a kit.

# License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
