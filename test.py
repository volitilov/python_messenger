from user import User
from message import Message
from messenger import Messenger

#	class User /////////////////////////////////////////////
#	create 	users ::::::::::::::::::::::::::::::::::::::::::

# bob = User('Bob', '123')
# i01 = User('i01', 'faint')
# sam = User('Sam', 'qwe')
# ban = User('Ban', '8787')
# xxx = User('xxx', '---')

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

# ban.addFriend('3x')

#	class Message //////////////////////////////////////////
#	::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# a = Message('Bob', 'Max', 'hello')
# b = Message('Max', 'Bob', 'Hay')

#	class Messenger ////////////////////////////////////////
#	create user messenger ::::::::::::::::::::::::::::::::::


bob = Messenger('Bob', '123')
# i01 = User('i01', 'faint')
# sam = User('Sam', 'qwe')
# ban = User('Ban', '8787')
xxx = Messenger('xxx', '---')

# xxx.addFriend('Bob')
# bob.addFriend('xxx')


# xxx.sendMessage('Bob', 'FUCK YOU')

xxx.log('Bob')

#	test addFriend() :::::::::::::::::::::::::::::::::::::::



#	shelve /////////////////////////////////////////////////
#	test users-db, messages-db :::::::::::::::::::::::::::::

import shelve

# d = shelve.open('db/users-db')
d = shelve.open('db/messages-db')

print(list(d))

for key in d:
	print(d[key])

# print(d['Bob'].__class__) 	# <class 'user.User'>
# print(d['Bob'].__class__.__name__) 	# User
# print(list(d.__dict__.keys())) 	# ['writeback', 'dict', '_protocol', 'cache', 'keyencoding']

# del d['1'], d['2'], d['3'], d['4']
# d.clear()

# d['1'] = d['6']
# del d['2'], d['3'], d['4']

d.close()