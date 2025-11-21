import hashlib
import secrets


class Security:

    @staticmethod
    def hash_password(password):
        cryptography = secrets.token_hex(16)
        return f"{cryptography}${hashlib.sha256((password + cryptography).encode()).hexdigest()}"

    @staticmethod
    def verify_password(password, password_hashed):
        cryptography, stored_hash = password_hashed.split("$")
        computed_hashed = hashlib.sha256((password + cryptography).encode()).hexdigest()
        return secrets.compare_digest(computed_hashed, stored_hash)
