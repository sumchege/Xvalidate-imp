
'''

Class/Entity for subsystems capture
Author: Sum

'''

class Subsystem(object):
    
    def __init__(self, id, name, date_created):
        """
        Subsystem:     
        id - Unique identifier
        name - Subsystem Name             
        """
        
        self.id = id
        self.name = name
        self.date_created = date_created
    
    def __str__(self, *args, **kwargs):
        return self(self.name)
    
    def getId(self):
        return self.id