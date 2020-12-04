#!/usr/bin/env python3
"""
Main file for testing.
"""
from web import get_page, r


url = 'https://www.google.com'

name = 'count: ' + '{' + url + '}'

gp = get_page(url)
get_page(url)
get_page(url)
count = r.get(name)
print(count)
