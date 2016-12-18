from user import User
from message import Message
import shelve

data_b = 'db/users-db'
data_b2 = 'db/messages-db'

#	:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Messenger(User, Message):
	def addFriend(self, name):
		ad_fr = False
		ad_fr2 = False

		db = shelve.open(data_b,  writeback=True)

		for i in sorted(db):
			if name == db[i].username:
				ad_fr = True
				break
			else:
				ad_fr = False
		
		for key in sorted(db):
			if db[key].username == self.username:
				if db[key].log_in == True:
					fr = name in db[key].friends
					if fr == True: 
						raise Exception('Вы с {} уже друзья.'.format(name))
					else:
						if ad_fr == True:
							db[key].friends.append(name)
							ad_fr2 = True
							break
				else:	
					raise Exception('{} авторизуйся.'.format(self.username))

		if ad_fr == False:
			raise Exception('Пользователь {}, не зарегестрирован.'.format(name))

		if ad_fr2 == False:
			raise Exception('{}: не зарегестрирован.'.format(name))

		db.close()

	def sendMessage(self, to, text):
		flag = False

		db = shelve.open(data_b)

		for key in db:
			if to != db[key].username:
				flag = False
			else:
				msg = Message(self.username, to, text)

				flag = True
				break

		db.close()

		if flag == False:
			raise Exception('Пользователь {} не зарегестрирован.'.format(self.username))

	def log(self, name):
		flag = False
		flag2 = False

		db2 = shelve.open(data_b2)

		for key in db2:
			if db2[key]._from != self.username:
				flag = False
			else:
				flag = True
				if db2[key].to != name:
					flag2 = False
				else:
					print(db2[key])
					flag2 = True

		db2.close()

		if flag == False:
			raise Exception('{} вы не отправляли сообщений.'.format(self.username))

		if flag2 == False:
			raise Exception('Cообщений нет.')