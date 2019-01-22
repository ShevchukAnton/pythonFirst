import mysql.connector as connector


class UseDatabase:

    def __init__(self, dbconfigs: dict) -> None:
        """Initialize configuration to connect to DB"""
        self.dbconfig = dbconfigs

    def __enter__(self) -> 'DBcursor':
        """Create new connection to DB and return cursor"""
        self.conn = connector.connect(**self.dbconfig)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Flush all changes to DB, close cursor, close connection"""
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
