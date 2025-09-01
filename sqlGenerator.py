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
        name=dta["name"]
        conditions=dta["filters"]
        query_conditions=self.createFilter(conditions)
        safe_query=f"DELETE FROM {name} WHERE {query_conditions}"
        print(safe_query)
        
# This also only executes the queries ,it doesn't return the resulting data
    def tableSelectQuery(self,dta):
        name =dta["name"]
        cols=",".join(k for k in dta["columns"])
        conditions=self.createFilter(dta["filters"])

        safe_query=f"SELECT {cols} FROM {name} WHERE {conditions}"
        print(safe_query)

    def createFilter(self,filter:dict):
        if "conditions" in filter.keys():
            return self.createFilterWithConditions(filter["operator"],filter["conditions"])
        else:
            return self.createFilterWithSingleCondition(filter)


    def createConditional(self,field,operator,value):
        tmp=""
        tmp+=f"{field}"
        tmp+=f" {operator} "
        if isinstance(value,str):
            tmp+=f"\"{value}\""
        else:
            tmp+=f"{value}"
        return tmp
    
    def createFilterWithConditions(self,operator,condition):
        tmp="("
        for i,operation in enumerate(condition):
            if operation["operator"]=="AND" or operation["operator"]=="OR":
                tmp+=self.createFilterWithConditions(condition[i]["operator"],condition[i]["conditions"])
            else:
                tmp+=self.createConditional(operation["field"],operation["operator"],operation["value"])


            if i<len(condition)-1:
                tmp+=f' {operator} '
        return tmp+")"
    
    def createFilterWithSingleCondition(self,condition):
        field=condition["field"]
        operator=condition["operator"]
        value=condition["value"]

        tmp="("
        tmp+=self.createConditional(field,operator,value)
        tmp+=")"
        return tmp

    
