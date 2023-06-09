from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Post import Base
from dbconfig import DB_CONFIG

# Baca konfigurasi db
username, password, host, database, raise_on_warnings = DB_CONFIG.values()

# Config to connect to the db
db_url = f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)

# Create table in db
Base.metadata.create_all(engine)
