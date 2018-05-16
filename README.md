# CP681 - Directed Studies
Ryan Kazmerik

## Check-in - May 14th, 2018
* Setup ElasticSearch development environment and installed spaCy NLP toolkit with two pre-built english language models.
* Installed ElasticSearch ingest attachment plugin for indexing PDF documents.
* Gathered 30 sample PDF documents, each labelled with a class of 'Analysis', 'Correspondence' or 'Summary'.
* Wrote a simple data loader (loader.py) for ingesting PDF documents into ElasticSearch including the class label.
* Wrote a simple model (model.py) that computes the spaCy similarity score between each sample document and the rest of the corpus.

### Results:
For each document in the corpus, the similarity to every other document is calculated, and the top three similar documents are shown.

<pre>
Test 1 - Analysis
[(u'Analysis', 1.0),
 (u'Analysis', 0.9940898954322718),
 (u'Analysis', 0.9513261611607577)]

Test 2 - Analysis
[(u'Analysis', 1.0),
 (u'Analysis', 0.9974945618647215),
 (u'Analysis', 0.9584604169442155)]

Test 3 - Analysis
[(u'Analysis', 1.0),
 (u'Analysis', 0.9853001042441596),
 (u'Analysis', 0.9778452694474005)]
</pre>
