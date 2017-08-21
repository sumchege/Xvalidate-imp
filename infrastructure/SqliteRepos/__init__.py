'''
Import db name from configs, and expose it to 
 
'''
import sqlite3

import App
from contextlib import contextmanager

db = sqlite3.connect(App.config['DATABASE'])
# @contextmanager
# def connect_db():
#     db = sqlite3.connect(App.config['DATABASE'])
#     try:
#         yield db
#     finally:
#         if db is not None:
#             db.close()
            
            
db.execute("PRAGMA foreign_keys=ON")

component_ddl = '''CREATE TABLE COMPONENT(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    category TEXT NOT NULL,
                                    description TEXT,
                                    manufacturer INTEGER NOT NULL, 
                                    date_created DATETIME NOT NULL,
                                    UNIQUE(name),
                                    FOREIGN KEY(category) REFERENCES SUBSYSTEM(id),
                                    FOREIGN KEY(manufacturer) REFERENCES MANUFACTURER(id)
                                    )'''
                                    
manufacturer_ddl = '''CREATE TABLE MANUFACTURER(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    phone TEXT ,
                                    email TEXT ,
                                    web TEXT ,
                                    country INTEGER NOT NULL DEFAULT(0),
                                    date_created DATETIME NOT NULL,
                                    UNIQUE(name, phone, email, web)
                                    )'''
                                    
requirement_ddl = '''CREATE TABLE REQUIREMENT(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    type TEXT NOT NULL,
                                    description TEXT NOT NULL,
                                    state INTEGER NOT NULL DEFAULT(0),
                                    date_created DATETIME NOT NULL,
                                    UNIQUE(name)
                                    )'''

subsystem_ddl = '''CREATE TABLE SUBSYSTEM(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL  , 
                                date_created DATETIME NOT NULL,
                                UNIQUE(name)
                                )'''
                                
systest_ddl = '''CREATE TABLE SYSTEST(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    date_time DATETIME NOT NULL ,
                                    type TEXT ,
                                    data_filename TEXT ,
                                    config_filename TEXT ,
                                    date_created DATETIME NOT NULL,
                                    UNIQUE(name)
                                    )'''
                                    
testobjective_ddl = '''CREATE TABLE TESTOBJECTIVE(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    objective TEXT NOT NULL,
                                    test INTEGER NOT NULL,
                                    req_trace INTEGER NOT NULL,
                                    date_created DATETIME NOT NULL,
                                    UNIQUE(objective),
                                    FOREIGN KEY(test) REFERENCES SYSTEST(id),
                                    FOREIGN KEY(req_trace) REFERENCES REQUIREMENT(id)
                                  )'''

for statement in [requirement_ddl, component_ddl, manufacturer_ddl, testobjective_ddl, subsystem_ddl, systest_ddl, testobjective_ddl]:
    try:
        db.execute(statement)   
     
    except sqlite3.OperationalError as e:
        print(e)

 
db.close()