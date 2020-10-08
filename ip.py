import argparse
import requests
import bs4

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, nargs='+')
    
    args = parser.parse_args()
    ips = args.ip
    
    return ips
    
ips = parse()
idx = 1
print("\n")
for ip in ips:
    url = 'http://ip2nation.com/'
    res = requests.post(url, data={'ip' : ip})
    
    res = bs4.BeautifulSoup(res.text, 'html.parser')
    res = res.find('acronym').text
    
    print("["+str(idx)+"] "+ip+"    ==> "+res)
    idx += 1
	
	#python ip.py --ip [ip]