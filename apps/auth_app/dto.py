from dataclasses import dataclass


@dataclass(frozen=True)
class RawAuthDTO:
    email: str
    first_name: str
    password: str
    second_name: str = None


@dataclass(frozen=True)
class LoginDTO:
    email: str
    password: str
