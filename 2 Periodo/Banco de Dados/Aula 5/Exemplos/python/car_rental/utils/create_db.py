from services.database import engine
from models import *

def create_db():
    Base.metadata.create_all(engine)