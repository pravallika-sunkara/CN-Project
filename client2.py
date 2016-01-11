mport Adafruit_DHT
import sys, time, os
import socket
from socket import *
from thread import *

MY_PORT = 50043
BUFSIZE = 1024

def main():
    if len(sys.argv) < 2:
        usage()
    if sys.argv[1] == '-c':
        client2()
    else:
        usage()


def usage():
    sys.stdout = sys.stderr
    print 'python client2.py -c serveraddress'
    sys.exit(2)


def client2():
    if len(sys.argv) < 3:
        usage()
    os.system("sudo iwconfig wlan0 | grep 'Signal level' > temp1.txt")
    with open('temp1.txt') as f:
        for line in f:
                date=time.strftime("%c")
                l = '\n' +'Room2 : ' +'\t'+date+'\n' +line.strip()
    os.system("sudo iwconfig wlan0 | grep 'Bit Rate' > temp1.txt")
    with open('temp1.txt') as f:
        for line in f:
                l =l +'\n'+ line.strip()
    sensor=Adafruit_DHT.DHT11
    pin=4

    host = sys.argv[2]
    port = MY_PORT
    t1 = time.time()
    s = socket(AF_INET, SOCK_STREAM)
    t2 = time.time()
    s.connect((host, port))
    t3 = time.time()
    i = 0
    while i < 30:
        #time.sleep(5)
        humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
        if humidity is not None and temperature is not None:

        l =l+'\n'+'Temperature:'+str(temperature)+'C'+'\t '+'Humidity:'+str(humidity)+'%'
                print "Temperature:",temperature,"Humidity:",humidity
        else:
                print "Failed to get reading. Try agian!"
                sys.exit(1)

        i = i+1
        t4 = time.time()
        length = len(l) +30
        #print length
        t = round((length*8)/(t4-t1),3)
        l =l + '\nThroughput :' + str(t) + ' bits/sec'+'\n'
        s.send(l)
        if(i>0):
                t1 = t4
                os.system("sudo iwconfig wlan0 | grep 'Signal level' > temp1.txt")

                with open('temp1.txt') as f:
                        for line in f:
                                l ='\n' + 'Room2 : '+time.strftime("%c")+'\n' +line.strip()
                os.system("sudo iwconfig wlan0 | grep 'Bit Rate' > temp1.txt")
                with open('temp1.txt') as f:
                with open('temp1.txt') as f:
                        for line in f:
                                l =l +'\n'+ line.strip()
    s.shutdown(1) # Send EOF
    t5 = time.time()
    data = s.recv(BUFSIZE)
    t6 = time.time()
    print data
    #print 'Latency:', round(t5-t1,4),"mseconds"
    #print 'Throughput:', round((BUFSIZE*0.001) / (t6-t1), 3),"bits/sec"

main()
