#from http import client
from socket import *
import datetime
import time
import sys

serverName = '127.0.0.1'
serverPort = 9999

clientSocket = socket(AF_INET,SOCK_STREAM)
ping = "ping"

print("Date of sending request by client is : " + str(datetime.datetime.now()))

start_time=time.time()