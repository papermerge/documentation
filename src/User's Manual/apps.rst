.. apps:

Apps
======

From the very beginning of its existence, Papermerge started to receive
features requests. Many of those requests made perfect sense and were
implemented (or will be implemented). It is thanks to the community's
feedback and contributions that Papermerge evolves naturally into a mature
archives management system.

However, a great number of features requests were subject to debate, or just
not suitable for majority of users. A very good example of such feature is
duplicates removal. First of all, how to define that a specific document is a
duplicate (of other document)?

There are at least three possibilities:

1. duplicate are documents with same file name
2. duplicates are documents with same digest value
3. duplicates are those documents where extracted text is >= 95% similar (i.e. very similar)

Each of points above has pros and cons. Each of them may be right under
specific circumstances and for specific user or company requirements. By
default, Papermerge does not implement any of those points. Even more, if you
upload files with __same content and filename__ Papermerge will gladly
accept them. In the end, duplicating documents or preventing them, is just a
matter of preference.

Apps were introduced to address such issues. Apps (or plugins if you like) are a
way to extend the base of Papermerge. Continuing with the example above,
duplicating documents, by adding/removing a specific Papermerge app, you can
add/remove specific document duplicate detection criterias. This way, Papermerge
base application, which is called Papermerge Core will contain only essential
features.

Papermerge Core
~~~~~~~~~~~~~~~~~

On the other hand, document management system are complex applications, with
rich set of requirements such as LDAP authentication, document electronic
signatures and even such fancy things as data retention policies. Not
everybody needs LDAP authentication though. Also, not everybody uses document
electronic signatures and data retention policies. These type of features are
very good candidates for Papermerge apps. All non essential features will be
implemented as apps which can be easily plugged or removed.


Meet Papermerge Apps
~~~~~~~~~~~~~~~~~~~~~

Papermerge app is basically a Django app with few extras. You may wonder what
is Django app anyway? First of all, Papermerge is build with help of web
framework called `Django <https://www.djangoproject.com/>`_. Secondly,
Papermerge project is a Django project which in turn is a loose collection of
Django apps plus (project) settings. Figure 1 illustrates this idea.

.. figure:: ../img/user-manual/apps/papermerge-project.svg
    :alt: Papermerge project is basically Django project

    Figure 1. Illustrates that Papermerge project is composed of a number of apps plus
    configuration settings. Papermerge project is very same as Django project.

Notice that Papermerge Core app is part of every Papermerge project. 

Writing a Basic App
~~~~~~~~~~~~~~~~~~~

The gory details of how to develop apps and include them into papermerge
project are explained in contributing guide. Here, in user manual, only high
level concepts are explained.

Let's consider an app which will detect filename duplicates. 
If used, the app will issue an error when the user tries to upload two documents
with the same filenames. 
Keep in mind that here the goal is to familiarize with general
concepts.

Inside Papermerge create a new django app:

.. code-block:: bash
    :caption: create new app
    
    $ ./manage.py startapp filebased_unique

To highlight that filebased_unique app is part of papermerge ecosystem, it will be moved into the papermerge namespace (which is just an extra folder):

.. code-block:: bash
    :caption: move filebased_unique django app inside papermerge folder
    
    $ mkdir papermerge
    $ mv filebased_unique papermerge/

Also, change ``name`` and ``label`` app attributes as shown below:

.. code-block:: python
    :caption: change ``name`` and ``label`` attributes
    
    from django.apps import AppConfig


    class FilebasedUniqueConfig(AppConfig):
        name = 'papermerge.filebased_unique'
        label = 'filebased_unique'

The heart of papermerge.filebased_unique app is 
papermerge/filebased_unique/models.py where the core document model is extended as
following:

.. code-block:: python
    :caption: extend document model

    from django.core.exceptions import ValidationError
    from papermerge.core.models import Document, AbstractDocument


    class DocumentPart(AbstractDocument):

        def clean(self):

            file_name = self.get_file_name()

            if Document.objects.filter(file_name=file_name).count() > 1:
                raise ValidationError(
                    "Document file_name duplicates detected"
                )


Here is a link to `app code <https://github.com/papermerge/papermerge-filebased-unique>`_ on GitHub.


Document Parts
~~~~~~~~~~~~~~~~

Apps are not just for adding extra validations, you can add extra fields
to the core document as well.

For example, in case you want to add a special UUID field to the document model:

.. code-block:: python
    :caption: extend core document model with extra fields

    import uuid
    from django.db import models

    from papermerge.core.models import AbstractDocument


    class DocumentPart(AbstractDocument):

        special_uuid = models.UUIDField(
            default=uuid.uuid4,
            editable=False
        )

Those extra fields added by apps to core document model - are called *document
parts*. Papermerge Core treats core document fields and those extra
fields added by apps as one whole:


.. figure:: ../img/user-manual/apps/document-parts.svg
    :alt: Papermerge treats all document parts augmentet by apps as one whole

    Figure 2. Papermerge treats all document parts augmentet by external apps as one whole.

This way, any user or company, can extend the core document model with whatever
number of custom fields they wish without interfering with the core application
code.


Document Widgets
~~~~~~~~~~~~~~~~~

.. note::

    This feature is experimental.

Each document part (i.e all those extra fields) will be visualized as widgets on the :ref:`ui_right_side_widgets_panel_in_doc_browser` along with metadata widget and basic info widget.
