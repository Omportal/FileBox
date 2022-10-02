import email
from sqlite3 import IntegrityError
from django.contrib.auth.hashers import check_password
from .repository import Repository
from apps.auth_app.dto import RawAuthDTO, LoginDTO
from apps.user_app.models import CustomUser
from utils.exceptions import UserAlreadyRegistered, UserNotFoundError


class AuthAppRepository(Repository):

    @staticmethod
    def register_user(auth_dto: RawAuthDTO) -> CustomUser:
        user = CustomUser.objects.filter(email=auth_dto.email).last()
        if user:
            raise UserAlreadyRegistered
        if not user:
            user = CustomUser.objects.create_user(email=auth_dto.email, second_name=auth_dto.second_name,
                                                  first_name=auth_dto.first_name, password=auth_dto.password)
            return user

    @staticmethod
    def get_user_by_email_password(dto: LoginDTO) -> CustomUser:
        try:
            user = CustomUser.objects.get(
                email=dto.email)
        except IntegrityError:
            raise UserNotFoundError
        return user
