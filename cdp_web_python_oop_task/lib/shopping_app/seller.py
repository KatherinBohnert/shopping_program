from user import User
from ownable import set_owner

class Seller(User):
    def __init__(self, name):
        super().__init__(name)
