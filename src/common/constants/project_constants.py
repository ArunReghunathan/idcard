AUTHORIZATOIN_FAILED = {
    "status": "Failed",
    "error": {
        "message": "User authentication failed",
        "code": 400,
        "error_type": "Authorization failed"
    }
}

SESSION_EXPIRED = {
    "status": "Failed",
    "error": {
        "message": "Session has expired.",
        "code": 400,
        "error_type": "Session Expired"
    }
}


PERMISSION_DENIED = {
    "status": "Failed",
    "error": {
        "message": "Permission denied",
        "code": 400,
        "error_type": "Permission denied"
    }
}