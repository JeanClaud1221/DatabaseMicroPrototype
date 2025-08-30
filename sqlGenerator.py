import json
import sqlite3
from enums import *

class SqlGenerator():
    def __init__(self):
        self.connection=sqlite3.connect('database.db')
        self.con=self.connection.cursor()

    def executeQuery(self,type:typeOfQuery,data:str):

        json_dict=json.loads(data)

        match type:
            case typeOfQuery.CREATE:
                qry=self.tableCreateQuery(json_dict)
                self.con.execute(qry)
                print("success")
            case typeOfQuery.INSERT:
                self.tableInsertQuery(json_dict)
            case typeOfQuery.READ:
                self.tableSelectQuery()
            case typeOfQuery.DELETE:
                self.tableDeleteQuery()
                

    def tableCreateQuery(self,dta:dict)->str:
        qry=""
        qry+=f'CREATE TABLE {dta["name"]} ('
        for i,val in enumerate(dta["fields"].keys()):
            qry+=f'{val} {dta["fields"][val]}'
            if i<len(dta["fields"])-1:
                qry+=","
        qry+=");"
        return qry
    
    def tableInsertQuery(self,dta:dict):
        columns=",".join([i for i in dta["fields"]])
        placeholders=", ".join(["?" for i in range(len(dta["fields"]))])
        values=tuple(dta["values"])
    

        safe_query=f'INSERT INTO {dta["name"]} ({columns}) VALUES ({placeholders})'

        self.con.execute(safe_query,values)
        self.connection.commit()

        
        pass

    def tableDeleteQuery(self,dta:dict):
        pass
    def tableSelectQuery(self,dta:dict):
        pass

