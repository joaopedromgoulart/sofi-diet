from app.controller.data_source.users import UsersService


class Controler:
    def __init__(self, users_data: UsersService) -> None:
        self._users_data = users_data

    def 