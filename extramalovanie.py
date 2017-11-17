dlzka = int (input ("zadaj dlzku: "))
sirka = int (input ("zadaj sirku: "))
vyska = int (input ("zadaj vysku: "))
litrem2 = int(input ("zadaj litre na m2: "))
celkovom2 = dlzka * vyska + sirka * vyska + dlzka * vyska + sirka * vyska + sirka * dlzka
celkovolitrov = celkovom2 * litrem2
print ("na vymalovanie celej miestnosti potrebujes", celkovolitrov, "litrov farby")
