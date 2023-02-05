Downloading
=============

The source is currently only available via GitHub. You can either clone it with ``git``:

.. code-block:: bash
    :caption: Close directly from repository

    $ git clone  --depth 1 --branch v1.5.5 https://github.com/ciur/papermerge.git
    $ cd papermerge

Notice ``--branch`` option. Always clone from latest stable release branch. See all `available stable releases here <https://github.com/ciur/papermerge/releases>`_.

.. note::

    Master branch is used for development.

or just download the tarball for latest stable release:


.. code-block:: bash
    :caption: Download the tarball for latest stable release

    $ cd to the directory where you want to run Papermerge
    $ wget https://github.com/ciur/papermerge/archive/v1.5.5.zip
    $ unzip v1.5.5.zip
    $ cd papermerge-1.5.5


Papermerge-Core
~~~~~~~~~~~~~~~~~~~

.. note::

    Below information will be interesting for software developers

The `GitHub repository <https://github.com/ciur/papermerge/releases>`_
mentioned above is the Papermerge's `Django project
<https://www.djangoproject.com/>`_. A good way to think about (any) Django
project is a as a collection of reuseable apps plus project specific
configurations. The above mentioned repository contains mostly configurations,
unit tests and references for further dependencies. If you will look for
actual application code - you won't find it there. Instead, the most important
part, the heart of it so to speak, was extracted into separate reusable django
app called `Papermerge Core <https://github.com/papermerge/papermerge-core>`_.

If you want learn in detail Papermerge's source code you will need to check `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ repository as well.