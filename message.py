import shelve
data_b2 = 'db/messages-db'

#	:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Message():
	def __init__(self, _from, to, text):
		self._from = _from
		self.to = to
		self.text = text

		db = shelve.open(data_b2)
		db['{}'.format(len(list(db)) + 1)] = self
		db.close()

	def gatherAttrs(self):
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append('{}: {}'.format(key, getattr(self, key)))
		return ', '.join(attrs)

	def __str__(self):
		return '[{} => {}]'.format(self.__class__.__name__, self.gatherAttrs())