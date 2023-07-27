from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = ""
SQLALCHEMY_DATABASE_URL = "postgresql://testdb_32tc_user:j3wGjNTSLxbFBVetyfLhMqNTuuIKavno@dpg-chnr3i82qv207f352r60-a.frankfurt-postgres.render.com/testdb_32tc"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()