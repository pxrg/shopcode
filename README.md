SaaS - Software as a Service
====

Install
----

1. Clone repository
2. Install requirements `pip install -r requirements.txt`
3. Create database `saas` in PostgreSQL
4. Run command `./manage.py sync_schemas` and `./manage.py migrate_schemas`
5. Populate dabatase with some required informations `./manage.py loaddata fixtures/dump_initial.json`
    - Create a Client with domain name **saas.io** and schema name **public**
    - Create **superuser** to Client with username:*root* and pass:*123456*
6. Add to your hosts file the following line:

    127.0.0.1           saas.io

    > Obs.: For every client register, add one line to your hosts file
