import pytest
from app.schemas.user import UserCreate
from app.services.teacher import TeacherService
from app.models.user import UserType

@pytest.fixture
def user_data():
    user_data = UserCreate(
        name="John Doe",
        email="johndoe@example.com",
        password="SecurePass1!",
        type=UserType.teacher
    )
    return user_data

class TestTeacherService:
    def test_create_teacher_success(self, db, user_data):

        subject_id = "89574125665"

        teacher = TeacherService.create_teacher(
            user_data=user_data,
            subject_id=subject_id,
            db=db
        )

        assert teacher is not None
        assert teacher.id is not None
        assert teacher.subject == subject_id
        assert teacher.type == UserType.teacher

        # Confirma que o user também foi criado
        from app.models.user import User
        user_in_db = db.query(User).filter(User.id == teacher.id).first()
        assert user_in_db is not None
        assert user_in_db.email == user_data.email

    def test_create_teacher_with_existing_email(self, db, user_data):

        TeacherService.create_teacher(
            user_data=user_data,
            subject_id="physics",
            db=db
        )

        response = TeacherService.create_teacher(
            user_data=user_data,
            subject_id="chemistry",
            db=db
        )

        assert isinstance(response, dict) or response.status_code == 400
        if hasattr(response, "status_code"):
            assert response.status_code == 400
            assert "detail" in response.body.decode()

