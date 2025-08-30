import json
import sqlite3
class SqlGenerator():
    def __init__(self):
        self.con=sqlite3.connect('database.db')
    def generate_query(self,type:,data:str)->str:
        json_dict=json.loads(data)
        return self.tableCreateQuery(json_dict)

    def tableCreateQuery(self,dta:dict)->str:
        qry=""
        qry+=f"CREATE TABLE {dta['name']} ("
        for i,val in enumerate(dta['fields'].keys()):
            qry+=f"{val} {dta['fields'][val]}"
            if i<len(dta['fields'])-1:
                qry+=","
        qry+=");"
        return qry