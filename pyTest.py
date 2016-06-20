#!/usr/local/bin/python
import sys, json

query = sys.argv[1]

itemArray = []
itemArray.append({"uid": query, "title": query, "subtitle": query})

print json.dumps({"items": itemArray})