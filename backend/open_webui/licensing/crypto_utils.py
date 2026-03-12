import base64
import json
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


def load_public_key(path: str):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())


def verify_signature(public_key, license_data: dict, signature_b64: str):
    signature = base64.b64decode(signature_b64)

    data_bytes = json.dumps(license_data, sort_keys=True).encode()

    public_key.verify(
        signature,
        data_bytes,
        padding.PKCS1v15(),
        hashes.SHA256(),
    )