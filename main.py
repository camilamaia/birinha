import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]
    event_name = os.environ["GITHUB_EVENT_NAME"]


    print(f"Hello {my_input}")

    # if event_name == "issue_comment" and :

    print(f"nome do evento: {event_name}")
    print(os.environ)


if __name__ == "__main__":
    main()
