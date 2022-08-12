from database import data

class User:
    all_users = []

    def __init__(self, data:dict):
        self.f_name = data.get('f_name')
        self.l_name = data.get('l_name')
        self.is_staff = data.get('is_staff')
        self.all_users.append(self)

    def __repr__(self) -> str:
        return f'This is the {self.f_name} {self.l_name} object'

    @classmethod
    def count_staff(cls) -> int:
        staff_users = []
        for user in cls.all_users:
            if user.is_staff:
                staff_users.append(user)
        return len(staff_users)
        # return len([user for user in cls.all_users if user.is_staff])

for user in data:
    User(user)

# print(User.all_users[0])
print(User.count_staff())