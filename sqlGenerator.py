import json
import sqlite3
from enums import *

class SqlGenerator():
    def __init__(self):
        self.con=sqlite3.connect('database.db')
        self.cur=self.con.cursor()

    def executeQuery(self,type:typeOfQuery,data:str):

        json_dict=json.loads(data)

        match type:
            case typeOfQuery.CREATE:
                qry=self.tableCreateQuery(json_dict)
                self.cur.execute(qry)
                print("success")
            case typeOfQuery.INSERT:
                self.tableInsertQuery()
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
        pass

    def tableDeleteQuery(self,dta:dict):
        pass
    def tableSelectQuery(self,dta:dict):
        pass

