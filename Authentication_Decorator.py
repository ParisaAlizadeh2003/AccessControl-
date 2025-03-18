import enum

class UserRoles(enum.Enum):
    Admin = "admin"
    Guest = "guest"
    Member = "member"

def authentication(user_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_role == UserRoles.Admin:
                return func(*args, **kwargs)
            elif user_role == UserRoles.Member:
                return "You don't have permission. You are a member."
            elif user_role == UserRoles.Guest:
                return "You don't have permission. You are a guest."
            else:
                raise PermissionError("Error: Invalid role")
        return wrapper
    return decorator 

@authentication(UserRoles.Admin)
def delete_user(user_id):
    return f"User {user_id} was successfully deleted."

@authentication(UserRoles.Member)
def view_profile():
    return "Displaying user profile."

print(delete_user(123))  
print(view_profile())    
