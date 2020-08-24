#!/usr/bin/python3
import configparser, psycopg2

########################################
##   Utility Functions               ###
########################################

## read_configmap: import data from config.ini
def read_configmap(config, section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section,option)
        except:
            print("Exception on %s!" % option)
            exit(1)
    return dict1

## print_dict: print keyvalue pairs from a dict
def print_dict(d):
    for k,v in d.items():
        print(k,v)

## db_connect: postgres database connection helper
def db_connect(dbs):
    conn_str = "host=%s dbname=%s port=%s user=%s password=%s" \
             % (dbs['hostname'], dbs['dbname'], dbs['port'], \
                dbs['username'], dbs['password'])
    try:
        conn = psycopg2.connect(conn_str)
        print('Connection Established!')
    except Exception as e:
        print('Connection Error: %s' % (e))
        return
    return conn

## db_cursor: create cursor
def db_cursor(conn):
    try:
        curs = conn.cursor()
        print('Crusor created.')
    except Exception as e:
        print('Couldn\'t ceate Cursor: %s' % (e))
        return
    return curs

########################################
##   Main                             ##
##     - Do the thing                 ##
########################################
def main():
    # Read in config settings
    config = configparser.ConfigParser()
    config.read('./config.ini')

    # Convert Database section of config map into db_settings dictionary
    db_settings = read_configmap(config, 'Database')

    # create database connection and cursor
    conn = db_connect(db_settings)
    curs = db_cursor(conn)

    # close cursor and connection
    curs.close()
    conn.close()

main()
