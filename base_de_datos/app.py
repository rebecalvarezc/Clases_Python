import sql_database

connection = sql_database.connect()  # guardo la conexión a la base de datos
sql_database.create_table(connection)
# sql_database.add_bean(connection, 'Awesome Arabica', 'Espresso', 90)
beans = sql_database.gather_beans(connection)
bean_name = sql_database.bean_name(connection, 'Exclusive')
best_bean = sql_database.best_bean(connection)
print(best_bean)