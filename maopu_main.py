import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36', 
'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8', 'Referer': 'http://www.mop.com/register.html', 'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = dict(cookie='mop_uid=15373342036697033; _ms=1537334204729586795; _mc=m-1537334204729471717; read_mop=/www.mop.com/register; _captcha_key=1537334204729471717; Hm_lvt_478a545b1304d1c78ecf8fa7a9ef656f=1537336914; Hm_lpvt_478a545b1304d1c78ecf8fa7a9ef656f=1537336914; mop_log=newindex%7Ctopnav%7Cregister%7C0%7C0%7C0%7C')

for i in range(0,9999,1):
	r = requests.get('http://imagecode.mop.com/captcha/getCaptcha.do', headers=headers,  cookies=cookies, verify=False, timeout=10).content
	print i
	sz = open(str(i)+'.png', 'wb')
	sz.write(r)
	sz.close()
	