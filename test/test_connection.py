from sqlalchemy import create_engine
from backend_package.config import settings

def test_connection():
    try:
        engine = create_engine(settings.DATABASE_URL)
        with engine.connect() as connection:
            result = connection.execute("SELECT version();")
            version = result.fetchone()
            print("Connected to - ", version)
    except Exception as e:
        print("Error while connecting to PostgreSQL", e)

if __name__ == "__main__":
    test_connection()
