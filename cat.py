import sys

if len(sys.argv) == 1:
	while True:
		a = raw_input()
		if a == "":
			exit()
		print a
else:
	for i in sys.argv[1:]:
	    try:
	        f = open(i)
	        for j in f:
	            print j.rstrip()
	        f.close()
	    except:
	        print "Error con fichero "+i
