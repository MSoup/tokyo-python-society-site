# Tokyo Python Society Site - Overview Proposal

## Tools Used in Development
Language: Python 3.10  
Libraries: FastAPI  
Database: Postgres (version to be determined)  
Formatter: Black 22.8.0  
Testing: PyTest  

## Branch Information

I propose three branches:

- production  
This is the production branch. Changes to this branch will ultimately affect the live site.

- staging  
This is the staging branch. Changes to this branch will affect a staging version of the application.

- dev  
This is the development branch. Changes to this branch are local

## Setting Up the Environment

1. Install Python 3.10

2. Install the dependencies from requirements.txt. *I recommend a virtual environment.*

This will install everything needed to get the app running. The core app consists of:
- Pytest
- FastAPI
- uvicorn

Everything else seen in requirements.txt are dependencies of the above three.

3. Install the appropriate code formatter. See `Tools` above for the formatter we use. 

## Running the App

`uvicorn main:app --reload`

## Seeing the endpoints

`http://127.0.0.1:8000/docs`

^ Provided by Swagger UI

## Alternative API docs

`http://127.0.0.1:8000/redoc`