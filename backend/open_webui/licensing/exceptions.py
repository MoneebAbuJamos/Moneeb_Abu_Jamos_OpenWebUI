class LicenseError(Exception):
    """Base license error"""
    pass


class LicenseNotFoundError(LicenseError):
    """License file missing"""
    pass


class LicenseInvalidError(LicenseError):
    """Signature verification failed"""
    pass


class LicenseExpiredError(LicenseError):
    """License expired"""
    pass


class LicenseLimitExceeded(LicenseError):
    """User limit reached"""
    pass