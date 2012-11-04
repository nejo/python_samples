# -*- coding: utf-8 -*-
from reqresp import *
from TextParser import *
import time
from datetime import datetime
import sendmail

def getPage(n):
	a=Request()
	
	a.setUrl("http://www.infoempleo.com/trabajo/en_barcelona/area-de-empresa_informatica/pagina_"+str(n))
	
	a.perform()
	
	HTML=a.response.getContent()
	
	tp=TextParser()
	tp.setSource("string",HTML)
	
	lista=[]
	
	while tp.readUntil('<tr class="[AB]">'):
		tp.readUntil('<td class="col1"><span>(.*)</span></td>')
		fecha=tp[0][0].split("-")
		
		if 9 == int(fecha[0]) and datetime.today().month == int(fecha[1]):
			tp.readUntil('<td class="col2"><a.*?>(.*)</a></td>')
			oferta=tp[0][0]
			
			tp.readUntil('<td class="col3"><strong><a.*?>(.*)</a></strong></td>')
			empresa=tp[0][0]

			tp.readUntil('<td class="col4"><a.*?>(.*)</a></td>')
			lugar=tp[0][0]

			tp.readUntil('<td class="col5">(.*)</td>')
			inscritos=tp[0][0]

			lista.append([oferta,empresa,lugar,inscritos])

	print "Descargada pagina",n

	return lista


total=[]

while True:
	for i in range(1,5):
		total+=getPage(i)

	message = ""
	if len(total) > 0:
		message += "Las ofertas de hoy son:"
		for oferta,empresa,lugar,inscritos in total:
			message += "\nOferta: "+oferta+"\nEmpresa: "+empresa+"\nLugar: "+lugar+"\nInscritos: "+inscritos+"\n\n"
	else:
		message += "Ninguna oferta hoy"

	print message
	#sendmail.sendMail("neonejo@gmail.com", message)
	
	time.sleep(10)