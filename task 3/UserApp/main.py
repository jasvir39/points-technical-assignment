import argparse
from user import User


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-name', action='store', type=str, help='User name', required=True)
    parser.add_argument('-age', action='store', type=int, help="User's age", required=True)
    user_info = parser.parse_args()
    user = User(user_info.name, user_info.age)
    user.print_message()
