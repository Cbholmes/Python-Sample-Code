class User():
    """Object represents a User."""
    def __init__(self, firstname, lastname, username="", dob="", email=""):
        """Constructor, creates a user with the given first and last names,
            username (lowercase), date of birth, and email. If username is blank username = firstname.lastname."""
        self._firstname = firstname
        self._lastname = lastname
        self._username = (firstname + "." + lastname).lower() if username == "" else username.lower()
        self._dob=dob
        self._email=email
    def describeUser(self):
        """Prints details of the User."""
        print("User Details:")
        print("\tFirst Name:", self._firstname)
        print("\tLast Name:", self._lastname)
        print("\tUsername:", self._username)
        print("\tDate of Birth:", self._dob)
        print("\tEmail Address:", self._email)
    def greetUser(self):
        """Prints a greeting to the User."""
        print("Hello there", self._firstname + ".")
