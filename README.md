# Happy Bank

Happy Bank is an educational project that demonstrates how to build a simple banking API using FastAPI and SQLModel. It provides endpoints for managing accounts, including creating accounts, withdrawing, depositing, and transferring money between accounts. The codebase uses a repository and service pattern for clean separation of concerns and supports SQLite as the database backend.

Main features:
- RESTful API for account operations
- Repository and service layers for business logic
- Database migrations and default data initialization
- Easily extensible for new banking features

To get started, install the dependencies from `requirements.txt` and run the FastAPI application.

## Quickstart

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate # On unix based systems use: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI application with Uvicorn
uvicorn app.main:app --reload
```

Open your browser and navigate to `http://localhost:8000/docs` to access the interactive API documentation provided by FastAPI.

### Repeated Run

```bash
# Join the virtual environment if not already activated
venv\Scripts\activate # On unix based systems use: source venv/bin/activate

# Run the FastAPI application with Uvicorn
uvicorn app.main:app --reload
```

## Database Initialization

Whenever you modify the database models or default data, you should delete the existing SQLite database file (`./app.db`) to apply the changes. The application will automatically create a new database with the updated schema and default data on the next run.
