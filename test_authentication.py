import pytest
from Authentication_Decorator import authentication, UserRoles, delete_user, view_profile

def test_admin_access():
    assert delete_user(123) == "User 123 was successfully deleted."

def test_member_access():
    assert view_profile() == "You don't have permission. You are a member."

def test_guest_access():    
    @authentication(UserRoles.Guest)
    def restricted_action():
        return "This should not execute"   
    assert restricted_action() == "You don't have permission. You are a guest."

def test_invalid_role():    
    with pytest.raises(PermissionError, match="Error: Invalid role"):
        @authentication("invalid_role")
        def some_function():
            return "Should not execute"
        
        some_function()

if __name__ == "__main__":
    pytest.main()
