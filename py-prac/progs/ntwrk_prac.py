# %% [markdown]
# # Network prac

""" http method retrieves existing resources

Returns:
    data_to_decode => object: returns an HTTP res with an HTTP \
status code

API, HTTP

HTTP Method:
  Allows REST api client to manage state of response in web services

1. GET - retrieve existing resource
2. POST - create new sresponse
3. PUT - update existing response
4. PATCH - partial update
5. DELETE - delete response

- after the RESTAPI recieves HTTP req it returns an HTTP res with an HTTP \
status code
- The app that sent the req to the API will perform actions based on the
results (also include error handling & success messages)
    - 2xx - success; 3xx - redirect; 4xx - client error; 5xx - server error
- Endpoints: the URLS the RESTAPI exposes that the Client App can use to \
access a web servers resources
"""

# %%

import urllib.error
import urllib.parse
import time
import socket
import urllib.request
import urllib.request as areq
import socket as sk
import requests
# import urllib.request


# %%
# https://www.datamuse.com/api/ API prac site
new_ur = requests.get("https://api.datamuse.com/words?")

# %%

""" _summary_

Returns:
    _type_: _description_
"""

sock1 = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
sock1.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
sock1.send(cmd)

while True:
    data = sock1.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

sock1.close()

# %% [markdown]
"""
network protocol HTTP

socket: make network connections and retrieve data over them

socket connection

- socket => connect => send (req) => recv (res)
- the program runs the above through port 80 to connect to info from server
"""

# %% [markdown]
"""
1. prog init connection to port 80 on the www.py4e.com server
2. this prog is the web browser, so HTTP protocol requires sending GET cmd \
followed by blank line
   1. \r\n = EOL (end of line)
   2. \r\n\r\n = nothing between 2 EOL sequences (which is == to a blank line)
3. the loop recv the data in 512-chars chunks from socket and prints until \
    recv() returns empty string (there's no more data left to read)
encode() and decode() methods convert strings into bytes objects and back again
"""

# %%
# par_list = "words?sp=Kentucky"
f = "https://api.datamuse.com/words?sp=Kentucky"
# f = "https://api.datamuse.com/" + par_list
# f = "https://api.datamuse.com/words?sp=*"

data = requests.get(f)
# data = requests.get(f, params= par_list)

# print(len(data.text))
print(data.text)

# %%
dataText = [{"word": "kentucky", "score": 129541},
            {"word": "kentuck", "score": 64667}]
dataText2 = {"one": {"word": "kentucky", "score": 129541},
             "two": {"word": "kentuck", "score": 64667}}


dataText2.keys()

dataText2.get('one')


# %%
lst = ['a', 'b', 'b', 'b', 'b']

for i in dataText:
    lst.insert(1, "Hima")

print(lst)

# %%
# dataText = [
# {"word":"kentucky","score":129541},
# {"word":"kentuck","score":64667}
# ]

lst = []

for i in data.text:
    lst.insert(0, {"Hima": "kdkkd"})

print(lst)

# %%
a_u = 'https://github.com/bahim22'
# a_u = '\\pointpark.edu\\files\\apps\\idphotos\\ibalde'
data = areq.urlopen(a_u).read()
type(data)

print(data)

# %%
# open & read data from url \
# only showing output

rom_u = 'http://data.pr4e.org/romeo.txt'
fh = urllib.request.urlopen(rom_u)
for line in fh:
    print(line.decode().strip())

# %%
# retrieve data =>
# compute freq of each word in fi

fha = urllib.request.urlopen(rom_u)

counts = dict()
for line in fha:
    words = line.decode().split()
    for w in words:
        counts[w] = counts.get(w, 0) + 1
print(counts)

# %% [markdown]
# # dict method info
#
# - dict() -> new empty dict dict(mapping) -> new dict initialized from a
# mapping object's (key, value) pairs
# - dict(iterable) -> new dictinitialized as if via:
#   - d = {} for k, v in iterable:
#   - d[k] = v
# dict(**kwargs) -> new dictionary initialized with the name=value pairs
#     in the keyword argument list. For example: dict(one=1, two=2)

# %% [markdown]
# # urllib
#
# - library for opening URLs using a variety of protocols
#   - The simplest way to use this module is to call the urlopen function,
# which accepts a string containing a URL or a Request object
#
# %%
# import urllib.request

# set up authentication info
authinfo = urllib.request.HTTPBasicAuthHandler()
authinfo.add_password(
        realm='PDQ-Application', uri='https://mahler:8092/site-updates.py',
        user='klem', passwd='geheim$parole'
    )

