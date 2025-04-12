import pytest
from app.security.password import Password, PasswordPolicy


class TestPassword:
    """Password Validator"""
    def test_valid_password_default_policy(self):
        password = "MySecure123!"
        assert Password.validate(password) == password

    # Tamanho mínimo
    def test_password_too_short(self):
        with pytest.raises(ValueError, match="at least 8 characters"):
            Password.validate("Ab1!")

    # Tamanho máximo
    def test_password_too_long(self):
        long_password = "A1!" + "a" * 100
        with pytest.raises(ValueError, match="at most 64 characters"):
            Password.validate(long_password)

    # Falta letra maiúscula
    def test_password_missing_uppercase(self):
        with pytest.raises(ValueError, match="one uppercase"):
            Password.validate("secure123!")

    # Falta número
    def test_password_missing_number(self):
        with pytest.raises(ValueError, match="one number"):
            Password.validate("SecureOnly!")

    # Falta caractere especial
    def test_password_missing_special(self):
        with pytest.raises(ValueError, match="one special character"):
            Password.validate("Secure123")

    # Teste com política customizada (sem número e sem especial)
    def test_password_with_custom_policy(self):
        policy = PasswordPolicy(require_number=False, require_special=False)
        password = "SecurePassword"
        assert Password.validate(password, policy) == password
