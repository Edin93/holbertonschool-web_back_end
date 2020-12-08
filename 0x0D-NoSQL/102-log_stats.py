#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_infos() -> None:
    """ Provides some stats about Nginx logs stored in MongoDB. """

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(
        "{} logs".format(
            nginx.count_documents({})
        )
    )

    print("Methods:")

    for method in methods:
        print(
            "\tmethod {}: {}".format(
                method, nginx.count_documents({'method': method})
            )
        )

    print(
        "{} status check".format(
            nginx.count_documents({'method': 'GET', 'path': '/status'})
        )
    )

    print("IPs:")

    ips = []


    top_ips = nginx.aggregate([
        { "$group": {  "_id" : "$ip", "total" : { "$sum": 1 }  } },
        { "$sort": { "total": -1 } }
    ])

    i = 0
    for ip in top_ips:
        if i == 10:
            break
        print(
            "\t{}: {}".format(
                ip.get('_id'),
                ip.get('total')
            )
        )
        i += 1

if __name__ == "__main__":
    log_infos()