proxy_support = urllib.request.ProxyHandler({"http": "http://ahad-haam:3128"})

# build a new opener that adds authentication and caching FTP handlers
opener = urllib.request.build_opener(
        proxy_support, authinfo, urllib.request.CacheFTPHandler
    )

# install it
urllib.request.install_opener(opener)

f = urllib.request.urlopen('https://www.python.org/')

# %% [markdown]

# `urlcleanup`: Clean up temporary files from urlretrieve calls.
# `urlopen`: Open the URL url, which can be == string | Request object.

# - *data* must be an object specifying additional data to be sent to\
# the server, or None if no such data is needed. See Request for details.
# - urllib.request module uses HTTP/1.1 and includes a "Connection:close"\
# header in its HTTP requests.
# - The optional *timeout* parameter specifies a timeout in seconds for\
# blocking operations like the connection attempt (if not specified, the\
# global default timeout setting will be used).\
# This only works for HTTP, HTTPS and FTP connections.
# - If *context* is specified, it must be a ssl.SSLContext instance \
# describing the various SSL options. See HTTPSConnection for more details.
# - The optional *cafile* and *capath* parameters specify a set of trusted \
# CA certificates for HTTPS requests. cafile should point to a single file \
# containing a bundle of CA certificates, whereas capath should point to a \
# directory of hashed certificate files. More information can be found in \
# ssl.SSLContext.load_verify_locations().
# - The *cadefault* parameter is ignored.
# - This function always returns an object which can work as a \
# context manager and has the properties \
# url, headers, and status `urlretrieve`

# - Retrieve a URL into a temporary location on disk.
# - Requires a URL argument. If a filename is passed, it is used as \
# the temporary file location. The reporthook argument should be a \
# callable that accepts a block number, a read size, and the total file size \
# of the URL target. The data argument should be valid URL encoded data.
# - If a filename is passed and the URL points to a local resource,\
# the result is a copy from local file to new file.
# - Returns a tuple containing the path to the newly created data file\
# as well as the resulting HTTPMessage object.

# %%

# par_list =
api_url = "https//:api.datamuse.com/words?"

f = open("../Docs/PyDocs22.md", "r")

# %%
res = requests.get('https://www.pointpark.edu/index')

print("Response text of res: ")
print(res.text)
print("\n===================")
print("\nContent of the url: ")
print("\n===================")
print("\nRaw data of url")

r = requests.get("https://api.github.com/events", stream=True)
print(r.raw)
print(r.raw.read(10))
# print(res.next)
# print(res.raise_for_status)
# print(res.status_code)


# %% [markdown]
# 1. res.text = Content of the response, in unicode.
# 2. res.content = Content of the response, in bytes.
# 3. iter_content: Iterates over the res data. When stream=True is set on
# the request, this avoids reading the content at once into memory for large
# responses. The chunk size is the number of bytes it should read into memory.
#    1. iter_lines: Iterates over the response data, one line at a time.
# 4. status_code, headers, json,
# 5. __non-zero__ | = This attribute checks if the status code of the response
# is between 400 and 600 to see if there was a client error or a server error.
# 6. .ok Returns True if status_code is less than 400, False if not.
# 7. res.next: Returns a PreparedRequest for the next request in a redirect
# chain, if there is one.
# 8. raise_for_status: returns HTTP error if one occurred
#
# ```py
# if HTTP error:
#     return res.status_code
#     Print(res.status_code, error)
# ```
#

# %% [markdown]
# # Requests: python HTTP Library example
#
# ## GET usage:
#
# %%
# import requests


r = requests.get('https://www.python.org')
r.status_code
# 200

print(b'Python is a programming language' in r.content)
# True or POST:

payload = dict(key1='value1', key2='value2')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
""" {
  ...
  "form": {
    "key1": "value1",
    "key2": "value2"
  },
  ...
} """

# %%

# %%
ib_pic2 = '//ppu.edu/ib11111.jpg'
ib_pic3 = 'file://ppu.edu/files/Apps/IDPhotos/ib1111.jpg'

# %%
# HOST = 'data.pr4e.org'
HOST = 'http://ppu.edu/files/Apps/IDPhotos/ib11111.jpg'
PORT = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
mysock.sendall(
    b'GET file://ppu.edu/files/Apps/IDPhotos/ib11111.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    # flow control
    # buffer between server making send() req & app recv() req
    # after filling up buffer this makes server wait for app to empty buffer
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for end of header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# skip header and save pic data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()
