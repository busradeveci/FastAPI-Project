# FastAPI Project
This project is a web application developed using FastAPI, aiming to create fast, efficient, and modern APIs.

## Features
- High-performance API development with FastAPI
- Support for asynchronous operations
- Automatic API documentation (Swagger & ReDoc)
- Easy to extend structure

## Installation

### Requirements
- Python 3.8+
- FastAPI
- Uvicorn

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/Busradeveci/FastAPI-Project.git
    cd FastAPI-Project
    ```

2. Create and activate a virtual environment:
    - For MacOS/Linux:
      ```bash
      python -m venv venv
      source venv/bin/activate
      ```
    - For Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the application:
    ```bash
    uvicorn main:app --reload
    ```

## API Usage
Once the application is running, you can access the API documentation via the following URLs:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
