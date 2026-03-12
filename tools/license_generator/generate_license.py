import json
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization


with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

license_data = {
    "license_id": "LIC-2026-001",
    "issued_to": "Demo Company",
    "max_users": 3,
    "expires_at": "2027-01-01"
}

data_bytes = json.dumps(license_data, sort_keys=True).encode()

signature = private_key.sign(
    data_bytes,
    padding.PKCS1v15(),
    hashes.SHA256()
)

license_data["signature"] = base64.b64encode(signature).decode()

with open("license.json", "w") as f:
    json.dump(license_data, f, indent=4)

print("License generated successfully")