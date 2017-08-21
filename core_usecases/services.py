'''
Services offered 
'''

''' Command Query Separation '''

class AddRequirement(object):
    def __init__(self, requirementRepo):
        self.repo = requirementRepo
        
    def add(self, requirement):
        '''
        Error handling and enforcement of business rules and also raising events
        '''
        self.repo.add(requirement)
        

class EditRequirement(object):
    def __init__(self, requirementRepo):
        self.repo = requirementRepo
        
    def edit(self, req_id, requirement):
        '''
        Error handling and enforcement of business rules and also raising events
        '''
        self.repo.edit(req_id, requirement)
        
        
class DeleteRequirement(object):
    def __init__(self, requirementRepo):
        self.repo = requirementRepo
        
    def delete(self, req_id):
        '''
        Error handling and enforcement of business rules and also raising events
        '''
        self.repo.delete(req_id)
        

