from user import User
import shelve
data_b = 'db/users-db'
data_b2 = 'db/msg-db'

class Message(User):
	def sendMessage(self, to, text):
		flag = False

		db = shelve.open(data_b)

		for key in db:
			if to != db[key].username:
				flag = False
			else:
				db2 = shelve.open(data_b2, writeback=True)
				db2['{}'.format(len(list(db2)) + 1)] = {'from': self.username, 'to': to, 'text': text}
				db2.close()

				flag = True
				break

		db.close()

		if flag == False:
			raise Exception('Пользователь {} не зарегестрирован.'.format(self.username))


	def log(self, name):
		flag = False

		db2 = shelve.open(data_b2)

		for key in db2:
			if db2[key['from']] != self.username:
				flag = False
			else:
				print(db[key])
				flag = True
				break

		db2.close()

		if flag == False:
			raise Exception('{} у вас нет сообщений.'.format(self.username))

	

	def gatherAttrs(self):
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append('{}: {}'.format(key, getattr(self, key)))
		return ', '.join(attrs)

	def __str__(self):
		return '[{} => {}]'.format(self.__class__.__name__, self.gatherAttrs())



# user.sendMessage('vasya', 'hello')

# user.log('vasya')

# [ { from: 'lalka', to: 'vasya', text: 'hello' } ]


# def sendMessage(self, to, text):
# 	msg = new Message(self.username, to, text)