
'''

Class/Entity for testing 
Author: Sum

'''

class SysTest(object):
    
    def __init__(self, name, id, date_time, type, data_filename, config_filename, date_created):
        """
        sysTest:     
        id - test Unique identifier
        date - Date of test
        data_filename - name of CSV file containing test data
        config_filename - filename of the file containing system configuration
        type - Type of test 0 - SIL, 1 - HIL, 2 - Real Field Test
                        
        """
        
        self.id = id
        self.name = name
        self.date_time = date_time
        self.type = type
        self.data_filename = data_filename
        self.config_filename = config_filename
        self.date_created = date_created
        

        
    
    def __str__(self, *args, **kwargs):
        return self(self.datafilename)
    
    def getId(self):
        return self.id