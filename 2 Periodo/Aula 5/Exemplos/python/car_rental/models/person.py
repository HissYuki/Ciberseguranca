from models.base import Base


from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, CHAR, DATE, VARCHAR
from datetime import date

class Person(Base):
    __tablename__ = 'person'
    id: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True, autoincrement=True)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    name: Mapped[str] = mapped_column('person_name', VARCHAR(256), nullable=False)
    rg: Mapped[str] = mapped_column(VARCHAR(12), nullable=False, unique=True)
    birth_date: Mapped[date] = mapped_column(DATE, nullable=False)

    emails: Mapped[list['Email']] = relationship('Email', backref='person', lazy=True)
    phones: Mapped[list['Phone']] = relationship('Phone', backref='person', lazy=True)