
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST
from app.schemas.user import UserCreate
from app.models.user import User
from app.security.hashing import HashService
from app.security.password import Password

class UserService:
    @staticmethod
    def create_user(user_data : UserCreate, database : Session):

        email_exists = database.query(User.email == user_data.email).first()

        if email_exists:
            return JSONResponse(
                status_code=HTTP_400_BAD_REQUEST,
                content={
                    "detail": "Email already registered"
                }
            )

        try:
            Password.validate(user_data.password)
        except ValueError as e:
            return JSONResponse(
                status_code=HTTP_400_BAD_REQUEST,
                content={
                    "detail" : f"{e}"
                }
            )

        hashed_pwd = HashService.hash_password(user_data.password)

        new_user = User(
            name=user_data.name,
            email=user_data.email,
            hashed_password=hashed_pwd,
            type = user_data.type
        )

        database.add(new_user)
        database.commit()
        database.refresh(new_user)





