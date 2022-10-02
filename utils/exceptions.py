import datetime
from typing import Optional


class CustomValidationError(Exception):
    error: str = None
    detail: str = None
    status_code: int = 400
    obj: Optional[dict] = None
    data: dict = {}

    def __init__(self, detail: str = None, obj: Optional[dict] = None):
        if detail:
            self.detail = detail

        self.data.update({
            'error': self.error,
            'detail': self.detail,
        })

        if obj:
            self.obj = obj
            self.data.update(object=self.obj)

        super(CustomValidationError, self).__init__(self.data)


class UserAlreadyRegistered(CustomValidationError):
    error: str = "USER_ALREADY_REGISTERED"
    detail: str = 'Пользователь с таким номером телефона уже зарегистрирован в системе'


class UserNotFoundError(CustomValidationError):
    error: str = "USER_NOT_FOUND"
    detail: str = 'Пользователь не найден'


class InvalidPassword(CustomValidationError):
    error: str = "INVALID_PASSWORD"
    detail: str = 'Проверьте пароль'


# class UserDeactivatedError(CustomValidationError):
#     error: str = app_errors.USER_IS_DEACTIVATED
#     detail: str = 'Пользователь деактивирован'
#     status_code: int = HTTP_401_UNAUTHORIZED


# class DeactivatedSessionError(CustomValidationError):
#     error: str = app_errors.SESSION_IS_DEACTIVATED
#     detail: str = 'Сессия деактивирована'
#     status_code: int = HTTP_401_UNAUTHORIZED


# class SessionNotFoundError(CustomValidationError):
#     error: str = app_errors.SESSION_NOT_FOUND
#     detail: str = 'Сессия не найдена'
#     status_code: int = HTTP_401_UNAUTHORIZED


# class RefreshTokenNotValidError(CustomValidationError):
#     error: str = app_errors.REFRESH_TOKEN_NOT_VALID
#     detail: str = 'Refresh token не валидный'
#     status_code: int = HTTP_400_BAD_REQUEST


# class BlockedSessionError(CustomValidationError):
#     error: str = app_errors.SESSION_IS_BLOCKED
#     detail: str = 'Сессия заблокирована'
#     status_code: int = HTTP_401_UNAUTHORIZED

#     def __init__(self,  unlock_dt: datetime, detail: str = None, obj: Optional[dict] = None):
#         self.unlock_dt = unlock_dt
#         self.data.update(unlock_dt=self.unlock_dt)
#         super().__init__(detail, obj)


# class InvalidDecodingToken(AuthenticationFailed):
#     default_detail: str = 'Не удалось корректно декодировать токен пользователя'


# class InputValueError(CustomValidationError):
#     error: str = app_errors.INPUT_VALUE_ERROR
#     status_code: int = HTTP_400_BAD_REQUEST
