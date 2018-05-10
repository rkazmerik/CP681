from __future__ import print_function
from elasticsearch import Elasticsearch
import base64
import json
import os

es = Elasticsearch()
docs = []

# Loop through all the pdfs in the docs dir
for file in os.listdir("docs/Well Analysis"):
    f = open("docs/Well Analysis/" + file, "rt").read()
    data = base64.b64encode(f).decode('ascii')
    docs.append({"index": {"_index":"docs", "_type":"doc", "pipeline":"attachment"}})
    docs.append({"data": data, "d_type": "Analysis"})

for file in os.listdir("docs/Contract Summary"):
    f = open("docs/Contract Summary/" + file, "rt").read()
    data = base64.b64encode(f).decode('ascii')
    docs.append({"index": {"_index":"docs", "_type":"doc", "pipeline":"attachment"}})
    docs.append({"data": data, "d_type": "Summary"})

for file in os.listdir("docs/Mineral Correspondence"):
    f = open("docs/Mineral Correspondence/" + file, "rt").read()
    docs.append({"index": {"_index":"docs", "_type":"doc", "pipeline":"attachment"}})
    docs.append({"data": data, "d_type": "Correspondence"})

resp = es.bulk(docs)

if (resp["errors"] == False):
  print("Ingest successfully completed:", len(resp["items"]), "docs")