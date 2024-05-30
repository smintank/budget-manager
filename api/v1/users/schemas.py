from pydantic import BaseModel


class SUser(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_staff: bool

    model_config = {
        "from_attributes": True
    }


class SRegisterUser(BaseModel):
    username: str
    email: str
    password: str
    first_name: str | None = None
    last_name: str | None = None

    model_config = {
        "from_attributes": True
    }


class SToken(BaseModel):
    token: str
    expires: str
    user_id: int

    model_config = {
        "from_attributes": True
    }


class SSettings(BaseModel):
    language: str
    currency: str

    model_config = {
        "from_attributes": True
    }
