
'''

Class/Entity for Manufacturers capture
Author: Sum

'''

class Manufacturer(object):
    
    def __init__(self, id, name, phone, email, web, country, date_created):
        """
        Component:     
        id - Unique identifier
        name - Manufacturer Name
        phone - Tel contact
        email
        web site
        Country - country of origin
        
                        
        """
        
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.web = web
        self.country = country
        self.date_created = date_created
        
    
    def __str__(self, *args, **kwargs):
        return self(self.name)
    
    def getId(self):
        return self.id