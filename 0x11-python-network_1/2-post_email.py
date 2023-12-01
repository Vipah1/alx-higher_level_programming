#!/usr/bin/python3
"""
POST request to the passed Url with the email as parameter
"""
import urllib.request
from sys import argv

def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = urllibe.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = request.read()
        print(result.decode('utf8'))

if __name__ as "__main__":
    main(argv)
