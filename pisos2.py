from reqresp import *
from TextParser import *

#
# http://www.pisosalaventa.com/listar_contactos_ofertas_compartir.php?pg=0&po=0&pro=9&paso=1
#

def getPage(n):
	a=Request()
	
	a.setUrl("http://www.pisosalaventa.com/listar_contactos_ofertas_compartir.php?pg="+str(n)+"&po=0&pro=9&paso=1")
	
	a.perform()
	
	HTML=a.response.getContent()
	
	tp=TextParser()
	tp.setSource("string",HTML)
	
	lista=[]
	
	while tp.readUntil("<tr class='contenido_tab' onClick='window.location=\"([a-zA-Z0-9\.-]+)\""):
		# Expresion regular mejorada ("<tr class='contenido_tab' onClick='window.location=\"([^\"]+)\""):
		link=tp[0][0]
	
		tp.readUntil("<td class='contenido_tab' align='right'>([0-9]+)</td>")
		precio=int(tp[0][0])
	
		lista.append([link,precio])

	print "Descargada pagina",n

	return lista


total=[]

for i in range(0,10):
	total+=getPage(i)

for link,euros in total:
	if euros<200000:
		print link
