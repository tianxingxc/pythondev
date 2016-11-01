# !/usr/bin/env python
# -*- coding:utf-8 -*-

import json
from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor

url = "http://localhost:8080/test?wsdl"

# 引入schemas，可不写
# 在出现type ... 无法在http://schemas.xmlsoap.org/soap/encoding/找到等错误下需要引入

imp = Import('http://xml.apache.org/xml-soap')
imp2 = Import('http://schemas.xmlsoap.org/soap/encoding/')
# 命名空间filter
imp.filter.add('http://www.test/web/')

# 一般情况下用这个就可以: 
# client = Client(url) 

client = Client(url, doctor=ImportDoctor(imp,imp2))
print client
result = client.service.get_test_method("test001")
print result
retMap = json.loads(result)
print retMap, type(retMap)