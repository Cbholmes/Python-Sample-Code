from user import User
class Admin(User):
    """Represents an Admin as a child of User"""
    def __init__(self, firstname, lastname, privileges, username="",
                 dob="", email="", loginattempts=0):
        """Constructor, creates an admin with given user arguments and privileges"""
        super().__init__(firstname, lastname, username, dob, email, loginattempts)
        self._privileges = Privileges(privileges)

class Privileges():
    """Represents Privleges an admin has"""
    def __init__(self, privileges):
        self._privileges = privileges
        
    def showPrivileges(self):
        print("Current privileges:")
        for privilege in self._privileges:
            print(privilege)
    

details = {"firstname":"John","lastname":"Doe",
           "privileges":["R Users\\*", "RW AdminDocs", "RWX AdminTools"],
           "dob":"January 1st, 2000"}
adminuser = Admin(**details)
adminuser._privileges.showPrivileges()
