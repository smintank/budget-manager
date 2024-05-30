import re

from api.v1.budget.models import Transaction, Budget, Currency
from api.v1.users.models import User
from core.database import Session as session


CATEGORY_MAPPING = {
    'зарплата': 'salary',
    'оплата': 'payment',
    'перевод': 'transfer',
    'зачисление': 'deposit',
    'поступление': 'income',
    'списание': 'write-off',
    'покупка': 'purchase',
    'платеж': 'payment',
    'недостаточно средств': 'insufficient funds',
    'автоплатеж': 'autopayment',
}

TRANSACTION_PATTERN = r'{} (\d+[,.]?\d*) ?(₽|руб|р|rub|r)\.?.*'


def parse_text(text: str, category: str) -> dict[str, str | int] | None:
    pattern = TRANSACTION_PATTERN.format(category)
    parsed_text = re.match(pattern, text)
    if not parsed_text:
        return None
    return {"amount": int(parsed_text.groups()[0]),
            "category": category,
            "row_currency": parsed_text.groups()[1]}


def get_currency(currency):
    currency = currency.strip().lower().replace('.', '')
    if currency in ['₽', 'р', 'руб', 'рубль', 'рублей', 'рубля',  'r', 'rub', 'rubles', 'rubl']:
        return 'rub'
    elif currency in ['$', 'доллар', 'доллары', 'долларов', 'usd', 'долл']:
        return 'usd'
    elif currency in ['€', 'евро', 'евр', 'eur', 'euro']:
        return 'eur'
    elif currency in ['₿', 'биткоин', 'btc', 'bitcoin']:
        return 'btc'
    elif currency in ['lari', 'gel', 'гел', 'лари', 'gel', 'ლ', 'ლარი']:
        return 'gel'
    else:
        return None


async def create_transaction(text: str, parsed_text: dict, user: User):
    currency: str = get_currency(parsed_text['row_currency'])
    if not currency:
        currency = user.settings.currency

    async with session() as s:
        Transaction(
            origin_text=text,
            currency=s.query(Currency).filter(Currency.name == currency).first(),
            budget=s.query(Budget).filter(Budget.user == user).first(),
            amount=parsed_text['amount'],
            category=parsed_text['category'],
            user=user
        )


def handle_raw_message(row_text, user):
    lower_text = row_text.lower()

    for key, value in CATEGORY_MAPPING.items():
        if key in lower_text:
            parsed_text = parse_text(row_text, value)
            transaction = create_transaction(row_text, parsed_text, user)
            return transaction

    return {"error": "Can't parse transaction"}
