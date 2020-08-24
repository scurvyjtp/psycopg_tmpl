# Postgres psycopg connection template

This is an extremely barebones psycopg2 template. It is intended to provide the bare skeleton for creating a postgres connection and cursor in psycopg2 by just changing values in the config.ini file.

## config.ini
At present, there are only 4 settings.
All four are required to connect to the database

* dbname   -- database to connect to
* hostname -- host to connect to (localhost/hostname/ip)
* username -- username to connect as
* password -- password for the user

## TODO List
* don't store password in paintext
* dynamic config parsing (don't require all four settings)
* some sanity checks
