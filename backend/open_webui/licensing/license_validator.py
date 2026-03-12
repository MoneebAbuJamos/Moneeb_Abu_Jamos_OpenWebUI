from datetime import datetime
from .crypto_utils import verify_signature, load_public_key
from .exceptions import LicenseInvalidError, LicenseExpiredError


class LicenseValidator:

    def __init__(self, public_key_path):
        self.public_key = load_public_key(public_key_path)

    def validate(self, license_data):

        if "signature" not in license_data:
            raise LicenseInvalidError("Missing signature")

        signature = license_data["signature"]

        data = license_data.copy()
        del data["signature"]

        try:
            verify_signature(self.public_key, data, signature)
        except Exception:
            raise LicenseInvalidError("Invalid signature")

        if "expires_at" in license_data:
            exp = datetime.fromisoformat(license_data["expires_at"])
            if datetime.utcnow() > exp:
                raise LicenseExpiredError("License expired")

        return True