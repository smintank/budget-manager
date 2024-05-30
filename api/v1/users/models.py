from sqlalchemy import ForeignKey, text, Table, Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base

budgets_users = Table(
    'budgets_users', Base.metadata,
    Column('budget_id', Integer, ForeignKey('budgets.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(40))
    first_name: Mapped[str] = mapped_column(String(40), nullable=True)
    last_name: Mapped[str] = mapped_column(String(40), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False)
    is_staff: Mapped[bool] = mapped_column(default=False)
    hashed_password: Mapped[str] = mapped_column(String(255))

    budget: Mapped['Budget'] = relationship('Budget', secondary=budgets_users, back_populates='user')
    token: Mapped['Token'] = relationship('Token', uselist=False, back_populates='user',)
    settings: Mapped['Settings'] = relationship('Settings', uselist=False, back_populates='user')

    def __repr__(self) -> str:
        return f'User(id={self.id!r}, name={self.username!r})'


class Token(Base):
    __tablename__ = 'tokens'

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        server_default=text('uuid_generate_v4()'),
        unique=True,
        nullable=False,
        index=True
    )
    user: Mapped['User'] = relationship('User', back_populates='token')
    expires = mapped_column(DateTime(), nullable=False)


class Settings(Base):
    __tablename__ = 'settings'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped['User'] = relationship('User', back_populates='settings')
    language: Mapped[str] = mapped_column(String(20), default='ru')
    currency: Mapped[str] = mapped_column(String(20), default='rub')
