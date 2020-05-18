from urllib import request
import json
header = {"Host": "www.laohu8.com"}
url = "https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/BILI"
req = request.Request(url = url,headers=header)
io = request.urlopen(req)
html = io.read()
json = json.loads(html)
print("昨收:"+str(json['preClose']))
print("最新:"+str(json['detail']['latestPrice']))