class User:
    '''Class represents operations related to products'''
    all_users = {}

    def __init__(self, email, username, password):
        self.id = len(User.all_users) + 1
        self.email = email
        self.username = username
        self.password = password


    def signup(self):
        payload = dict(
            email = self.email,
            id = self.id,
            username = self.username,
            password = self.password
            )

        self.all_users.update({self.username:payload})

    @classmethod
    def get_one(cls, username):
        for key in User.all_users:
            if key == username:
                return User.all_users[key]
                
    @classmethod
    def get_all(self):
        return {u['username']: u for u in User.all_users.values()}