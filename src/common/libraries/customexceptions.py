from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR

__author__ = ["arunreghunathan"]


class BaseCustomException(Exception):
    """
    Used as the base class for all other exceptions
    Why? So that custom exceptions can be caught at the views
    """

    def _init__(self):
        super(BaseCustomException, self).__init__()
        self.code = 0000
        self.message = "An unknown BaseCustomException occurred"


class EmailExistsExecption(BaseCustomException):
    def __init__(self):
        super(EmailExistsExecption, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = "User with email address already registered"


class PhoneNumberExistsExecption(BaseCustomException):
    def __init__(self):
        super(PhoneNumberExistsExecption, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = "User with phone number already registered"


class UsernameExistException(BaseCustomException):
    def __init__(self):
        super(UsernameExistException, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = "Username is already being used"


class UserNotFound(BaseCustomException):
    def __init__(self, message="User Not Found"):
        super(UserNotFound, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = message


class UserNotCreated(BaseCustomException):
    def __init__(self, message="User Could Not be Created"):
        super(UserNotCreated, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = message


class TokenUserMismatch(BaseCustomException):
    def __init__(self):
        super(TokenUserMismatch, self).__init__()
        self.code = HTTP_401_UNAUTHORIZED
        self.message = "Token does not match user"


class CannotUpdateUserReference(BaseCustomException):
    def __init__(self):
        super(CannotUpdateUserReference, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = "User reference Cannot be Updated"


class EmailRequiredExecption(BaseCustomException):
    def __init__(self):
        super(EmailRequiredExecption, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = "Email is required to create new User"


class UsernameRequiredException(BaseCustomException):
    def __init__(self):
        super(UsernameRequiredException, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = "Username is required to create new User"


class UserIdRequiredExecption(BaseCustomException):
    def __init__(self):
        super(UserIdRequiredExecption, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = "idUser is required"


class UserUnauthenticatedException(BaseCustomException):
    def __init__(self):
        super(UserUnauthenticatedException, self).__init__()
        self.code = HTTP_401_UNAUTHORIZED
        self.message = "User is Unauthenticated"


class PayementCouldNotBeVerified(BaseCustomException):
    def __init__(self):
        super(PayementCouldNotBeVerified, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = "Payment id could not be verified, please check the payment_id or pay again"


class TransactionIdAlreadyPresent(BaseCustomException):
    def __init__(self):
        super(TransactionIdAlreadyPresent, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = "This payment id is already present, please check the payment_id or pay again"


class AmountMismatch(BaseCustomException):
    def __init__(self, message=None):
        super(AmountMismatch, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = message if message else "Please check the amount you have paid"


class BadRequestException(BaseCustomException):
    def __init__(self, message=None):
        super(BadRequestException, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = message if message else "Bad Request. Data could not be stored"


class InvalidDataException(BaseCustomException):
    def __init__(self, message=None):
        super(InvalidDataException, self).__init__()
        self.code = HTTP_400_BAD_REQUEST
        self.message = message if message else "Invalid Data send in request."
