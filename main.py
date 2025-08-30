from sqlGenerator import SqlGenerator
sl=SqlGenerator()
res=sl.generate_query("{\"name\":\"test\",\"fields\":{\"id\":\"int\",\"name\":\"text not null\"}}")
print(res)