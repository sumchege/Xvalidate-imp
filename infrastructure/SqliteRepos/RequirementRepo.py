from core_domain.Repos.requirementRepository import RequirementRepository
from core_domain.requirement import Requirement
import sqlite3

                           
                                    
class sqlRequirementRepository(RequirementRepository):
    
    def __init__(self, db):
        self.db = db
        
        
    
    def add(self, requirement):
        cursor = self.db.cursor()
        sql = '''INSERT INTO requirement(name, type, description, state, date_created) VALUES(?, ?, ?, ?, ?)'''
        params = (requirement.name, requirement.type, requirement.description, requirement.state, 
                  requirement.date_created)
        
        cursor.execute(sql, params)
        self.db.commit()

    
    def edit(self, requirement_id, req):
        cursor = self.db.cursor()
        sql = '''UPDATE requirement SET name=?, type =?, description=? WHERE id=?'''
        params = (req.name, req.type, req.description, requirement_id)
        cursor.execute(sql, params)
        self.db.commit()
        

    
    def delete(self, requirement_id):
        cursor = self.db.cursor()
        sql = '''DELETE FROM requirement WHERE id=?'''
        params = (requirement_id, )
        cursor.execute(sql, params)
        self.db.commit()

    
    def getAll(self):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, type, description, state, date_created FROM requirement'''
        rows = [Requirement(id=row['id'], name=row['name'], type=row['type'], description=row['description'], state=row['state'], date_created=row['date_created']) for row in cursor.execute(sql).fetchall()]
        return rows
        

    
    def getby_id(self, requirement_id):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, name, type, description, state, date_created FROM requirement WHERE id = ?'''
        params = (requirement_id, )
        rows = [Requirement(id=row['id'], name=row['name'], type=row['type'], description=row['description'], state=row['state'], date_created=row['date_created']) for row in cursor.execute(sql, params).fetchall()]
        return rows

    
# import datetime
# db = sqlite3.connect('../db/sysdb.db')
# req = Requirement(id=None, name="Landing gearfsdfggt", type="Non Functional", 
#                                   description="The landing shall dfghghggjhjeploy in 5 seconds upon trigger", state=0, date_created=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# repo = sqlRequirementRepository(db)
# repo.add(req)
# for row in repo.getAll():
#     print(row.id, row.name, row.type, row.description, row.state, row.date_created)
# db.close()