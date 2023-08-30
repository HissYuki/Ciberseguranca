from models import Base, Person
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import SMALLINT, BIGINT, INTEGER, ForeignKey

class Phone(Base):
    __tablename__ = 'phone'
    country_code: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    ddd:Mapped[int] = mapped_column(SMALLINT, nullable=False)
    phone_number: Mapped[int] = mapped_column(BIGINT, nullable=False)
    person_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Person.id), nullable=False)