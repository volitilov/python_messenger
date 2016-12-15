from user import User
import shelve
data_b = 'db/users-db'

class Add_friend(User):
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



# user.sendMessage('vasya', 'hello')

# user.log('vasya')

# [ { from: 'lalka', to: 'vasya', text: 'hello' } ]


# def sendMessage(self, to, text):
# 	msg = new Message(self.username, to, text)