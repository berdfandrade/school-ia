from dataclasses import dataclass

@dataclass
class PasswordPolicy:
    min_len: int = 8
    max_len: int = 64
    require_uppercase: bool = True
    require_number: bool = True
    require_special: bool = True


class Password:
    @staticmethod
    def validate(password: str, policy: PasswordPolicy = PasswordPolicy()) -> str:
        if len(password) < policy.min_len:
            raise ValueError(f"Password must be at least {policy.min_len} characters long.")
        if len(password) > policy.max_len:
            raise ValueError(f"Password must be at most {policy.max_len} characters long.")

        if policy.require_uppercase and not any(c.isupper() for c in password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if policy.require_number and not any(c.isdigit() for c in password):
            raise ValueError("Password must contain at least one number.")
        if policy.require_special and not any(c in "!@#$%^&*()-_=+[]{}|;:',.<>/?`~" for c in password):
            raise ValueError("Password must contain at least one special character.")

        return password

