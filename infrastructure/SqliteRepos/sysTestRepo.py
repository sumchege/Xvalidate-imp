from core_domain.Repos.systestRepository import SysTestRepository
from core_domain.systest import SysTest
import sqlite3


class sqlSysTestRepository(SysTestRepository):
    
    def __init__(self, db):
        self.db = db
        
        
    
    def add(self, systest):
        cursor = self.db.cursor()
        sql = '''INSERT INTO systest(name, date_time, type, data_filename, config_filename , date_created) VALUES(?, ?, ?, ?, ?, ?)'''
        params = (systest.name, systest.date_time, systest.type, systest.data_filename, systest.config_filename, 
                  systest.date_created)
        
        cursor.execute(sql, params)
        self.db.commit()

    
    def edit(self, systest_id, test):
        cursor = self.db.cursor()
        sql = '''UPDATE systest SET name=?, date_time=?, type =?, data_filename=?, config_filename=? WHERE id=?'''
        params = (test.name, test.date_time, test.type, test.data_filename, test.config_filename, systest_id)
        cursor.execute(sql, params)
        self.db.commit()
        

    
    def delete(self, systest_id):
        cursor = self.db.cursor()
        sql = '''DELETE FROM systest WHERE id=?'''
        params = (systest_id, )
        cursor.execute(sql, params)
        self.db.commit()

    
    def getAll(self):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, date_time, type, data_filename, config_filename, date_created FROM systest'''
        rows = [SysTest(id=row['id'], name=row['name'], date_time=row['date_time'], type=row['type'], data_filename=row['data_filename'], config_filename=row['config_filename'], date_created=row['date_created']) for row in cursor.execute(sql).fetchall()]
        return rows
        

    def getby_id(self, systest_id):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, date_time, type, data_filename, config_filename, date_created FROM systest WHERE id = ?'''
        params = (systest_id, )
        rows = [SysTest(id=row['id'], name=row['name'], date_time=row['date_time'], type=row['type'], data_filename=row['data_filename'], config_filename=row['config_filename'], date_created=row['date_created']) for row in cursor.execute(sql, params).fetchall()]
        return rows
        pass
    
# import datetime
# db = sqlite3.connect('../db/sysdb.db')
# date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# test = SysTest(id=None, name="Test 3", type="HIL/SIL", date_time="2017-02-04 4-26 PM", data_filename="dcsv.txt", 
#                        config_filename="confighilsil.ini", date_created=date)
# repo = sqlSysTestRepository(db)
# repo.add(test)
# for row in repo.getAll():
#     print(row.id, row.name, row.date_time, row.type, row.data_filename, row.config_filename, row.date_created)
# db.close()