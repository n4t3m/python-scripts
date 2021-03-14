import requests
import time
from datetime import datetime

def checkCVS():
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'Referer': 'https://www.cvs.com/immunizations/covid-19-vaccine'
            }
    url = "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.CA.json?vaccineinfo"
    r = requests.get(url, headers=headers)
    try:
        data = r.json()['responsePayloadData']['data']['CA']
        return data
    except:
        print("something went wrong")
        exit(1)

    return -1

def main():
    print("===CVS Vaccine Checker===")
    while True:
        print("Check on " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        data = checkCVS()
        for c in data:
            if c['status'] != "Fully Booked":
                print(c['city'].lower().capitalize())
        print('-----------------------------------------')
        time.sleep(60) 

if __name__ == '__main__':
    main()