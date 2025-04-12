import pytest
from sqlalchemy.orm import Session
from app.services.user import UserService
from app.schemas.user import UserCreate
from app.models.user import UserType, User

@pytest.fixture
def user_data():
    user_data = UserCreate(
        name="João Silva",
        email="joao@example.com",
        password="SenhaSegura123!",
        type=UserType.student
    )
    return user_data

class TestUserService:
    """UserService"""
    def test_create_user_success(self, db: Session, user_data):

        UserService.create_user(user_data, db)

        created_user = db.query(User).filter(User.email == user_data.email).first()
        assert created_user is not None
        assert created_user.name == user_data.name
        assert created_user.email == user_data.email
        assert created_user.type == user_data.type

    def test_create_user_duplicate_email(self, db: Session, user_data):

        UserService.create_user(user_data, db)
        response = UserService.create_user(user_data, db)

        # Assert
        assert response.status_code == 400
        assert response.body is not None
        assert b"Email already registered" in response.body

    def test_create_user_invalid_password(self, db: Session):

        user_data = UserCreate(
            name="João Silva",
            email="joao@example.com",
            password="123456789",
            type=UserType.student
        )

        response = UserService.create_user(user_data, db)

        assert response.status_code == 400