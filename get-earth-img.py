import requests
import json
import re
import os


url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json?uid=1495684555889"
#023000_0_0.png格林威治时间
imgsrc = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/thumbnail/550/%s/%s/%s/%s00_0_0.png"
r = requests.get(url=url)
data = json.loads(r.text)
rr = re.compile(r'\d+')
res = rr.findall(data['file'])
print("start")
date = res[1]
time = res[2]
dl = imgsrc % (date[:4], date[4:6], date[6:9], time)
filename = "%s00_0_0.png" % (time)
img = requests.get(dl)
f = open("cache/"+filename,"wb")
print("open file")
f.write(img.content)
print("write file")
bg = open("bg/bg.png","wb")
print("open file")
bg.write(img.content)
print("write file")
print("OK")
print(dl)
os.system("set-bg.vbe")
