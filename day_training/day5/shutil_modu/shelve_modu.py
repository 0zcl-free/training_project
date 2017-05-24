
import shelve
import datetime

d = shelve.open('shelve_test')

# info = {'age':22, 'job':'it'}
#
# name = ['alex', 'rain', 'test']
# d['name'] = name
# d['info'] = info
# d['date'] = datetime.datetime.now()
# d.close()

print(d.get('name'))
print(d.get('info'))
print(d.get('data'))