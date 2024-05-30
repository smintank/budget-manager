from datetime import datetime

from sqlalchemy.types import String, Integer, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.v1.users.models import User, budgets_users
from core.database import Base


class Budget(Base):
    __tablename__ = 'budgets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    current_amount: Mapped[int] = mapped_column(Integer())
    user: Mapped['User'] = relationship('User', secondary=budgets_users, back_populates='budgets')
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now)
    transactions: Mapped['Transaction'] = relationship('Transaction', back_populates='budget')

    def __repr__(self) -> str:
        return f'Budget(id={self.id!r}, name={self.name!r})'


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    slug: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    transaction: Mapped['Transaction'] = relationship('Transaction', back_populates='category')

    def __repr__(self) -> str:
        return f'Category(id={self.id!r}, name={self.name!r})'


class Currency(Base):
    __tablename__ = 'currencies'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    symbol: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    transaction: Mapped['Transaction'] = relationship('Transaction', back_populates='currency')

    def __repr__(self) -> str:
        return f'Currency(id={self.id!r}, name={self.name!r})'


class Transaction(Base):
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Float())
    budget: Mapped['Budget'] = relationship('Budget', back_populates='transactions')
    currency: Mapped['Currency'] = relationship('Currency', back_populates='transactions')
    category: Mapped['Category'] = relationship('Category', back_populates='transactions')
    sms_text: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now)
    location: Mapped[str] = mapped_column(String(255), nullable=True)
    source: Mapped[str] = mapped_column(String(255), nullable=True)

    def __repr__(self) -> str:
        return f'Transaction(id={self.id!r}, amount={self.amount!r})'
