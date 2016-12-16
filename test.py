from user import User
from addFriend import Add_friend as AFr
from msg import Message

#	class User /////////////////////////////////////////////
#	create 	users ::::::::::::::::::::::::::::::::::::::::::

bob = User('Bob', '123')
i01 = User('i01', 'faint')
sam = User('Sam', 'qwe')
ban = User('Ban', '8787')
xxx = User('xxx', '---')

#	test registration ::::::::::::::::::::::::::::::::::::::

# bob.registration()
# i01.registration()
# sam.registration()
# ban.registration()
# xxx.registration()

#	test login :::::::::::::::::::::::::::::::::::::::::::::

# bob.login()
# i01.login()
# sam.login()
# ban.login()
# xxx.login()


#	class Add_friend ///////////////////////////////////////
#	::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# xxx = AFr('3x', '123')

# xxx.registration()
# xxx.login()

#	test addFriends ::::::::::::::::::::::::::::::::::::::::

ban.addFriend('3x')

#	class Message //////////////////////////////////////////
#	::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# xxx.sendMessage('Ban', 'hello')


#	shelve /////////////////////////////////////////////////
#	test users-db ::::::::::::::::::::::::::::::::::::::::::

import shelve

d = shelve.open('db/users-db')

print(list(d))

for key in d:
	print(d[key])

# print(d['Bob'].__class__) 	# <class 'user.User'>
# print(d['Bob'].__class__.__name__) 	# User
# print(list(d.__dict__.keys())) 	# ['writeback', 'dict', '_protocol', 'cache', 'keyencoding']

# del d['1'], d['2'], d['3'], d['4']
# d.clear()

# d['1'] = d['6']
# del d['6']

d.close()