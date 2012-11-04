from reqresp import *
from datetime import datetime
import smtplib
import time

def sendMail(to,msg):
	fromaddr = 'wbpqsp@gmail.com'  
	  
	# Credentials (if needed)  
	username = 'wbpqsp'  
	password = '69642180'  
	  
	# The actual mail send  
	server = smtplib.SMTP('smtp.gmail.com:587')  
	server.ehlo()  
	server.starttls()  
	server.ehlo()  
	server.login(username,password)  
	server.sendmail(fromaddr, to, msg)  
	server.quit()  

while True:
	a=Request()
	a.setUrl("http://www.infoempleo.com/trabajo/en_barcelona/area-de-empresa_informatica")
	
	a.perform()
	
	HTML=a.response.getContent()
	
	tp=TextParser()
	tp.setSource("string",HTML)
	
	lista=[]
	
	dia=datetime.today().day-1
	mes=datetime.today().month
	
	while tp.readUntil("<tr class=\"[AB]\">"):
		tp.readUntil("<td class=\"col1\"><span>([0-9-]+)</span></td>")
		fecha=tp[0][0]
		tp.readUntil("<td class=\"col2\"><a href=\"([^\"]+)\" title=\"([^\"]+)\">")
		link=tp[0][0]
		puesto=tp[0][1]
	
	
		diatmp,mestmp=fecha.split("-")	
		diatmp=int(diatmp)
		mestmp=int(mestmp)
		if dia==diatmp and mes==mestmp:
			lista.append([fecha,link,puesto])

	cad=""
	for i in lista:
		cad+=i[0]+"-"+i[1]+"\n"
	
	if cad:
		sendMail("deepbit@gmail.com",cad)

	time.sleep(86400)

