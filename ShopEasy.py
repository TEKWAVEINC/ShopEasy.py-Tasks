class UserProfile:
    def __init__(self, username, email, full_name, bio='', profile_picture=None):
        self.username = username
        self.email = email
        self.full_name = full_name
        self.bio = bio
        self.profile_picture = profile_picture

    def update_profile(self, bio=None, profile_picture=None):
        if bio:
            self.bio = bio
        if profile_picture:
            self.profile_picture = profile_picture

    def __str__(self):
        return (f"Username: {self.username}\nEmail: {self.email}\nFull Name: {self.full_name}\nBio:"
                f"{self.bio}\nProfile Picture: {self.profile_picture}")


class UserAuthentication:
    def __init__(self):
        self.users = {}

    def register_user(self, username, email, password):
        if username in self.users:
            return "Username already exists. Please choose another."
        self.users[username] = {'email': email, 'password': password}
        return "Registration successful."

    def login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return True
        return False
