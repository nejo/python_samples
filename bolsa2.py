from reqresp import *
import re

def vigilaAcciones(lista):

	a=Request( )        # Creamos la peticion
	a.setUrl("http://www.bolsamadrid.es/esp/mercados/acciones/accind1_1.htm")   #Url de la bolsa espanyola
	
	a.perform()
	
	HTML=a.response.getContent()       #Obtenemos el HTML
	
	results=re.findall("<TR align=right.*</TD></TR>",HTML,re.M)    #Buscamos las lineas que contienen los datos
									# re.M (es un flag para las regexp, significa 
									# que la entrada es multilines, contiene retornos de carro
	
	acciones={}        # Creamos diccionario que contendra los datos
	
	for i in results:
		a=re.findall("([A-Za-z0-9\. ]+)</A></TD><TD>([0-9,]+)",i)    # Extraemos el nombre de la empresa y el valor en bolsa
	
		empresa=a[0][0].strip()                    # Limpiamos el nombre
		valor=float(a[0][1].replace(",","."))      # Convertimos el valor de bolsa a float (sustituyendo antes las , por .
	
		acciones[empresa]=valor                    # Rellenamos el diccionario

	for i,j in lista:
		try:
			if acciones[i]<j:
				print "Compra",i,"!!!",acciones[i],"<",j
		except:
			pass

vigilaAcciones([["IBERIA",3],["ACCIONA",70]])
