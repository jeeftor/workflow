#!/usr/local/bin/python
import sys, json

query = sys.argv[1]

itemArray = []
itemArray.append({"uid": query, "title": "Query string in subtitle", "subtitle": query})

print json.dumps({"items": itemArray})