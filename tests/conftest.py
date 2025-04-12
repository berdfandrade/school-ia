import pytest
import _pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config.database import Base

@pytest.fixture(scope="session")
def postgres_container():
    """Cria um contêiner PostgreSQL para testes."""
    with PostgresContainer("postgres:latest") as postgres:
        yield postgres


@pytest.fixture(scope="function")
def db(postgres_container):
    """Cria uma conexão temporária com o banco PostgreSQL de testes."""
    engine = create_engine(postgres_container.get_connection_url())
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)
