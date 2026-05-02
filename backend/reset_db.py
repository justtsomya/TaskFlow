"""
Run this ONCE to wipe all existing users, projects, and tasks from the database.
After running, you can create fresh admin and member accounts from the signup page.

Usage:
    python reset_db.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from database import engine, SessionLocal
import models

def reset():
    print("Creating/verifying database tables...")
    models.Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        task_count = db.query(models.Task).count()
        project_count = db.query(models.Project).count()
        user_count = db.query(models.User).count()
        print(f"Found: {user_count} users, {project_count} projects, {task_count} tasks")

        confirm = input("Delete ALL users, projects, and tasks? Type YES to confirm: ").strip()
        if confirm != "YES":
            print("Aborted.")
            return

        db.query(models.Task).delete()
        db.query(models.Project).delete()
        db.query(models.User).delete()
        db.commit()
        print("✅ All data wiped. Database is clean.")
        print("You can now register fresh admin and member accounts via the signup page.")
    finally:
        db.close()

if __name__ == "__main__":
    reset()
