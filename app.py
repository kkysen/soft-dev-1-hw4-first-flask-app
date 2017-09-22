#!/usr/bin/python

"""
Khyber Sen
SoftDev1 pd7
HW2 -- NO-body expects the Spanish Inquisition!
2017-09-13
"""

__author__ = 'Khyber Sen'
__date__ = '2017-09-22'

from flask import Flask
from flask import request
from urllib2 import urlopen

app = Flask(__name__)


@app.route('/hello')
def hello():
    # type: () -> str
    print('hello')
    return 'Hello, World!'


def reflect_url(url):
    # type: () -> str
    try:
        http_request = urlopen(url)
    except ValueError:
        return 'bad url: ' + url
    result = http_request.read()  # type: str
    http_request.close()
    return result


@app.route('/reflect')
def reflect():
    # type: () -> str
    url = request.query_string  # type: str
    return reflect_url(url)


@app.route('/')
def index():
    return reflect_url('http://www.stuycs.org/courses/software-development/mykolyk-1')


def generate_route(i):
    # type: (int) -> None
    i = str(i)

    def route():
        return i
    route.__name__ += i

    app.route('/' + i)(route)


def generate_routes(start, stop):
    # type: () -> None
    for i in xrange(start, stop):
        generate_route(i)


if __name__ == '__main__':
    generate_routes(0, 10000)
    app.debug = True
    app.run()
