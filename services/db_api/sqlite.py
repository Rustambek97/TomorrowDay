import aiosqlite

class Database:
    def __init__(self, db_path = "config/main.db"):
        self.db_path = db_path

    async def execute(self, sql, parameters = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()

        # Ma'lumotlar bazasiga ulanish
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(sql, parameters)

            data = None
            if fetchone:
                data = await cursor.fetchone()
            if fetchall:
                data = await cursor.fetchall()

            if commit:
                await db.commit()

            return data

import aiosqlite

class Database:
    def __init__(self, db_path: str = "config/main.db"):
        self.db_path = db_path

    async def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()

        # Ma'lumotlar bazasiga ulanish
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(sql, parameters)

            data = None
            if fetchone:
                data = await cursor.fetchone()
            if fetchall:
                data = await cursor.fetchall()

            if commit:
                await db.commit()

            return data

    async def add_user(self, id: int, name: str, email: str = None):
        sql = "INSERT INTO Users(id, name, email) VALUES(?, ?, ?)"
        await self.execute(sql, parameters=(id, name, email), commit=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetchall=True)

    async def count_users(self):
        res = await self.execute("SELECT COUNT(*) FROM Users", fetchone=True)
        return res[0] if res else 0

    async def update_user_email(self, email: str, id: int):
        sql = "UPDATE Users SET email=? WHERE id=?"
        await self.execute(sql, parameters=(email, id), commit=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", commit=True)

db = Database()