"""
This is the source code
"""
# a python script to get the version of the requests library
# also curls the Google homepage
# and prints the source code
import requests


def main():
    print(f"The version of requests library is {requests.__version__}")
    print(requests.get("http://google.com/"))

    file = requests.get("https://raw.githubusercontent.com/Holy-Hero/CMPUT-404-LAB01/main/Lab01Script.py")
    print(file.text)


if __name__ == "__main__":
    main()