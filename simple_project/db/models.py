from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Numbers(Base):
    __tablename__ = 'numbers'

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[float]
