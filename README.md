# Flask Quote API

This repository contains a simple Flask-based REST API application that provides a list of quotes from LeBron James. You can retrieve a specific quote, delete a quote, update a quote, and add a new quote. It's built with Flask and Flask-RESTful.

## Installation

To run this application, you must have Python and pip installed. If you do not have Python, you can download it [here](https://www.python.org/downloads/).

After cloning this repository, navigate into the directory and install the necessary packages using pip:

```bash
pip install -r requirements.txt

The requirements.txt file should contain:
flask
flask-restful

Running the Application
Run the application using the command:

python app.py

By default, the application will run on http://127.0.0.1:5000/.

API Usage
The application provides the following endpoints:

GET /quotes: Get a list of all quotes.
POST /quotes: Add a new quote. The body of the request should be a JSON object with a 'quote' field.
GET /quotes/<quote_id>: Get a specific quote.
PUT /quotes/<quote_id>: Update a specific quote. The body of the request should be a JSON object with a 'quote' field.
DELETE /quotes/<quote_id>: Delete a specific quote.

