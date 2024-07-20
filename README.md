# Bookstore Project
The BookStore API is a RESTful API built with FastAPI that allows users to manage a collection of books. It includes user authentication and authorization features, along with CRUD operations for books.


#### `requirements.txt`

annotated-types==0.7.0
anyio==4.4.0
astroid==3.2.3
bcrypt==4.1.3
black==24.4.2
certifi==2024.7.4
click==8.1.7
colorama==0.4.6
coverage==7.6.0
dill==0.3.8
dnspython==2.6.1
ecdsa==0.19.0
email_validator==2.2.0
fastapi==0.111.1
fastapi-cli==0.0.4
h11==0.14.0
httpcore==1.0.5
httptools==0.6.1
httpx==0.27.0
idna==3.7
iniconfig==2.0.0
isort==5.13.2
Jinja2==3.1.4
markdown-it-py==3.0.0
MarkupSafe==2.1.5
mccabe==0.7.0
mdurl==0.1.2
motor==3.5.1
mypy-extensions==1.0.0
packaging==24.1
passlib==1.7.4
pathspec==0.12.1
platformdirs==4.2.2
pluggy==1.5.0
pyasn1==0.6.0
pycryptodome==3.20.0
pydantic==2.8.2
pydantic_core==2.20.1
Pygments==2.18.0
PyJWT==2.8.0
pylint==3.2.5
pymongo==4.8.0
pytest==8.2.2
pytest-asyncio==0.23.8
pytest-cov==5.0.0
python-dotenv==1.0.1
python-jose==3.3.0
python-multipart==0.0.9
PyYAML==6.0.1
rich==13.7.1
rsa==4.9
shellingham==1.5.4
six==1.16.0
sniffio==1.3.1
starlette==0.37.2
tomlkit==0.13.0
typer==0.12.3
typing_extensions==4.12.2
uvicorn==0.30.1
watchfiles==0.22.0
websockets==12.0


## Project Structure
The project follows a standard FastAPI structure with the following directory and file layout:

BookStoreProject/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── routes.py
│ ├── schemas.py
│ ├── auth.py
│ ├── config.py
│ └── dependencies.py
├── .env
├── requirements.txt
└── README.md



### File Descriptions

- **`app/__init__.py`**: Initializes the `app` package. This file is usually empty or contains package-level docstrings.

- **`app/main.py`**: The entry point of the FastAPI application. Contains the FastAPI app initialization and includes routing configuration.

- **`app/database.py`**: Contains the database connection logic. Manages connections to MongoDB and provides access to collections.

- **`app/models.py`**: Defines Pydantic models and custom types used throughout the application. Includes models for data validation and serialization.

- **`app/routes.py`**: Contains route definitions for handling HTTP requests. Implements CRUD operations for books and user-related endpoints.

- **`app/schemas.py`**: Defines request and response schemas using Pydantic models. Includes data structures for creating, updating, and retrieving books and users.

- **`app/auth.py`**: Implements authentication and authorization logic. Contains functions for user authentication, token generation, and validation.

- **`app/config.py`**: Manages configuration settings and environment variables. Loads configurations required for the application to run.

- **`app/dependencies.py`**: Contains dependency functions used in routes, such as retrieving the current user or handling other common tasks.

- **`.env`**: Environment file where sensitive configurations and environment-specific variables are stored (e.g., database URL, secret key).

- **`requirements.txt`**: Lists the Python packages required to run the project. Use `pip install -r requirements.txt` to install dependencies.

- **`README.md`**: Provides project documentation, including setup instructions, API usage, and other relevant information.



## Setup

1. **Coding in VS Code Studio:**


2. **Create and activate a virtual environment:**

    
    python -m venv env
    source env/bin/activate  
    

3. **Install the dependencies:**

    
    pip install -r requirements.txt
    

4. **Set up environment variables:**

    Create a `.env` file in the root of your project and add the following variables:

    
    MONGO_URL=mongodb://localhost:27017
    DATABASE_NAME=your_database_name
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    

5. **Start the MongoDB server:**

    Start mongoDB

## Running the Project

1. **Run the FastAPI application:**

    
    uvicorn app.main:app --reload
  

2. **Access the API documentation:**

    Open  browser or Postman

## API Endpoints

### Authentication

- **Login:**

   
    POST "http://127.0.0.1:8000/login
    

    Request Body:
   
    {
      "username": "your_username",
      "password": "your_password"
    }
    

    Response:
    
    {
      "access_token": "your_access_token",
      "token_type": "bearer"
    }
    

### Users

- **Register a new user:**

    POST "http://127.0.0.1:8000/users/

    Request Body:
    
    {
      "username": "your_username",
      "email": "your_email@example.com",
      "password": "your_password"
    }
    

    Response:
    
    {
      "id": "user_id",
      "username": "your_username",
      "email": "your_email@example.com"
    }
    

### Books

- **Create a new book:**

   

    Request Body:
   
    {
      "title": "Book Title",
      "author": "Author Name",
      "published_date": "2023-01-01",
      "isbn": "123-456-789"
    }
  

    Response:
    
    {
      "id": "book_id",
      "title": "Book Title",
      "author": "Author Name",
      "published_date": "2023-01-01",
      "isbn": "123-456-789"
    }
   

- **Get all books:**

    Response:
    
    [
      {
        "id": "book_id",
        "title": "Book Title",
        "author": "Author Name",
        "published_date": "2023-01-01",
        "isbn": "123-456-789"
      }
    ]
   

- **Get a single book by ID:**

    Response:
   
    {
      "id": "book_id",
      "title": "Book Title",
      "author": "Author Name",
      "published_date": "2023-01-01",
      "isbn": "123-456-789"
    }
   

- **Update a book by ID:**

    Request Body:

    {
      "title": "Updated Title",
      "author": "Updated Author",
      "published_date": "2023-01-01",
      "isbn": "123-456-789"
    }


    Response:

    {
      "id": "book_id",
      "title": "Updated Title",
      "author": "Updated Author",
      "published_date": "2023-01-01",
      "isbn": "123-456-789"
    }


- **Delete a book by ID:**

    Response:

    {
      "message": "Book deleted successfully"
    }


## Authentication Process

1. **Register a new user:**

    Use the `/register` endpoint to create a new user.

2. **Login to get the token:**

    Use the `/login` endpoint to obtain a JWT token. The token will be used for authenticated requests.

3. **Include the token in requests:**

    For endpoints that require authentication (e.g., creating, updating, or deleting books), include the token in the `Authorization` header:

    ```http
    Authorization: Bearer your_access_token
    ```

##Conclusion


This documentation provides a comprehensive guide to setting up, running, and using the BookStore API. Follow the instructions carefully to ensure a smooth setup and usage experience. If you encounter any issues or have any questions, please feel free to open an issue on the project's GitHub repository.


## For Screen Shots

refer to this link- https://drive.google.com/drive/folders/1pWy2cUPj6L2ro6RJuwe_IS9MedbLXph_?usp=sharing
