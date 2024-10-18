from django.core.management import BaseCommand
import pyodbc
from config.settings import DATABASE, USER, PASSWORD, HOST

class Command(BaseCommand):
    connectionString = f'''DRIVER={{ODBC Driver 17 for SQL Server}};
                           SERVER={HOST};
                           DATABASE={DATABASE};
                           UID={USER};
                           PWD={PASSWORD}'''
    try:
        conn = pyodbc.connect(connectionString)
        conn.autocommit = True
        conn.execute(fr'CREATE DATABASE Django_project;')
    except pyodbc.ProgrammingError as ex:
        print(ex)
    else:
        conn.execute(fr'CREATE DATABASE Django_project;')
        print('База данных создана!')
    finally:
        conn.close()

