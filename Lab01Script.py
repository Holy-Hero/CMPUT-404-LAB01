"""
This is the source code
"""
# a python script to get the version of the requests library
# also curls the Google homepage
# and prints the source code
import requests


def main():
    print(f"The version of requests library is {requests.__version__}")
    print(requests.get('http://google.com/'))
    print(*open(__file__), sep="")


if __name__ == "__main__":
    main()