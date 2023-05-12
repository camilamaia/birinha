import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    print(f"Hello {my_input}")


if __name__ == "__main__":
    main()
