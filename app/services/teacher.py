from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST
from app.schemas.user import UserCreate
from app.models.teacher import Teacher
from app.services.user import UserService


class TeacherService:

    @staticmethod
    def create_teacher(user_data : UserCreate, subject_id : str, db : Session):

        try:
            user = UserService.create_user(user_data, db)
        except ValueError as e:
            return JSONResponse(
                status_code=HTTP_400_BAD_REQUEST,
                content={"detail" : str(e)}
            )

        teacher = Teacher(id=user.id, subject=subject_id, type="teacher")
        db.add(teacher)
        db.commit()
        db.refresh(teacher)

        return teacher



