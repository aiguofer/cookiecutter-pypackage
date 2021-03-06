.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.package_name }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone {{ cookiecutter.git_host | replace("https", "git") }}/{{ cookiecutter.git_host_username }}/{{ cookiecutter.project_slug }}

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL {{ cookiecutter.git_host }}/{{ cookiecutter.git_host_username }}/{{ cookiecutter.project_slug }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: {{ cookiecutter.git_host }}/{{ cookiecutter.git_host_username }}/{{ cookiecutter.project_slug }}
.. _tarball: {{ cookiecutter.git_host }}/{{ cookiecutter.git_host_username }}/{{ cookiecutter.project_slug }}/tarball/master
