from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST
from app.schemas.user import UserCreate
from app.models.student import Student
from app.services.user import UserService


class StudentService:

    @staticmethod
    def create_student(user_data : UserCreate, class_id : str, db : Session):
        
        try:
            user = UserService.create_user(user_data, db)
        except ValueError as e:
            return JSONResponse(
                status_code=HTTP_400_BAD_REQUEST,
                content={"detail" : str(e)}
            )

        student = Student(id=user.id, class_id=class_id, type="student")
        db.add(student)
        db.commit()
        db.refresh(student)

        return student



