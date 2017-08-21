
'''

Class/Entity for components capture
Author: Sum

'''

class Component(object):
    
    def __init__(self, id, name, category, description, manufacturer, date_created):
        """
        Component:     
        id - Unique identifier
        name - Component Name
        category - integer denoting subsytem that the component belongs to
        manufacturer - manufacture id
        description - Text describing the component and its function
        
                        
        """
        
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.manufacturer = manufacturer
        self.date_created = date_created
        
    
    def __str__(self, *args, **kwargs):
        return self(self.name)
    
    def getId(self):
        return self.id