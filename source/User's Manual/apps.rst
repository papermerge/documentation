.. apps:

Apps
======

From the very beginning of its existence, Papermerge started to receive
features requests. Many of those requests made perfect sense and were
implemented (or will be implemented). It is thanks to the  community's
feedback and contributions that Papermerge evolves naturally into a mature
archives management system.

However, a great number of features requests were subject to debate, or just
not suitable for majority of users. A very good example of such feature is
duplicates removal. First of all, what is a duplicate? There are at least three possibilities:

1. duplicate are documents with same file name
2. duplicates are documents with same digest value
3. duplicates are those documents where extracted text is >= 95% similar (i.e. very similar)

Each of points above has pros and cons. By default, Papermerge does not
implement any of those points. If you upload same files (with same content and
even same filename) it will gladly accept them. In the end, it is a matter of
preference.

Apps were introduced to address such issues. App (or plugin if you like) is a
way extend base Papermerge application. Continuing with above example with
document duplicates, by adding/removing specific Papermerge app you can
add/remove specific document duplicate removal criteria. This way, Papermerge
base application, which is called Papermerge Core will contains only essential
features.

Papermerge Core
~~~~~~~~~~~~~~~~~

Papermerge Core contains only features which are crucial for a document
management system. Organizing documents with tags and
folders are essential. Document versioning, metadata and OCR are indispensable
features archives management system - thus they are part of the Core (core features).

On the other hand, not everybody needs LDAP authentication, document
electronic signatures and data retention policies. These type of features are
good candidates for Papermerge apps. All non essential features will be
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

Writing Basic App
~~~~~~~~~~~~~~~~~~

Let's dive into a specific example and write a very simple app which will
detect file name based document duplicates.

Inside Papermerge project create a new django app:

.. code-block:: bash
    :caption: create new app
    
    $ ./manage.py startapp filebased_unique

To highlight that filebased_unique app is part of papermerge ecosystem, it will be moved into a namespace papermerge (which is just an extra folder):

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

The heart of papermerge.filebased_unique app is file models.py where core document model is extended
as following:

.. code-block:: python
    :caption: extend document model

    from papermerge.core.models import AbstractDocument


    class DocumentPart(AbstractDocument):
        """
        Extend papermerge document model with extra features
        """
        pass
