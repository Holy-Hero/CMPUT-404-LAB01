# a python script to get the version of the requests library
import requests


def main():
    print(f"The version of requests library is {requests.__version__}")


if __name__ == "__main__":
    main()