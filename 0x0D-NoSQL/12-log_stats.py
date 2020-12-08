#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

client = MongoClient('mongodb://127.0.0.1:27017')
nginx = client.logs.nginx

print(
    "{} logs".format(
        nginx.count({})
    )
)

print("Methods:")

for method in methods:
    print(
        "\tmethod {}: {}".format(
            method, nginx.count({'method': method})
        )
    )

print(
    "{} status check".format(
        nginx.count({'method': 'GET', 'path': '/status'})
    )
)
