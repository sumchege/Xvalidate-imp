from core_domain.component import Component
from core_domain.Repos.componentRepository import ComponentRepository

import sqlite3


class sqlComponentRepository(ComponentRepository):
     
    def __init__(self, db):
        self.db = db
         
         
     
    def add(self, component):
        cursor = self.db.cursor()
        sql = '''INSERT INTO component(name, category, description, manufacturer, date_created) VALUES(?, ?, ?, ?, ?)'''
        params = (component.name, component.category, component.description, component.manufacturer, 
                  component.date_created)
         
        cursor.execute(sql, params)
        self.db.commit()
 
     
    def edit(self, component_id, component):
        cursor = self.db.cursor()
        sql = '''UPDATE component SET name=?, category =?, description=?, manufacturer=? WHERE id=?'''
        params = (component.name, component.category, component.description, component.manufacturer, component_id)
        cursor.execute(sql, params)
        self.db.commit()
         
 
     
    def delete(self, component_id):
        cursor = self.db.cursor()
        sql = '''DELETE FROM component WHERE id=?'''
        params = (component_id, )
        cursor.execute(sql, params)
        self.db.commit()
 
     
    def getAll(self):
        self.db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, category, description, manufacturer, date_created FROM component'''
        rows = [Component(id=row['id'], name=row['name'], category=row['category'], description=row['description'], manufacturer=row['manufacturer'], date_created=row['date_created']) for row in cursor.execute(sql).fetchall()]
        return rows
         
 
     
    def getby_id(self, component_id):
        self.db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, category, description, manufacturer, date_created FROM component WHERE id = ?'''
        params = (component_id, )
        rows = [Component(id=row['id'], name=row['name'], category=row['category'], description=row['description'], manufacturer=row['manufacturer'], date_created=row['date_created']) for row in cursor.execute(sql, params).fetchall()]
        return rows
        pass
    
# import datetime
# date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# comp = Component(id=None, name="Can Interface", category=2, 
#                          description="Enable in chip communication in the vehicle", manufacturer=8, date_created=date)
#  
# db = sqlite3.connect('../db/sysdb.db')
#  
# repo = sqlComponentRepository(db)
# repo.add(comp)
#  
# for row in repo.getAll():
#     print(row.id, row.name, row.category, row.description, row.manufacturer, row.date_created)
# db.close()
