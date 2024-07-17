from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

PROD_DATABASE_URL = settings.PROD_DATABASE_URL

# Determine the environment (dev or prod)
ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')  # Set 'prod' in production environment

# Create engine based on environment
if ENVIRONMENT == 'dev':
    # SQLite connection
    engine = create_engine('sqlite:///dev_database.db')

elif ENVIRONMENT == 'prod':
    # PostgreSQL connection
    engine = create_engine(PROD_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
