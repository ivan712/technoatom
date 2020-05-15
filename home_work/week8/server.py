import requests
import re
import collections
import socket
import json

predl = "a on an the in into the for laquo raquo and to of from with is at а на с у или но и в с при за о по так для что как из под от не к"
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

    text_without_space = re.sub(r'\n+',' ',text_response)

    text_without_script = re.sub(r'<script.+?/script>','',text_without_space)

    text_without_style = re.sub(r'<style.+?/style>','',text_without_script)

    text_without_html_tags = re.sub(r'<[^>]+>','',text_without_style)


    words_with_pred = re.findall(r'[a-zа-я]+',text_without_html_tags)

    words = []
    for i in words_with_pred:
        if i not in predl:
            words.append(i)

    popular_words = collections.Counter(words).most_common(10)
    return json.dumps(popular_words)




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

while True:
   # establish a connection
    try:
        clientsocket,addr = serversocket.accept()

    except KeyboardInterrupt:
        print("\nserver close")
        serversocket.close()
        break



    else:
        print("Got a connection from %s" % str(addr))
        website_adress = clientsocket.recv(1024)

        msg = str(words(website_adress.decode('utf-8')))

        clientsocket.send(msg.encode('utf-8'))
        clientsocket.close()
