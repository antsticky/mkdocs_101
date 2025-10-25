from models import User

def greet(user: User) -> str:
    return f"Hello, {user.name}!"

if __name__ == "__main__":
    user = User(id=1, name="2", email="alice@example.com")
    print(greet(user))


