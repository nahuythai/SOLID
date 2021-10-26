Class Crawler(high level) depend on class SQLDB, MongoDb(low level) because we implement

If we want to change or add new database, must modified class Crawler. 

To fix, we must depend on abstration class, create a abstract class for low level class
and use dependecy injection
