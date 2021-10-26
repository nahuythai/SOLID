class Database:
	@abstractmethod
	def connect(self):

class SQLDB(Database):
	def __init__(self):
	def connect(self):

class MongoDB(Database):
	def __init__(self)
	def connect(self):

class Crawler:
	def __init__(self, db):
		self.db = db
	def crawl(self):
		self.db.connect()
		.....


Crawler(SQLDB())
Crawler(MongoDB())
