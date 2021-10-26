class SQLDB:
	def __init__(self):
	def connect(self):

class MongoDB:
	def __init__(self):
	def mongo_connect(self):

class Crawler:
	def __init__(self)
	def crawl(self, db):
		if db == 'sql':
			sql = SQLDB()
			sql.connect()
		if db == 'mongo':
			mongo = MongoDB()
			mongo.connect()			
		....

crawler = Crawler()
crawler.crawl('sql')
