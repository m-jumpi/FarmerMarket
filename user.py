from werkzeug.security import generate_password_hash, check_password_hash


class MyUser:
    def __init__(self, email, username, password):
        self.email = email
        self.usernamne = username
        self.password_hash = generate_password_hash(password)

        # def password(self):
        #     raise AttributeError('password is not a readable attribute')
        #
        # def password(self, password):
        #     self.password_hash = generate_password_hash(password)

        def verify_password(self, password):
            return check_password_hash(self.password_hash, password)
