import aiomysql

class SQL:
    def __init__(self, host, port, username, password, db):
        self.conn = None
        self.cursor = None
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    async def connect(self):
        if self.conn is None:
            try:
                self.conn = await aiomysql.connect(host=self.host, port=self.port, user=self.username, password=self.password, db=self.db)
                self.cursor = await self.conn.cursor()
                return True
            except aiomysql.Error as err:
                print(err)
                return False
        return True

    async def query(self, sql, params = [], fetchall = False, fetchone = False):
        await self.cursor.execute(sql, params)
        if sql[0:6] == "SELECT":
            if fetchall:
                return await self.cursor.fetchall()
            elif fetchone:
                return await self.cursor.fetchone()
            else:
                return await self.cursor.fetchone()
        else:
            await self.conn.commit()
            return {"rowcount": self.cursor.rowcount, "last_insert_id": self.cursor.lastrowid}

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None