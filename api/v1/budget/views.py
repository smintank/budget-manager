from api.v1.budget.utils import handle_raw_message
from api.v1.budget.schemas import SRawTransaction
from fastapi import APIRouter

from api.v1.users.models import Token
from core.loggers import logger
from core.settings import LOG_TEMPLATE
from core.database import Session


router = APIRouter(prefix='/api/v1/budget')


@router.post('/{token}/raw/', status_code=201)
async def create_transaction_raw(token: str, raw_transaction: SRawTransaction):
    async with Session() as session:
        user = session.query(Token).filter(Token.token == token).user
    logger.info(LOG_TEMPLATE.format(raw_transaction))
    handle_raw_message(raw_transaction, user)

    return raw_transaction


@router.post('/transactions/', status_code=201)
async def create_transaction():
    pass


@router.get('/transactions/{transaction_id}/')
async def get_transaction(transaction_id: int):
    pass


@router.get('/transactions/', status_code=200)
async def get_all_transactions():
    pass
