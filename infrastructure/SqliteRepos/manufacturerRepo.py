from core_domain.Repos.manufacturerRepository import ManufacturerRepository
from core_domain.manufacturer import Manufacturer
import sqlite3

                                    
                         
class sqlManufacturerRepository(ManufacturerRepository):
    
    def __init__(self, db):
        self.db = db
        
        
    
    def add(self, manufacturer):
        cursor = self.db.cursor()
        sql = '''INSERT INTO manufacturer(name, phone, email, web, country, date_created) VALUES(?, ?, ?, ?, ?, ?)'''
        params = (manufacturer.name, manufacturer.phone, manufacturer.email, manufacturer.web, 
                  manufacturer.country, manufacturer.date_created)
        
        cursor.execute(sql, params)
        self.db.commit()

    
    def edit(self, manufacturer_id, manufacturer):
        cursor = self.db.cursor()
        sql = '''UPDATE manufacturer SET name=?, phone =?, email=?, web=?, country=? WHERE id=?'''
        params = (manufacturer.name, manufacturer.phone, manufacturer.email, manufacturer.web, manufacturer.country, manufacturer.id)
        cursor.execute(sql, params)
        self.db.commit()
        

    
    def delete(self, manufacturer_id):
        cursor = self.db.cursor()
        sql = '''DELETE FROM manufacturer WHERE id=?'''
        params = (manufacturer_id, )
        cursor.execute(sql, params)
        self.db.commit()

    
    def getAll(self):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, phone, email, web, country, date_created FROM manufacturer'''
        rows = [Manufacturer(id=row['id'], name=row['name'], phone=row['phone'], email=row['email'], web=row['web'], country=row['country'], date_created=row['date_created']) for row in cursor.execute(sql).fetchall()]
        return rows
        

    
    def getby_id(self, manufacturer_id):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, phone, email, web, country, date_created FROM manufacturer WHERE id = ?'''
        params = (manufacturer_id, )
        rows = [Manufacturer(id=row['id'], name=row['name'], phone=row['phone'], email=row['email'], web=row['web'], 
                             country=row['country'], date_created=row['date_created']) for row in cursor.execute(sql, params).fetchall()]
        return rows

     
import datetime
  
date = datetime.datetime.now()
man = Manufacturer(id=None, name="Micropilot", phone="888 444 222", 
                           email="sales@micropilot.com", web="www.micropilot.com", country="Canada", date_created=date)

# db = sqlite3.connect('../db/sysdb.db')
# repo = sqlManufacturerRepository(db)
# repo.add(man)
# for row in repo.getAll():
#     print(row.id, row.name, row.phone, row.email, row.web, row.country, row.date_created)
# db.close()