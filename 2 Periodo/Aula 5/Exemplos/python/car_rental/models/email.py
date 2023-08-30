from models import Base, Person
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, INTEGER, ForeignKey

class Email(Base):
    __tablename__ = 'email'
    email: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
    id_person: Mapped[int] = mapped_column(INTEGER, ForeignKey(Person.id), nullable=False, unique=True)