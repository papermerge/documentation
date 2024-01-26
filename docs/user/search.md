# Search

{{extra.project}} offers an extensive searching mechanism that is designed to allow you to quickly find a document you're looking for.

When you search {{extra.project}} for a document, it tries to match this query
against your documents. {{extra.project}} will look for matching documents by
inspecting their content, title, and tags.

!!! note

	{{extra.project}} searches only in **content of the last version** of the document


By default, {{extra.project}} returns only documents which contain any of the
words typed in the search bar. However, {{extra.project}} also offers
additional search syntax if you want to drill down the results further.

Matching inexact words:

	*5951

Will return document with title: brother_005951.pdf

Matching specific tags:

	tags:paid

will return documents with tag "paid"


You can match document with logical expressions:

	pizza AND salami

will return all documents containing both words: "pizza" and "salami".

	pizza AND (salami OR speciale)

will return all documents containing either "pizza" and "salami";
or "pizza" and "speciale".

!!! note

	Logical expression must be in capital case, otherwise they
	will be ignored.

Implicit logical expression is "OR". In other words, if you search:

	pizza salami

is same as you would search with following query:

	pizza OR salami

All of these constructs can be combined as you see fit.
For example, following search query will return all documents tagged with "important" and contain word "pizza":

	pizza AND tags:important
