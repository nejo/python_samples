import sys

try:
    numlines = int(sys.argv[1])
except:
    print "El parametro introducido no es numerico"
    exit();

j = 0

if len(sys.argv) > 2:
    for i in sys.argv[2:]:
        try:
            f = open(i)
            while j < numlines:
		# , o rstrip() para eliminar uno d los 2 enters, el del print o el del readline()
                print f.readline(),
                j += 1
            f.close()
        except:
            print "error en el archivo:",i
else:
    while numlines:
        a = raw_input()
        print a
        numlines -= 1