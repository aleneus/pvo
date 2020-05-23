"""Security system."""


class User:
    """Data for user."""
    def __init__(self, login, passwd):
        self.login = login
        self.passwd = passwd

    def equals(self, user):
        """Check if user equals to given."""
        if self.login != user.login:
            return False

        if self.passwd != user.passwd:
            return False

        return True


class Passwd:
    """Maintainer for user records."""
    def __init__(self, name, driver=None):
        self.driver = driver
        self.users = []
        self._read(name)

    def add_user(self, login, passwd):
        """Add new user."""
        if self.user_exists(login):
            raise RuntimeError("User exists")

        self.users.append(User(login, passwd))

    def commit(self):
        """Save data."""
        text = ""
        for user in self.users:
            text = text + "{};{}\n".format(user.login, user.passwd)
        self.driver.write(text)

    def user_exists(self, login):
        """Check if user exists."""
        for user in self.users:
            if user.login == login:
                return True

        return False

    def check_user(self, login, passwd):
        """Check login and password."""
        for user in self.users:
            if user.equals(User(login, passwd)):
                return True

        return False

    def remove_user(self, login, passwd):
        """Remove existing user."""
        tmp = []

        if not self.user_exists(login):
            raise RuntimeError("No such user")

        if not self.check_user(login, passwd):
            raise RuntimeError("Wrong password")

        for user in self.users:
            if user.equals(User(login, passwd)):
                continue
            tmp.append(user)

        self.users = tmp

    def _read(self, name):
        content = self.driver.read(name)
        if not content:
            return

        if ";" not in content:
            raise RuntimeError("Wrong file structure")

        self.users = []
        lines = content.split("\n")
        if lines:
            for line in lines[:-1]:
                pair = line.split(";")
                self.users.append(User(*pair))


class DataDriver:
    """Reader and writer."""
    def __init__(self, name):
        pass

    def read(self):
        """Read file."""
        raise NotImplementedError

    def write(self, text):
        """Write file"""
        raise NotImplementedError
