class AuthSystem:
    # Hash Counter for Permission's
    Hash = 3

    # Default Permission's
    PERMISSION_TYPES = {1: "READ",
                        2: "WRITE",
                        3: "DELETE"}

    # User And There Permission's Mapping
    USER_PERMISSION_MAPPING = {}

    # All Existing User
    ALL_USERS = []

    # Initial User
    CURRENT_USER = "ADMIN"

    def __init__(self):
        self.ALL_USERS = ["ADMIN"]
        self.USER_PERMISSION_MAPPING["ADMIN"] = [1, 2, 3]

    def add_new_user(self):
        permission = self.USER_PERMISSION_MAPPING.get(self.CURRENT_USER)
        if permission and 3 in permission:
            a = input("Enter the New user Name: ")
            self.ALL_USERS.append(a)
            self.USER_PERMISSION_MAPPING[a] = []
            print("These are the Permission that you can add for this User")
            self.all_user_permissions()
            lst = list(map(int, input("Enter comma separated Permissions Example:- 1,2,3: ").split(",")))
            for i in lst:
                self.USER_PERMISSION_MAPPING[a].append(i)
        else:
            print("You Don't Have Add New User Permission")

    def all_user_permissions(self):
        for key, value in self.PERMISSION_TYPES.items():
            print(f"Key:- {key}  Permission Name:- {value}")

    def check_all_users_information(self):
        for user in self.ALL_USERS:
            print(f"User Name:- {user}")
            user_permissions = self.USER_PERMISSION_MAPPING.get(user)
            if user_permissions:
                print("User Have these permissions:- ")
                for user_permission in user_permissions:
                    print(f"{self.PERMISSION_TYPES.get(user_permission)}")

    def re_login(self, old_user):
        new_user = input("Enter The User Name For Which you want to Login:- ")
        if new_user in self.ALL_USERS:
            self.CURRENT_USER = new_user
            print(f"You have been logged out as {old_user} and Successfully Logged in as {self.CURRENT_USER}")
        else:
            print("This User Doesn't Exists in our System")

    def add_new_permission(self):
        permission = self.USER_PERMISSION_MAPPING.get(self.CURRENT_USER)
        if permission and 3 in permission:
            a = input("Enter The new Permission Name:- ")
            self.Hash += 1
            self.PERMISSION_TYPES[self.Hash] = a
            print("New Permission Added Successfully")
        else:
            print("You Don't Have Write Permission")

    def delete_user_permission(self):
        all_permission = self.USER_PERMISSION_MAPPING.get(self.CURRENT_USER)
        permission_id = int(input("Enter the key which permission you want to delete for Current User:- "))
        if all_permission.get(permission_id):
            all_permission.pop(permission_id)
            print("Permission successfully Deleted")
        else:
            print("This Permission Doesn't Exists for current User")


obj = AuthSystem()
choice = 1
print("hi! you are logged in as admin")
while choice != 0:
    print("Please Choose Any of the below Action")
    print("0. Exit")
    print("1. Login as another user")
    print("2. Create New user")
    print("3. Add New Master Permission")
    print("3. Edit Current User Permissions")
    print("5. Check all User's Information")
    choice = int(input("Enter choice: "))
    if choice == 1:
        obj.re_login(obj.CURRENT_USER)
    elif choice == 2:
        obj.add_new_user()
    elif choice == 3:
        obj.add_new_permission()
    elif choice == 4:
        obj.delete_user_permission()
    elif choice == 5:
        obj.check_all_users_information()
