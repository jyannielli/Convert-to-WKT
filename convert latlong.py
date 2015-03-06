import math
import csv

# absorbs data lat / long and turns into WKT used below
def latlon2wkt(lat,long) :
    half_circ = 20037508.34
    x = long * half_circ /180
    y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    y = y * half_circ / 180
    return "GEOMETRYCOLLECTION(POINT("+str(x)+" "+str(y)+"))"


# asks the name of the CSV file to read, file must have an entry for latitude, longitude per line, following this format:
# -22.814914,-47.091363
# -22.898138,-47.076776
# ...
# ...
entra = raw_input("\n Enter the name of the CSV file and press <enter> --> ")
arq_cvs = csv.reader(open(entra,'rb'),delimiter=',',quotechar='"')


# generates a list (matrix) to organize data
lista_cvs = list(arq_cvs)

# converts the data
for i in range(0,len(lista_cvs)):
	lista_cvs[i][0] = latlon2wkt(float(lista_cvs[i][0]),float(lista_cvs[i][1]))
	lista_cvs[i].pop(1)


# asks CSV file name to save data in WKT
saida = raw_input("\n Enter the file name to save WKT data and press <enter> --> ")
result = open(saida,'wb')
writer=csv.writer(result,dialect='excel')
headings=writer.writerows(lista_cvs)
result.close()
