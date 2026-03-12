import os
from .license_loader import load_license
from .license_validator import LicenseValidator
from .exceptions import LicenseLimitExceeded


class LicenseService:

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        license_path = os.path.join(base_dir, "..", "config", "license.json")
        public_key_path = os.path.join(base_dir, "licensing", "public_key.pem")

        # DEBUG
        print("LICENSE PATH:", license_path)
        print("PUBLIC KEY PATH:", public_key_path)

        self.license_data = load_license(license_path)

        validator = LicenseValidator(public_key_path)
        validator.validate(self.license_data)

        self.max_users = self.license_data.get("max_users", 0)

    def enforce_user_limit(self, current_users: int):

        if current_users >= self.max_users:
            raise LicenseLimitExceeded(
                f"User limit reached ({self.max_users})"
            )