import json
import sqlite3
from enums import *

class SqlGenerator():
    def __init__(self):
        self.connection=sqlite3.connect('database.db')
        self.con=self.connection.cursor()

    def executeQuery(self,type:typeOfQuery,data:str):

        # json_dict=json.loads(data)

        match type:
            case typeOfQuery.CREATE:
                qry=self.tableCreateQuery(json_dict)
                self.con.execute(qry)
            case typeOfQuery.INSERT:
                self.tableInsertQuery(json_dict)
            case typeOfQuery.READ:
                return self.tableSelectQuery(data)
            case typeOfQuery.DELETE:
                self.tableDeleteQuery(json_dict)
                

    def tableCreateQuery(self,dta:dict)->str:
        qry=""
        qry+=f'CREATE TABLE {dta["name"]} ('
        for i,val in enumerate(dta["fields"].keys()):
            qry+=f'{val} {dta["fields"][val]}'
            if i<len(dta["fields"])-1:
                qry+=","
        qry+=") STRICT;"
        return qry
    
    def tableInsertQuery(self,dta:dict):
        columns=",".join([i for i in dta["fields"]])
        placeholders=", ".join(["?" for i in range(len(dta["fields"]))])
        values=tuple(dta["values"])
    

        safe_query=f'INSERT INTO {dta["name"]} ({columns}) VALUES ({placeholders})'

        self.connection.execute(safe_query,values)

        self.connection.commit()

        

    def tableDeleteQuery(self,dta:dict):

        pass
    def tableSelectQuery(self,dta):
        return self.createFilter(dta["operator"],dta["conditions"])
        pass

    def createFilter(self,operator,condition):
        tmp="("
        
        # print(condition)
        for i,operation in enumerate(condition):

            if operation["operator"]=="AND" or operation["operator"]=="OR":
                tmp+=self.createFilter(condition[i]["operator"],condition[i]["conditions"])
            else:
            # print("----------------")
            # print(operation)
            # print("----------------")
                tmp+=f" {operation['field']}"
                tmp+=f"{operation['operator']}"
                tmp+=f"{operation['value']}"
            if i<len(condition)-1:
                tmp+=f' {operator} '
            # return sql
        # print(sql)
        return tmp+")"

