friends = input('Escribe el nombre de 3 amigos. Separalos por comas, sin espacios. \n -->').split(',')
doc = open('people.txt', 'r')
people_nearby =[i.strip() for i in doc.readlines()]
doc.close()

people_nearby_set = set(people_nearby)
unique_friends = set(friends)

friends_nearby = people_nearby_set.intersection(unique_friends)  # los sets son como los conj de matematicas. Sin almacenar valores repetidos.
new_doc = open('close_friends.txt', 'w')
for friend in friends_nearby:
    new_doc.write(friend + '\n')
new_doc.close()