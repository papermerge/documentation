.. _api_search:

Search
======

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core`_ in master branch.

Search REST API uses `Elasticsearch`_ backend to perform full text search on the documents and folders.


.. note:: In `Elasticsearch`_ parlance the word "document" has different meaning as in Papermerge. Throughout this reference word "document" is used in Papermerge sense.

.. _api_get_search:

GET /search/
------------

.. http:GET:: /search/

  :query q: string to search, can be any string -  from one letter to whole propositions.
  :reqheader Content-Type: application/json
  :reqheader Authorization: Token <token>
  :status 200: on success

  Searches documents and folders for matches of specific term, word, string or propositions.


  **200 - Response Body Schema**

  .. code-block:: bash

    [
      {
        id: string,
        text: string,
        title: string,
        hightlight: string,
        breadcrumb: [
          string, string, string,...
        ],
        node_type: "document" | "folder",
        user_id: string
      },
      {
        ...
      },
      ...
    ]

  ``node_type`` can be either "document" or "folder".

  If ``node_type`` is "document", then rest of the fields, including ``id`` and ``title``
  refer to a document (in papermerge sense). If ``node_type`` is "folder",
  then rest of the fields, including ``id`` and ``title`` refer to a folder
  instance.

  In case of ``node_type`` "folder", ``text`` and ``hightlight`` fields will always be
  empty.

  ``text`` field is relevant only for Papermerge documents i.e. when (``node_type`` value is "document"). ``text`` field is concatenation of all text extracted/OCRed from each page of the (last version) document. Depending on the number of pages and content of each page, ``text`` field can be very long.

  ``breadcrumb`` is a list of ancestor folder' titles of the matched node. It does not
  include matched document's title. First item in the list if the most distance ancestor's title.
  Last item in list is least distance ancestor's title. Example:
  if matched document is located in Home / My Documents / Very Important / Invoice.pdf,
  then ``breadcrumb`` will be ["Home", "My Documents", "Very Important"]. Notice that "Invoice.pdf"
  was not included in breadcrumb.

  ``highlight`` is the exterpt of the matched text wrapped in ``<em>`` tag and
  sourounded text for easier understading if match is relevant or no.


  Request example:

  .. code-block:: bash


    curl http://papermerge-example.com/api/search/?q=service \
     -H 'Content-Type: application/json' \
     -H 'Authorization: Token abcde8ccaaa42181119095c70abc9a8a' \

  Response example:


  .. code-block:: bash

    [
        {
            "id": "115",
            "text": "\nHinweise zur\nStaubsauger-Nu ... tzung\n\ne Staubsauger + Luftpistolen werden",
            "title": "brother_003961.pdf",
            "highlight": [
                "aufbewahren\n* und an allen <em>Service</em>-Stationen",
                "aufbewahren\n* und an allen <em>Service</em>-Stationen"
            ],
            "breadcrumb": [
                ".home"
            ],
            "node_type": "document",
            "user_id": "14"
        },
        {
            "id": "122",
            "text": "bitte aufbewahren\n* und an allen Service-Stationen\n* vorzeigen.\n\n* Der Beles ist nur heute sültig\n\nMr. Wash Autoservice AG\nRhinstraße 136\n12681 Berlin\nKasse/’Kassierer! 3725336\n11.85.2828 12:25:36\nSteuernummer",
            "title": "brother_003961.pdf",
            "highlight": [
                "aufbewahren\n* und an allen <em>Service</em>-Stationen"
            ],
            "breadcrumb": [
                ".home",
                "Folder 1"
            ],
            "node_type": "document",
            "user_id": "14"
        },
        {
            "id": "121",
            "text": "...long text...",
            "title": "brother_003962.pdf",
            "highlight": [
                "Gleich-hier am REWE <em>Service</em>-Punkt",
                "oder\nhier im Markt am REWE <em>Service</em>-Punkt"
            ],
            "breadcrumb": [
                ".home",
                "Folder 1"
            ],
            "node_type": "document",
            "user_id": "14"
        }
    ]


.. _Elasticsearch: https://www.elastic.co/elasticsearch/
.. _Papermerge Core: https://github.com/papermerge/papermerge-core