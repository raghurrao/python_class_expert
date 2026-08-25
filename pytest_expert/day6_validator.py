# Day 6: DataValidator Library to Test

class DataValidator:
    @staticmethod
    def validate_username(username):
        """Validates username: alphanumeric, 3 to 20 chars."""
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        if len(username) < 3 or len(username) > 20:
            raise ValueError("Username must be between 3 and 20 characters")
        if not username.isalnum():
            raise ValueError("Username must be alphanumeric")
        return True

    @staticmethod
    def validate_email(email):
        """Validates email: contains '@' and '.'."""
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        return True

    @staticmethod
    def validate_password(password):
        """Validates password: >= 8 chars, 1 uppercase, 1 lowercase, 1 digit."""
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isupper() for c in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in password):
            raise ValueError("Password must contain at least one number")
        return True
