from app import db, app
import os

with app.app_context():
    db.create_all()
    db_path = os.path.abspath("database.db")
    print("✅ Tables created in:", db_path)
    print("📁 Files in folder:")
    print(os.listdir(os.path.dirname(db_path)))
