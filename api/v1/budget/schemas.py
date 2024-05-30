from pydantic import BaseModel


class SCategory(BaseModel):
    title: str
    description: str
    slug: str

    model_config = {
        "from_attributes": True
    }


class SBudget(BaseModel):
    name: str
    current_amount: int
    description: str

    model_config = {
        "from_attributes": True
    }


class SCurrency(BaseModel):
    name: str
    symbol: str
    description: str

    model_config = {
        "from_attributes": True
    }


class SRawTransaction(BaseModel):
    sms_text: str

    model_config = {
        "from_attributes": True
    }
