# Flask Quote API

This repository contains a simple Flask-based REST API application that provides a list of quotes from LeBron James. You can retrieve a specific quote, delete a quote, update a quote, and add a new quote. It's built with Flask and Flask-RESTful.

## Installation

To run this application, you must have Python and pip installed. If you do not have Python, you can download it [here](https://www.python.org/downloads/).

After cloning this repository, navigate into the directory and install the necessary packages using pip:

## Requirements

The requirements contain:

- `flask`  
- `flask-restful` 

## Preview
<img width="1088" alt="Screenshot 2023-07-05 at 2 01 34 AM" src="https://github.com/AmaroTruong/LebronQuoteRestfulApi/assets/137460611/00e521a2-7487-42e0-b4a6-44c51da3a9b0">


## API Usage
The application provides the following endpoints:

1.GET /quotes: Get a list of all quotes.
2.POST /quotes: Add a new quote. The body of the request should be a JSON object with a 'quote' field.
3.GET /quotes/<quote_id>: Get a specific quote.
4.PUT /quotes/<quote_id>: Update a specific quote. The body of the request should be a JSON object with a 'quote' field.
5.DELETE /quotes/<quote_id>: Delete a specific quote.


