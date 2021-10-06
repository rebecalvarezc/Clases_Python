# cada variable será una query

CREATE_BEANS_TABLE = """CREATE TABLE IF NOT EXISTS beans
(id INTEGER NOT NULL UNIQUE, name TEXT NOT NULL, method TEXT NOT NULL, rating INTEGER NOT NULL,
PRIMARY KEY(id AUTOINCREMENT));"""

INSERT_BEANS = "INSERT INTO  beans (name, method, rating) VALUES (?, ?, ?);"

GATHER_BEANS = "SELECT * FROM beans;"

GATHER_BEAN_NAME = "SELECT * FROM beans WHERE name = ?;"

BEST_RATED_BEAN = "SELECT * FROM beans ORDER BY rating DESC LIMIT 1;"

USER_BEAN = "SELECT * FROM beans WHERE name = ? ORDER BY rating DESC LIMIT 1"

# Tarea: Agregar la base de datos a la app de libros.
