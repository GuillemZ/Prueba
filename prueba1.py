
print('************\n\nMonedas en la lista:\n')
archivo=open('monedas.txt','r')
monedillas=[]
for line in archivo:
    line=line.rstrip()
    monedillas.append(line)
monedillas.sort()
print('\n'.join(map(str, monedillas)))#imprime en orden alfabetico
archivo.close()
print('\n**********\n\nse ha cerrado el archivo\n')  
