# a python script to get the version of the requests library
# also curls the Google homepage
import requests


def main():
    print(f"The version of requests library is {requests.__version__}")
    print(requests.get('http://google.com/'))


if __name__ == "__main__":
    main()