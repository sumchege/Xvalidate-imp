from core_domain.Repos.subsytemRepository import SubsystemRepository
from core_domain.subsystem import Subsystem
import sqlite3


print("Table created")                        
class sqlSubsystemRepository(SubsystemRepository):
     
    def __init__(self, db):
        self.db = db
         
         
     
    def add(self, subsystem):
        cursor = self.db.cursor()
        sql = '''INSERT INTO subsystem(name, date_created) VALUES(?, ?)'''
        params = (subsystem.name, subsystem.date_created)
         
        cursor.execute(sql, params)
        self.db.commit()
 
     
    def edit(self, subsystem_id, subsystem):
        cursor = self.db.cursor()
        sql = '''UPDATE subsystem SET name=?  WHERE id=?'''
        params = (subsystem.name, subsystem_id)
        cursor.execute(sql, params)
        self.db.commit()
         
 
     
    def delete(self, subsystem_id):
        cursor = self.db.cursor()
        sql = '''DELETE FROM subsystem WHERE id=?'''
        params = (subsystem_id, )
        cursor.execute(sql, params)
        self.db.commit()
 
     
    def getAll(self):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, date_created FROM subsystem'''
        rows = [Subsystem(id=row['id'], name=row['name'], date_created=row['date_created']) for row in cursor.execute(sql).fetchall()]
        return rows
         
 
     
    def getby_id(self, subsystem_id):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, date_created FROM subsystem WHERE id = ?'''
        params = (subsystem_id, )
        rows = [Subsystem(id=row['id'], name=row['name'], date_created=row['date_created']) for row in cursor.execute(sql, params).fetchall()]
        return rows
        pass
   
   
import datetime
db = sqlite3.connect('../db/sysdb.db')
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sub = Subsystem(id=None, name="Communication", date_created=date)
repo = sqlSubsystemRepository(db)
# # repo.delete(2)
repo.add(sub)
for row in repo.getAll():
    print(row.id, row.name, row.date_created)
db.close()
