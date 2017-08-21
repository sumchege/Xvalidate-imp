import unittest
from core_domain.requirement import Requirement
from infrastructure.MockdB.inMemdb import imRequirementRepository

# from core_domain.component import Component
# from core_domain.subsystem import Subsystem
# from core_domain.manufacturer import Manufacturer
# from core_domain.systest import SysTest
# from core_domain.test_objective import TestObjective

from datetime import datetime


'''-----------------------------------------------------------------------------------------
------------------------------ Domain entity unit tests ---------------------------------'''


class testRequirementRepository(unittest.TestCase):
    
    def setUp(self):
        self.db = {}
        self.repo = imRequirementRepository(self.db)
    

    def test_save(self):
        
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        req = Requirement(id=1, name="Landing gear", type="Functional", 
                                  description="The landing shall deploy in 5 seconds upon trigger", state=0, date_created=date)
        req1 = Requirement(id=5, name="Landing gear", type="Functional", 
                                  description="The landing shall deploy in 5 seconds upon trigger", state=0, date_created=date)
        self.repo.add(req)
        self.repo.add(req1)
        
        element = self.repo.getAll()
        assert len(element) == 2
        element = self.repo.getbyid(1)
        
        self.assertEqual(element.id, req.id)      
    
    def test_edit(self):
        date = datetime.datetime.now()
        req = Requirement(id=1, name="Landing gear", type="Functional", 
                                  description="The landing shall deploy in 5 seconds upon trigger", state=0, date_created=date)
        
        req2 = Requirement(id=1, name="Landing gear", type="Functional", 
                                  description="The landing shall deploy in 5 seconds upon trigger", state=1, date_created=date)
        
        self.repo.add(req)
        self.repo.edit(1, req2)
        
        assert len(self.repo.getAll()) == 1
        assert self.repo.getbyid(1).state == 1


#         
#         
#         assert req.id == 1
#         assert req.name == "Landing gear"
#         assert req.type == "Functional"
#         assert req.description == "The landing shall deploy in 5 seconds upon trigger"
#         assert req.state == 0
#     
#     def test_component(self):
#         comp = Component(id=1, name="Landing gear", belongsto="Mechanical Body", 
#                          description="Enables the plane to land on a runway", manufacturer=2)
#         
#         assert comp.id == 1
#         assert comp.name == "Landing gear"
#         assert comp.belongsto == "Mechanical Body" 
#         assert comp.description == "Enables the plane to land on a runway"
#         assert comp.manufacturer == 2
#         
#     def test_subsystem(self):
#         sub = Subsystem(id=2, name="Communication")
#         
#         assert sub.id == 2
#         assert sub.name == "Communication"
#         
#     def test_manufacturer(self):
#         man = Manufacturer(id=2, name="Pipeman", phone="222 222 222", 
#                            email="sales@pipeman.com", website="www.pipeman.com", country="Kenya")
#         
#         assert man.id == 2
#         assert man.name == "Pipeman"
#         assert man.phone == "222 222 222"
#         assert man.email == "sales@pipeman.com"
#         assert man.website == "www.pipeman.com"
#         assert man.country == "Kenya"
#         
#     def test_systest(self):
#         test = SysTest(id=1, datetime="2017-05-04 4-26 PM", datafilename="csv.txt", 
#                        configfilename="config.ini", ttype=2)
#         
#         assert test.id == 1
#         assert test.datetime == "2017-05-04 4-26 PM"
#         assert test.datafilename == "csv.txt"
#         assert test.configfilename == "config.ini"
#         assert test.ttype == 2
#     
#     def test_testObjective(self):
#         obj = TestObjective(1, 1, "To test effectiveness of the landing gear", 1)
#         
#         assert obj.id == 1
#         assert obj.testid == 1
#         assert obj.objective_text == "To test effectiveness of the landing gear"
#         assert obj.related_requirement == 1
#         
#         
    