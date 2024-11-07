import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    date_of_birth: dict[str, int]
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str
