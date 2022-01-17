.. _api_preferences:

Preferences
=============

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core`_ in master branch.

.. _api_get_preferences:

GET /preferences/
------------------

.. http:GET:: /preferences/

  :query section: list all preferences with this section **name**
  :reqheader Content-Type: application/json
  :reqheader Authorization: Token <token>
  :status 200: on success

  Lists all user preferences (of current user)


  **200 - Response Body Schema**

  .. code-block:: bash

    {
      links: {
        first: string,
        last: string,
        next: string,
        prev: string
      },
      data: [
        {
          id: string,
          type: "preferences",
          attributes: {
            section: string,
            name: string,
            verbose_name: string,
            help_text: string,
            identifier: string,
            default: string,
            value: string | integer
            additional_data: BooleanTypeData | ChoiceTypeData | CharTypeData,
            field: BooleanTypeField | ChoiceTypeField | CharTypeField
          }
        },
        {
          ...
        },
        ...
      ],
      meta: {
        pagination: {
            page: integer,
            pages: integer,
            count: integer
        }
      }
    }

  **Example Response**

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "links": {
        "first": "http://papermerge.local/api/preferences/?page%5Bnumber%5D=1",
        "last": "http://papermerge.local/api/preferences/?page%5Bnumber%5D=1",
        "next": null,
        "prev": null
      },
      "data": [
        {
          "type": "preferences",
          "id": "18",
          "attributes": {
            "section": "localization",
            "name": "data_format",
            "identifier": "localization__data_format",
            "default": "%Y-%m-%d",
            "value": "%Y-%m-%d",
            "verbose_name": null,
            "help_text": "Date format",
            "additional_data": {
              "choices": [
                [
                    "%Y-%m-%d",
                    "2020-11-25"
                ],
                [
                    "%a %d %b, %Y",
                    "Wed 25 Nov, 2020"
                ],
                [
                    "%d %b, %Y",
                    "25 Nov, 2020"
                ],
                [
                    "%m/%d/%Y",
                    "11/25/2020"
                ],
                [
                    "%d/%m/%Y",
                    "25/11/2020"
                ],
                [
                    "%d.%m.%y",
                    "25.11.20"
                ],
                [
                    "%d.%m.%Y",
                    "25.11.2020"
                ]
              ]
            },
            "field": {
              "class": "ChoiceField",
              "widget": {
                "class": "Select"
              },
              "input_type": "select"
            }
          }
        },
        {
          "type": "preferences",
          "id": "21",
          "attributes": {
            "section": "ocr",
            "name": "trigger",
            "identifier": "ocr__trigger",
            "default": "auto",
            "value": "manual",
            "verbose_name": null,
            "help_text": "OCR Process Trigger",
            "additional_data": {
              "choices": [
                [
                  "auto",
                  "Automatic"
                ],
                [
                  "manual",
                  "Manual"
                ]
              ]
            },
            "field": {
              "class": "ChoiceField",
              "widget": {
                "class": "Select"
              },
              "input_type": "select"
            }
          }
        },
      ]
    }


GET /preferences/{section__name}/
---------------------------------

.. http:GET:: /preferences/{section__name}/

  :reqheader Content-Type: application/json
  :reqheader Authorization: Token <token>
  :status 200: on success

  Returns details of the user preferences identified with {section__name}.


  **200 - Response Body Schema**

  .. code-block:: bash

    {
      data: {
        id: string,
        type: "preferences",
        attributes: {
          section: string,
          name: string,
          verbose_name: string,
          help_text: string,
          identifier: string,
          default: string,
          value: string | integer
          additional_data: BooleanTypeData | ChoiceTypeData | CharTypeData,
          field: BooleanTypeField | ChoiceTypeField | CharTypeField
        }
      }
    }

  **Example Request**

  .. sourcecode:: http

    GET /preferences/ocr__trigger/  HTTP/1.1

  **Example Response**

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "data": {
        "type": "preferences",
        "id": "21",
        "attributes": {
          "section": "ocr",
          "name": "trigger",
          "identifier": "ocr__trigger",
          "default": "auto",
          "value": "manual",
          "verbose_name": null,
          "help_text": "OCR Process Trigger",
          "additional_data": {
            "choices": [
              [
                  "auto",
                  "Automatic"
              ],
              [
                  "manual",
                  "Manual"
              ]
            ]
          },
          "field": {
            "class": "ChoiceField",
            "widget": {
                "class": "Select"
            },
            "input_type": "select"
          }
        }
      }
    }

PATCH /preferences/{section__name}/
------------------------------------

.. http:PATCH:: /preferences/{section__name}/

  :reqheader Content-Type: application/json
  :reqheader Authorization: Token <token>
  :status 200: on success

  Updates **the value** of user preference identified with {section__name}. Body is expected to have following structure:

  .. code-block:: bash

    {
      "value": <new-value>
    }

  **Example Request**

  .. sourcecode:: http

    PATCH /preferences/ocr__trigger/  HTTP/1.1

    {
      "value": "auto"
    }

  **Example Response**

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "data": {
        "type": "preferences",
        "id": "21",
        "attributes": {
          "section": "ocr",
          "name": "trigger",
          "identifier": "ocr__trigger",
          "default": "auto",
          "value": "auto",
          "verbose_name": null,
          "help_text": "OCR Process Trigger",
          "additional_data": {
            "choices": [
              [
                  "auto",
                  "Automatic"
              ],
              [
                  "manual",
                  "Manual"
              ]
            ]
          },
          "field": {
            "class": "ChoiceField",
            "widget": {
                "class": "Select"
            },
            "input_type": "select"
          }
        }
      }
    }


POST /preferences/bulk/
---------------------------------

.. http:POST:: /preferences/bulk/

  :reqheader Content-Type: application/json
  :reqheader Authorization: Token <token>
  :status 200: on success

  Updates user preferences in bulk. Body is expected to have following structure:

  .. code-block:: bash

    {
      "section1__name1": <new-value1>,
      "section2__name2": <new-value2>
      "section3__name3": <new-value3>
    }

  **Example Request**

  .. sourcecode:: http

    POST /preferences/bulk/  HTTP/1.1

    {
      "ocr__trigger": "auto",
      "ocr__language": "eng"
    }

  **Example Response**

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
    "data": [
      {
        "section": "ocr",
        "name": "language",
        "identifier": "ocr__language",
        "default": "deu",
        "value": "eng",
        "verbose_name": null,
        "help_text": "Language used for OCR processing",
        "additional_data": {
          "choices": [
            [
                "deu",
                "Deutsch"
            ],
            [
                "eng",
                "English"
            ]
          ]
        },
        "field": {
          "class": "ChoiceField",
          "widget": {
            "class": "Select"
          },
          "input_type": "select"
        }
      },
      {
        "section": "ocr",
        "name": "trigger",
        "identifier": "ocr__trigger",
        "default": "auto",
        "value": "auto",
        "verbose_name": null,
        "help_text": "OCR Process Trigger",
        "additional_data": {
          "choices": [
            [
                "auto",
                "Automatic"
            ],
            [
                "manual",
                "Manual"
            ]
          ]
        },
        "field": {
          "class": "ChoiceField",
          "widget": {
            "class": "Select"
          },
          "input_type": "select"
        }
      }
    ]
  }


Boolean Type
-------------

  **BooleanTypeData**


  BooleanTypeData is always empty:

  .. code-block:: bash

    {}

  **BooleanTypeField**

  .. code-block:: json

    {
      "class": "BooleanField",
      "widget": {
          "class": "CheckboxInput"
      },
      "input_type": "checkbox"
    }

Choices Type
-------------

  **ChoiceTypeData**

  .. code-block:: bash

    {
      choices: [
          [
              string,  # key
              string   # value
          ],
          [
              string,  # key
              string   # value
          ],
          ...
      ]
    }

  **ChoiceTypeField**

  .. code-block:: json

    {
      "class": "ChoiceField",
      "widget": {
          "class": "Select"
      },
      "input_type": "select"
    }


Char Type
----------

  **CharTypeData**


  CharTypeData is always empty

  .. code-block:: bash

    {}

  **CharTypeField**


  .. code-block:: json

    {
      "class": "CharField",
      "widget": {
          "class": "TextInput"
      },
      "input_type": "text"
    }


.. _Papermerge Core: https://github.com/papermerge/papermerge-core