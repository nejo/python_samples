from urllib import urlretrieve
from time import sleep

for i in range(1, 100):
	urlretrieve('http://hosted.ifw.es/galerias/09/09/5720909/'+str(i)+'.jpg', 'Ellen/'+str(i)+'.jpg')
	sleep(3)

print "Finalizado correctamente"
