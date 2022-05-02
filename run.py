"""Flask CLI/Application entry point."""
import os

from user_mgmt import create_app, db
from user_mgmt.models.token_blacklist import BlacklistedToken
from user_mgmt.models.user import User

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db, "User": User, "BlacklistedToken": BlacklistedToken}
