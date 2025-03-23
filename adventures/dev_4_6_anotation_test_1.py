import asyncio
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class UserCreateRequest:
    username: str
    email: str
    full_name: str
    age: int
    roles: List[str] = None
    is_active: bool = True

async def create_user(user: UserCreateRequest):
    # For this example, let's just print the user info and return a mock result
    print(f"Creating user: {user.username}, {user.email}")
    # In a real application, this would interact with a database
    return {"id": "user_123", "username": user.username, "email": user.email}

# Example of how to call the function
async def main():
    # Create a UserCreateRequest instance
    new_user_request = UserCreateRequest(
        username="johndoe",
        email="john.doe@example.com",
        full_name="John Doe",
        age=30,
        roles=["user", "editor"]
    )
    
    # Call the create_user function
    try:
        created_user = await create_user(new_user_request)
        print(f"User created successfully! User ID: {created_user['id']}")
    except Exception as e:
        print(f"Error creating user: {str(e)}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
