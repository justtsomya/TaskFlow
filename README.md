# TaskPro v2 — Setup & Run Guide

## Backend Setup

```bash
cd backend
pip install -r requirements.txt

# FIRST TIME or to wipe all old users/data:
python reset_db.py

# Start the server
uvicorn main:app --reload
```

Server runs at: http://127.0.0.1:8000

## Admin Secret Code

The secret code to register as **Admin** is set in `backend/config.py`:

```python
ADMIN_SECRET_CODE = "TASKPRO-ADMIN-2024"
```

**Change this before deploying** to something only you know.

## Creating Accounts

1. Go to `frontend/signup.html`
2. For **Member** accounts: just fill username + password
3. For **Admin** accounts: select Admin role → enter the secret code above

## Fixes Applied

- ✅ Backend database file name made consistent (`taskpro.db`)
- ✅ `models.py` — proper file formatting, `assigned_to` made nullable
- ✅ `schemas.py` — added `admin_code` field, `TaskStatusUpdate` schema
- ✅ `main.py` — signup validates admin secret code; anyone trying to register as admin without the code gets rejected
- ✅ `main.py` — `update_task_status` now accepts a `{status}` body (was hardcoded to "completed")
- ✅ `signup.html` — admin secret code field shown only when Admin role is selected
- ✅ `dashboard.html` — `markDone()` sends proper JSON body to backend
- ✅ `reset_db.py` — script to wipe all existing users/projects/tasks
