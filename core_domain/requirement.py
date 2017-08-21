
'''

Class/Entity for requirements capture
Author: Sum

'''

class Requirement(object):
    
    def __init__(self, id, name, type, description, state, date_created):
        """
        Requirement:     
        name - Requirement Name 
        type - Requirement type eg functional, non-functional
        description - Text describing the requirement
        state - tracks the State of the requirement 0-Not fullfiled, 1-Halfway met, 2-Fully met 
                        
        """
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.state = state
        self.date_created = date_created
        
    
    def __str__(self, *args, **kwargs):
        return self(self.name)
    