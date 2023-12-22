from db_connection import get_database_connection

cursor, db = get_database_connection()


cursor.execute("show tables from Expenses")
tables = cursor.fetchall()
print(tables)

cursor.execute("select * from Expenses.expense")
rows = cursor.fetchall()
print(rows)