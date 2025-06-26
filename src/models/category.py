from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import BaseModel
from src.core.db import db


class Category(BaseModel):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(db.String(255), nullable=False)

    polls: Mapped[list['Poll']] = relationship(
        'Poll',
        back_populates='category',
    )

