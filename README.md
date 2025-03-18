# Authentication Decorator 🔒

## Overview  
This project implements an **authentication decorator** in Python to control access to functions based on user roles. The decorator ensures that only authorized users can execute certain functions while restricting access for others.  

## Features  
- Role-based access control using an **Enum** (`Admin`, `Member`, `Guest`)  
- Restricts unauthorized users from executing protected functions  
- Raises an exception for invalid roles  
- Demonstrates authentication logic with example functions  

## Installation  
No external dependencies are required. Ensure you have **Python 3.x** installed.  

## Usage  
### 1. Define User Roles  
Roles are defined using an **Enum** to enforce predefined user access levels:  

```python
import enum

class UserRoles(enum.Enum):
    Admin = "admin"
    Member = "member"
    Guest = "guest"
```

### 2. Implement the Authentication Decorator  
The `authentication` decorator checks the user's role before allowing access to the function:  

```python
def authentication(user_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_role == UserRoles.Admin:
                return func(*args, **kwargs)
            elif user_role == UserRoles.Member:
                return "Access Denied: You are a Member."
            elif user_role == UserRoles.Guest:
                return "Access Denied: You are a Guest."
            else:
                raise PermissionError("Invalid Role!")
        return wrapper
    return decorator
```

### 3. Apply the Decorator to Functions  
Example functions that require authentication:  

```python
@authentication(UserRoles.Admin)
def delete_user(user_id):
    return f"User {user_id} has been successfully deleted."

@authentication(UserRoles.Member)
def view_profile():
    return "Displaying user profile."
```

## Running Tests  
To test the authentication logic, use **pytest**.  

### Test Script  
Create a test file `test_authentication.py`:  

```python
import pytest
from authentication_decorator import authentication, UserRoles

@authentication(UserRoles.Admin)
def admin_task():
    return "Admin task executed."

@authentication(UserRoles.Member)
def member_task():
    return "Member task executed."

@authentication(UserRoles.Guest)
def guest_task():
    return "Guest task executed."

def test_admin_access():
    assert admin_task() == "Admin task executed."

def test_member_access():
    assert member_task() == "Access Denied: You are a Member."

def test_guest_access():
    assert guest_task() == "Access Denied: You are a Guest."

def test_invalid_role():
    with pytest.raises(PermissionError, match="Invalid Role!"):
        @authentication("unknown_role")
        def invalid_task():
            pass
        invalid_task()
```

Run tests using:  
```bash
pytest test_authentication.py
```

## License  
This project is licensed under the **MIT License**.  

## Contributing  
Feel free to open issues or submit pull requests! 🎉  

---

### 🚀 Stay Secure & Control Access with Python!  
```

This README provides **clear explanations, usage examples, and a test section**. Let me know if you need any modifications! 🚀
