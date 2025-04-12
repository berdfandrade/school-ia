from app.security.hashing import HashService

def test_hash_and_verify_password():
    password = "MySecurePassword123!"
    hashed = HashService.hash_password(password)

    assert isinstance(hashed, str)
    assert hashed != password
    assert HashService.verify_password(password, hashed) is True

def test_wrong_password_fails_verification():
    password = "RightPassword123!"
    wrong_password = "WrongPassword123!"
    hashed = HashService.hash_password(password)

    assert HashService.verify_password(wrong_password, hashed) is False
