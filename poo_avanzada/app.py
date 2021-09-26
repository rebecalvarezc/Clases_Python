from admin import Admin
from database import Database

rebeca = Admin('rebeca', 123, 'guest')
ronny = Admin('ronny', 789, 'admin')
evelio = Admin('evelio', 456, 'admin')
users = [rebeca, ronny, evelio]

for x in users:
    x.save()

print(Database.content)
