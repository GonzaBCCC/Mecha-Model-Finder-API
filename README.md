# Mecha-Model-Finder-API
This is a full-stack web application designed to showcase a comprehensive development workflow, from data collection and API design to front-end application development. The project focuses on creating and managing a database of anime model kits.
# Project Description
This full-stack app showcases a custom RESTful API for anime model kit data. It features a Python back end with full CRUD functionality, complemented by a JavaScript front end for data display and management. The project also includes a safe Python scraper to populate the database.
# Technical StackBack-end: 
## Python with Flask
## Front-end: HTML, CSS (Tailwind CSS), and JavaScript
## Data Collection: 
Python with requests and BeautifulSoupDatabase: 
In-memory dictionary (for this demonstration)
Key Features
RESTful API: A well-structured API with endpoints for retrieving, creating, updating, and deleting model kit data.
Safe Web Scraper: A Python script designed to ethically scrape public data, demonstrating responsible data collection practices.
Dynamic Front-end: A single-page application that interacts with the API to search, display, and manage model kit data.
Responsive Design: The front-end is built with Tailwind CSS, ensuring a clean and professional look on all devices.
CORS Enabled: The API includes a CORS policy to allow cross-origin requests from the front-end application.
# Getting Started
Prerequisites
Python 3.x
pip package manager
Installation
Clone this repository:git clone [https://github.com/your-username/Mecha-Model-Finder-API.git](https://github.com/your-username/Mecha-Model-Finder-API.git)
cd Mecha-Model-Finder-API
Install the required Python packages:
pip install Flask Flask-Cors requests beautifulsoup4
Running the ProjectStart the API:
Open a terminal in the project directory and run the Flask application:
python scalemates_api.py
The API will be running at http://127.0.0.1:5000.
View the Front-end:
Open the index.html file in your web browser. You can use a local web server for a better experience, but simply opening the file will also work.
# How to Use the API
You can interact with the API using a tool like Postman or curl.
GET http://127.0.0.1:5000/kits - Retrieve all kits.
GET http://127.0.0.1:5000/kits/<kit_id> - Retrieve a single kit by its ID.
POST http://127.0.0.1:5000/kits - Create a new kit. (Requires JSON body)
PUT http://127.0.0.1:5000/kits/<kit_id> - Update an existing kit. (Requires JSON body)
DELETE http://127.0.0.1:5000/kits/<kit_id> - Delete a kit.
#License
This project is licensed under the MIT License. See the LICENSE file for details.
