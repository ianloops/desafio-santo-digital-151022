import sqlite3

connection = sqlite3.connect("university.db")
cursor = connection.cursor()

with open('database/data_definition_university.sql') as definition_file:
    definition_sql = definition_file.read()

with open('database/data_insertion_university.sql') as insertion_file:
    insertion_sql = insertion_file.read()


cursor.executescript(definition_sql)
cursor.executescript(insertion_sql)
