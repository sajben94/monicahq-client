

MonicaHQ Client
===============
This is MonicaHQ API Wrapper for convinient access to data.

Installing
============

.. code-block:: bash

    pip install monicahq-client

Usage
=====

Create connection
=================
.. code-block:: python
    from Session import Session
    from Client import Client
    session = Session("monicahq.com", "API_TOKEN")
    c = Client(session)

Search for contacts
===================
.. code-block:: python
    data = c.search_contacts()
    for contact in data['data']:
        print(contact['complete_name'])

