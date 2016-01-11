import sys, time, os,re
import smtplib
import plotly.plotly as py
from plotly import tools
import datetime
from socket import *
from thread import *

MY_PORT = 50043
BUFSIZE = 1024

def main():
    if len(sys.argv) < 2:
        usage()
    if sys.argv[1] == '-s':
        server()
    else:
        usage()


def usage():
    sys.stdout = sys.stderr
    print 'use:python server.py -s'
    sys.exit(2)


def server():

    port = MY_PORT
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('72.19.120.24', port)) #host ip address
    s.listen(2)
    print 'Server ready...'
    while 1:
        conn, (host, remoteport) = s.accept()
        start_new_thread(clientthread,(conn,))	
    conn.send('OK\n')
    conn.close()



def clientthread(conn):
	#plotly signin and setup
	py.sign_in('plotly_username','6yk748kwqh')
	
	url=py.plot([{'x':[],'y':[],'type':'scatter','stream':{'token':'hxkaxe7wkj','maxpoints':200}}],filename='Signal Level')
	url2=py.plot([{'x':[],'y':[],'type':'scatter','stream': {'token':'zivvy1rznz','maxpoints': 200}}], filename='Bit Rate')
	url3=py.plot([{'x':[],'y':[],'type':'scatter','stream':{'token':'0ul0f7foyr','maxpoints':200}}],filename='Temperature')
	url4=py.plot([{'x':[],'y':[],'type':'scatter','stream':{'token':'7yby2x1sd0','maxpoints':200}}],filename='Humidity')
	url5=py.plot([{'x':[],'y':[],'type':'scatter','stream':{'token':'halsmdw2gu','maxpoints':200}}],filename='Throughput')
	print url2,url3,url4,url5

	stream1 = py.Stream('hxkaxe7wkj')
	stream2 = py.Stream('zivvy1rznz')
	stream3 = py.Stream('0ul0f7foyr')
	stream4 = py.Stream('7yby2x1sd0')
	stream5 = py.Stream('halsmdw2gu')
	stream1.open()
        stream2.open()
	stream3.open()
	stream4.open()
	stream5.open()
		
	#Email setup
  	mail = smtplib.SMTP('smtp.gmail.com',587)
	print "entered the thread"
    	mail.ehlo()
        mail.starttls()
	print "started starttls"
        mail.login('sender_email@gmail.com','sender_password')
	while 1:
            data  = conn.recv(BUFSIZE)   
	    if not data:
                conn.send('OK\n')
		break
	    
	    number=(re.findall(r"[-+]?\d*\.\d+|\d+",data)) # splits a string into floats
 
	    
	    stream1.write({'x':datetime.datetime.now(),'y':number[8]})
	    stream2.write({'x':datetime.datetime.now(),'y':number[12]})
	    stream3.write({'x':datetime.datetime.now(),'y':number[15]})
	    stream4.write({'x':datetime.datetime.now(),'y':number[16]})
      stream5.write({'x':datetime.datetime.now(),'y':number[17]})
	    
	    #time.sleep(15) #to sepcify how frequently to receive a email to a user
	
	    #Email notifications to the users
      mail.sendmail('sender_email@gmail.com','receiver_email@umass.edu',data+'\n'+"Signal level:"+url+'\n'+"Bitrate:"+url2+'\n'+"Temperature:"+url3+'\n'+"Humidity:"+url4+'\n'+"Throughput:"+url5)
      stream1.close()
      stream2.close()
      stream3.close()
      stream4.close()
      stream5.close()
      conn.close()
main()
