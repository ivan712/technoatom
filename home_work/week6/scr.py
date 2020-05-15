import requests
import json

def log_auth(email):
    datas = {'p':'resplash','email':email,'split':'s796s','r':'https://mail.ru/','pgid':'k9mtiyp0.knk'}
    url = 'https://xray.mail.ru/batch?p=resplash&email=allalala%40list.ru&split=s796s&r=https%3A%2F%2Fmail.ru%2F&pgid=k9mtiyp0.knk'
    s = requests.Session()
    r = s.post(url,data = datas)
    return json.dumps(r.text)
if __name__=="__main__":
    a=str(input('vv email:'))
    print(json.loads(log_auth(a)))
