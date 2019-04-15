d = { 'name': 'xx', 'age': 18, 'sex': 'm'}
from operator import itemgetter
print(sorted(d.items(), key=itemgetter(0)))