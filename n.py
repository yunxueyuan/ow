import requests
import time


url='https://learnreport.xiaoeknow.com/v1/learnRecord/pushData'
headers={
'Host': 'learnreport.xiaoeknow.com',
'Connection': 'keep-alive',
'Content-Length': '433',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
'Accept': 'application/json, text/plain, */*',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Requested-With': 'XMLHttpRequest',
'sec-ch-ua-mobile': '?0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
'sec-ch-ua-platform': "Windows",
'Origin': 'https://app3z0bz5gy7466.h5.xiaoeknow.com',
'Sec-Fetch-Site': 'same-site',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://app3z0bz5gy7466.h5.xiaoeknow.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

for i in range(1800):
    time.sleep(10.1)
    millis = int(round(time.time() * 1000))
    data='channel_id=07404dc6-bedb-11ec-9673-52540014416d&app_id=app3z0bz5Gy7466&user_id=u_625cfb613fa0c_zkB5dNxiva&resource_id=l_6083fde1e4b0d4eb0394903b&product_id=&agent_type=3&content_app_id=&resource_type=4&display_state=0&is_try=0&is_first=0&visit=0&progress=0&is_play=1&live_type=2&live_state=0&alive_state=3&org_learn_progress=&eventName=autoDot&version=1.5.10&packet_number=4&client_time=%d&time_interval=10&report_rate=10000'%(millis)
    x = requests.post(url, data = data, headers=headers)
    print(x.text)

 
