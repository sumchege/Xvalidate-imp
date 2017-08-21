from core_domain.Repos.test_objectiveRepository import TestObjectiveRepository
import sqlite3
from core_domain.test_objective import TestObjective


                                 
class sqlTestObjectiveRepository(TestObjectiveRepository):
    
    def __init__(self, db):
        self.db = db
        
        
    
    def add(self, objective):
        cursor = self.db.cursor()
        sql = '''INSERT INTO TESTOBJECTIVE(objective, test, req_trace, date_created) VALUES(?, ?, ?, ?)'''
        params = (objective.objective, objective.test, objective.req_trace,
                  objective.date_created)
        
        cursor.execute(sql, params)
        self.db.commit()

    
    def edit(self, objective_id, objective):
        cursor = self.db.cursor()
        sql = '''UPDATE TESTOBJECTIVE SET objective=?, test =?, req_trace=? WHERE id=?'''
        params = (objective.objective, objective.test, objective.req_trace, objective_id)
        cursor.execute(sql, params)
        self.db.commit()
        

    
    def delete(self, objective_id):
        cursor = self.db.cursor()
        sql = '''DELETE FROM TESTOBJECTIVE WHERE id=?'''
        params = (objective_id, )
        cursor.execute(sql, params)
        self.db.commit()

    
    def getAll(self):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, objective, test, req_trace, date_created FROM TESTOBJECTIVE'''
        rows = [TestObjective(id=row['id'], objective=row['objective'], test=row['test'], req_trace=row['req_trace'], date_created=row['date_created']) for row in cursor.execute(sql).fetchall()]
        return rows
        

    
    def getby_id(self, objective_id):
        db.row_factory = sqlite3.Row
        cursor = self.db.cursor()
        sql = '''SELECT id, objective, test, req_trace, date_created FROM TESTOBJECTIVE WHERE id = ?'''
        params = (objective_id, )
        rows = [TestObjective(id=row['id'], objective=row['objective'], test=row['test'], req_trace=row['req_trace'], date_created=row['date_created']) for row in cursor.execute(sql, params).fetchall()]
        return rows

    
import datetime
db = sqlite3.connect('../db/sysdb.db')
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
obj = TestObjective(id=None, objective="To the stability of the lateral segment", test=2, req_trace=2, date_created=date)
repo = sqlTestObjectiveRepository(db)
# repo.add(obj)
for row in repo.getAll():
    print(row.id, row.objective, row.test, row.req_trace, row.date_created)
db.close()