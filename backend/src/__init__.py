# src/__init__.py

# Import necessary components from the database module
from database import db_session, init_db, Base  # Absolute imports
from database.models import Contract  # Optional: Importing specific models

# Print statements for verification
print(db_session)  # This will show the db_session object or function
print("Hello world")  # Confirmation message
