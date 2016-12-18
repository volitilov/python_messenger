import shelve
data_b = 'db/users-db'

#	:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.friends = []
		self.log_in = False

	def registration(self): 
		db = shelve.open(data_b)

		for key in sorted(db):
			if db[key].username == self.username:
				raise Exception('Пользователь {} есть в базе.'.format(self.username))
		
		db['{}'.format(len(list(db)) + 1)] = self

		db.close()

	def login(self):
		db = shelve.open(data_b,  writeback=True)
		
		for key in sorted(db):
			# reg = False if (db[key].username, db[key].password) != (self.username, self.password) else True
			if (db[key].username, db[key].password) == (self.username, self.password):
				db[key].log_in = True
				break
			else:
				db[key].log_in = False

		if db[key].log_in == False:
			raise Exception('{} регестрируйся.'.format(self.username))

		db.close()