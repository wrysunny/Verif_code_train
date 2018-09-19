import time
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36', 
'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9'}
t = str(time.time()).strip('.')
for i in range(0,9999,1):
	r = requests.get('http://sso.people.com.cn/util/randChinese?d='+t, headers=headers,   verify=False, timeout=10).content
	print i
	sz = open(str(i)+'.png', 'wb')
	sz.write(r)
	sz.close()
	