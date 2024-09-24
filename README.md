# User Data Flask App

This application displays user data from a JSON file using Flask.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Go to the project directory
5. Install dependencies: `pip install -r requirements.txt`
6. Run the application: `python app.py`

## Configuration

The application uses different configurations for development, testing, and production. You can change the configuration by modifying the `config.py` file. The main configuration options are:

- `SECRET_KEY`: Used for session management
- `USERS_JSON_PATH`: Path to the JSON file containing user data
- `ITEMS_PER_PAGE`: Number of users to display per page
- `APPLICATION_NAME`: Name of the application displayed in templates
- `HOMEPAGE_TITLE`: Title for the homepage
- `USER_DETAIL_TITLE`: Title for the user detail page
- `ERROR_404_TITLE` and `ERROR_500_TITLE`: Titles for error pages
- `ERROR_404_MESSAGE` and `ERROR_500_MESSAGE`: Messages for error pages

To use different configurations, you can set the FLASK_CONFIG environment variable before running the application. 

For example:
```
export FLASK_CONFIG=production
python app.py
```

## JSON Data

User data is stored in `users.json`. The file structure should be:

{
    "users": [
        {"id": 1, "username": "example_user", "email": "user@example.com"},
        ...
    ]
}

## Running the Application

To run the application in development mode:

python app.py

The application will be available at `http://localhost:5000`.

## Testing

Run tests using pytest:

pytest

The test suite includes tests for the homepage, user detail page, error pages, and utility functions.

## Routes

- `/`: Display the list of users
- `/user/<int:id>`: Display details for a specific user
- Error pages: 404 (Not Found) and 500 (Internal Server Error)