# doc = open('data.txt', 'r')
# si data no estuviese en la misma ruta, tengo que especificar la ruta.
# file_content = doc.read()
# doc.close()  # lo ideal es que el archivo esté abierto la menor cantidad de tiempo posible.
# print(file_content)
# Es importante cerrar el archivo. al guardar el contenido deberíamos cerrar el archivo.

user_name = input('Enter your username: \n -->')
doc = open('data.txt', 'a')
doc.write(user_name + '\n')  # al escribir no es 'importante' guardar esta variable
doc.close()
