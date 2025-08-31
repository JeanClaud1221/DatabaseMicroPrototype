import json
import sqlite3
from enums import *

class SqlGenerator():
    def __init__(self):
        self.connection=sqlite3.connect('database.db')
        self.con=self.connection.cursor()

# TODO this only executes the queries and doesnt return anything have update return success or failure and read queries return the actuall data
    def executeQuery(self,type:typeOfQuery,data:str):

        json_dict=json.loads(data)

        match type:
            case typeOfQuery.CREATE:
                qry=self.tableCreateQuery(json_dict)
                self.con.execute(qry)
            case typeOfQuery.INSERT:
                self.tableInsertQuery(json_dict)
            case typeOfQuery.READ:
                self.tableSelectQuery(json_dict)
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
# This also only executes the queries ,it doesn't return the resulting data
    def tableSelectQuery(self,dta):
        name =dta["name"]
        cols=",".join(k for k in dta["columns"])
        conditions=self.createFilterConditions(dta["filters"]["operator"],dta["filters"]["conditions"])

        safe_query=f"SELECT {cols} FROM {name} WHERE {conditions}"

        self.con.execute(safe_query)
        print(self.con.fetchall())

    def createFilterConditions(self,operator,condition):
        tmp="("
        for i,operation in enumerate(condition):

            if operation["operator"]=="AND" or operation["operator"]=="OR":
                tmp+=self.createFilterConditions(condition[i]["operator"],condition[i]["conditions"])
            else:

                tmp+=f"{operation['field']}"
                tmp+=f" {operation['operator']} "
                if isinstance(operation['value'],str):
                    tmp+=f"\"{operation['value']}\""
                else:
                    tmp+=f"{operation['value']}"
            if i<len(condition)-1:
                tmp+=f' {operator} '
        return tmp+")"

