from sqlGenerator import SqlGenerator
from enums import *
sl=SqlGenerator()
res=sl.executeQuery(typeOfQuery.CREATE,"{\"name\":\"test\",\"fields\":{\"id\":\"int\",\"name\":\"text not null\"}}")
