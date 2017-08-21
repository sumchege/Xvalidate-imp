import unittest
from core_domain.requirement import Requirement
from core_domain.component import Component
from core_domain.subsystem import Subsystem
from core_domain.manufacturer import Manufacturer
from core_domain.systest import SysTest
from core_domain.test_objective import TestObjective
import datetime


'''-----------------------------------------------------------------------------------------
------------------------------ Domain entity unit tests ---------------------------------'''


class testCore(unittest.TestCase):

    def test_requirement(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        req = Requirement(id=1, name="Landing gear", type="Functional", 
                                  description="The landing shall deploy in 5 seconds upon trigger", state=0, date_created=date)
        assert req.id == 1
        assert req.name == "Landing gear"
        assert req.type == "Functional"
        assert req.description == "The landing shall deploy in 5 seconds upon trigger"
        assert req.state == 0
        assert req.date_created == date
        
    
    def test_component(self):
        
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comp = Component(id=1, name="Landing gear", category="Mechanical Body", 
                         description="Enables the plane to land on a runway", manufacturer=2, date_created=date)
        
       
        assert comp.id == 1
        assert comp.name == "Landing gear"
        assert comp.category == "Mechanical Body" 
        assert comp.description == "Enables the plane to land on a runway"
        assert comp.manufacturer == 2
        assert comp.date_created == date
        
    def test_subsystem(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sub = Subsystem(id=2, name="Communication", date_created=date)
        
        assert sub.id == 2
        assert sub.name == "Communication"
        assert sub.date_created == date
        
    def test_manufacturer(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        man = Manufacturer(id=2, name="Pipeman", phone="222 222 222", 
                           email="sales@pipeman.com", web="www.pipeman.com", country="Kenya", date_created=date)
        
        assert man.id == 2
        assert man.name == "Pipeman"
        assert man.phone == "222 222 222"
        assert man.email == "sales@pipeman.com"
        assert man.web == "www.pipeman.com"
        assert man.country == "Kenya"
        assert man.date_created == date
        
    def test_systest(self):
        
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        test = SysTest(id=1, name="Test 1", type="Real", date_time="2017-05-04 4-26 PM", data_filename="csv.txt", 
                       config_filename="config.ini", date_created=date)
        
        assert test.id == 1
        assert test.name == "Test 1"
        assert test.date_time == "2017-05-04 4-26 PM"
        assert test.data_filename == "csv.txt"
        assert test.config_filename == "config.ini"
        assert test.type == "Real"
        assert test.date_created == date
    
    def test_testObjective(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        obj = TestObjective(id=1, objective="To test effectiveness of the landing gear", test=1, req_trace=1, date_created=date)
        
        assert obj.id == 1
        assert obj.test == 1
        assert obj.objective == "To test effectiveness of the landing gear"
        assert obj.req_trace == 1
        assert obj.date_created == date
        
        
        
'''-----------------------------------------------------------------------------------------
------------------------------ Entity Repos unit tests ---------------------------------'''


    