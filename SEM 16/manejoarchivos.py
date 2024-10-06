with open('my_notes.txt', 'w') as archivo:                                                               # cierra automaticamente el archivo despues de escribirlo                                              
    archivo.write('1 Ir de Compras\n2 Ir al Banco a hacer un deposito\n3 Hacer deberes de programacion UEA')       # sobreescribe el contenido del archivo      
with open('my_notes.txt', 'r') as archivo:                                                                # cierra automaticamente el archivo despues de abrirlo  
    lineas= archivo.readlines()                                                                                # guarda en una variable las lineas   
    for l in lineas:                                                                                             # imprimire con for cada linea 
        print(l.replace('\n',' '))                                                                               # quita el enter de \n