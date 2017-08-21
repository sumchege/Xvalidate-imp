
'''

Class/Entity for test objective capture
Author: Sum

'''


class TestObjective(object):
    
    def __init__(self, id, test, objective, req_trace, date_created):
        """
        Requirement:     
        id - test Unique identifier
        test - The test reference in question
        objective - objective statement
        req_trace - Requirement being validated by the test
                        
        """
        
        self.id = id
        self.test = test
        self.objective = objective
        self.req_trace = req_trace
        self.date_created = date_created

        
    
    def __str__(self, *args, **kwargs):
        return self.objective_text
    
    def getId(self):
        return self.id