from core_domain.Repos.requirementRepository import RequirementRepository
from core_domain.requirement import Requirement

class imRequirementRepository(RequirementRepository):
    
    def __init__(self, db):
        self.db = db
        
    
    def add(self, requirement):
        self.db[requirement.id] = requirement
    
    def edit(self, requirementid, req):
        self.db[requirementid] = req
    
    def delete(self, requirementid):
        self.db.pop(requirementid)
     
    def getAll(self):
        return [Requirement(id=row.id, name=row.name, type=row.type, description=row.description, state=row.state, date_created= row.date_created) 
                for row in list(self.db.values())]
    
    def getbyid(self, requirementid):
        row = self.db[requirementid]
        return Requirement(id=row.id, name=row.name, type=row.type, description=row.description, state=row.state, date_created = row.date_created)


