from __future__ import print_function
from __future__ import unicode_literals
from pprint import pprint
from elasticsearch import Elasticsearch
import json
import spacy
from spacy import displacy

es = Elasticsearch()
nlp = spacy.load('en')
#nlp = spacy.load('en_core_web_lg')

rawDocs = []
res = es.search(index="docs",
  _source_exclude="data",
  size=10000,
  body={"query": {"match_all": {}}})
for hit in res['hits']['hits']:
    rawDocs.append((hit["_source"]))

train, labels = [],[]
for doc in rawDocs:
  attachment = doc["attachment"]
  train.append(nlp(attachment["content"]))
  labels.append(doc["d_type"])

for idx, label in enumerate(labels):
  test = train[idx]
  print("Test", idx, "-", labels[idx])

  results = []
  for i, doc in enumerate(train):
    results.append((labels[i], test.similarity(doc)))

  sortedResults = sorted(results, key=lambda result:result[1],
    reverse=True)
  pprint(sortedResults[:3])
  print()
