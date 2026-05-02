import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./taskpro.db")

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

# Secret code required to register as admin.
# Change this before deploying!
ADMIN_SECRET_CODE = "TASKPRO-ADMIN-2024"
