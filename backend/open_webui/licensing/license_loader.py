import json
import os
from .exceptions import LicenseNotFoundError


def load_license(path: str):
    if not os.path.exists(path):
        raise LicenseNotFoundError("License file not found")

    with open(path, "r") as f:
        return json.load(f)