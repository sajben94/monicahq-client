

MonicaHQ Client
===============
This is MonicaHQ API Wrapper for convinient access.

Installing
============

    pip install monicahq-client

Usage
=====

Create connection
-----------------

    from monicahq.Session import Session
    from monicahq.Client import Client
    session = Session("monicahq.com", "API_TOKEN")
    c = Client(session)

Search for contacts
------------------

    data = c.search_contacts()
    for contact in data['data']:
        print(contact['complete_name'])

