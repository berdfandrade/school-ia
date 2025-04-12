import pytest
import logging
from sqlalchemy.exc import OperationalError
from sqlalchemy import text, create_engine
from app.config.database import DATABASE_URL

class TestDatabaseConnection:
    def test_real_database_connection(self):

        engine = create_engine(DATABASE_URL)
        connection = engine.connect()

        try:
            result = connection.execute(text("SELECT 1")).scalar()
            assert result == 1
        except OperationalError as e:
            pytest.fail(f"Erro ao conectar ao banco real: {e}")
        finally:
            connection.close()

    def test_container_database_connection(self, db):
        try:
            result = db.execute(text("SELECT 1")).scalar()
            assert result == 1, "Deve retornar a conexão"
        finally:
            db.close()

