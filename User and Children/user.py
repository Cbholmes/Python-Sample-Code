class User():
    """Object represents a User."""
    def __init__(self, firstname, lastname, username="", dob="", email="", loginattempts = 0):
        """Constructor, creates a user with the given first and last names,
            username (lowercase), date of birth, and email. If username is blank username = firstname.lastname."""
        self._firstname = firstname
        self._lastname = lastname
        self._username = (firstname + "." + lastname).lower() if username == "" else username.lower()
        self._dob=dob
        self._email=email
        self._loginattempts = loginattempts

    def describeUser(self):
        """Prints details of the User."""
        print("User Details:")
        print("\tFirst Name:", self._firstname)
        print("\tLast Name:", self._lastname)
        print("\tUsername:", self._username)
        if self._dob != "": print("\tDate of Birth:", self._dob)
        if self._email != "": print("\tEmail Address:", self._email)

    def greetUser(self):
        """Prints a greeting to the User."""
        print("Hello there", self._firstname + ".")

    def incrLoginAttempts(self):
        """Increments amount of login attempts by 1."""
        self._loginattempts += 1

    def resetLoginAttempts(self):
        """Sets amount of login attempts to 0."""
        self._loginattempts = 0

