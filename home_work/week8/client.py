import socket
import json
import sys
import time
import threading

urls = ['ht://yandex.ru/','https://python-scripts.com/json','https://python.hotexamples.com/ru/examples/pyquery/PyQuery/-/python-pyquery-class-examples.html','https://technoatom.mail.ru/curriculum/program/lesson/13156/','https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string']
urls = urls*10
def response_func(urls):
    for i in urls:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 9999
        try:
            s.connect((host, port))
        except ConnectionRefusedError:
            print("Cannot connect to server")
            return
        s.send(i.encode('utf-8'))
        time.sleep(1.01)
        # Receive no more than 1024 bytes
    s.close()

response_func(urls)
