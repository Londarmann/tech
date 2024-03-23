import subprocess
import sys

from test_data import  test_data
def install_packages():
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)


def make_migrations():
    try:
        subprocess.run(["python", "manage.py", "makemigrations"], check=True)
        subprocess.run(["python", "manage.py", "migrate"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error making migrations: {e}")
        sys.exit(1)


if __name__ == "__main__":
    install_packages()
    make_migrations()
    test_data()