import requests
import re
import collections
import socket
import json
from threading import Thread
import time
import signal
import sys

n_threads = 4

n_done_urls = [0 for _ in range(n_threads)]

results = {}

predl = "a on an the in into the for laquo nbsp quot raquo and moex to of from with is at а на с у или но и в с при за о по так для что как из под от не к"
predl = predl.split()

def words(site):
    try:
        response = requests.get(site)
    except requests.exceptions.InvalidSchema:
        s="incorrect adress"
        return json.dumps(s)
    except :
        s = "cannot connect to website"
        return json.dumps(s)
    response.encoding = 'utf-8'
    text_response = response.text.lower()
    text_without_space = re.sub(r'\n+','//0000//',text_response)
    text_without_script = re.sub(r'<script.+?/script>','',text_without_space)
    text_without_style = re.sub(r'<style.+?/style>','',text_without_script)
    text_without_html_tags = re.sub(r'<[^>]+>','',text_without_style)
    structuring_text = re.sub(r'&quot|&nbsp','',re.sub(r'//0000//','\n',text_without_html_tags))
    return structuring_text



# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

port_num = 8999
port_min_num = port_num + 1
port_max_num = port_num + n_threads

def port_():
    global port_num
    if port_num == port_max_num:
        port_num = port_min_num
        return port_num

    port_num += 1
    return port_num



def make_worker(p):
    global n_done_urls
    serversocket_w = socket.socket(
    	        socket.AF_INET, socket.SOCK_STREAM)
    host_w = socket.gethostname()
    port_w = p
    serversocket_w.bind((host_w, port_w))
    serversocket_w.listen(5)

    while True:
       # establish a connection
        clientsocket_w,addr = serversocket_w.accept()
        website_adress = clientsocket_w.recv(1024)
        print(f'worker address {addr} with port {port_w}')
        url = website_adress.decode('utf-8')
        print(url)
        f=open('res.txt','a')
        f.write(url)
        f.write('\n')
        f.write('----------------------------------------\n')
        f.write(words(url))
        f.write('----------------------------------------\n')
        f.close()
        clientsocket_w.close()
        n_done_urls[port_w-port_min_num]+=1
        #time.sleep(20)


def main_thread():
    while True:
       # establish a connection
        clientsocket,addr = serversocket.accept()
        website_adress = clientsocket.recv(1024)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port_wor = port_()
        try:
            s.connect((host, port_wor))
        except ConnectionRefusedError:
            print("Cannot connect to server")
        s.send(website_adress)
        #website_adress = clientsocket.recv(1024)
        clientsocket.close()
            #time.sleep(10)

m_thread = Thread(target=main_thread,args=(),daemon=True)
threads = [Thread(target=make_worker,args=(i,),daemon=True) for i in range (port_min_num,port_max_num+1)]

def signal_handler(signal_num,frame):
    print('This is hello from signal')
    print()
    for i in range(n_threads):
        print(f'Thread {i+1} have done {n_done_urls[i]} urls')
    print(f'In general master-worker have done {sum(n_done_urls)} urls')
    serversocket.close()

    sys.exit(0)
signal.signal(signal.SIGUSR1,signal_handler)


m_thread.start()
for i in threads:
    i.start()

m_thread.join()
for i in threads:
    i.join()
