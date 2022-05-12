def cliente(informacion:dict)->dict:
    if informacion['edad'] > 18:
        atraccionV = 'X-Treme'
        aptoV = True
        if informacion['primer_ingreso'] == True:
            pass
        else:
            pass
        
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccionV = 'Carros chocones'
        aptoV = True
        
        
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccionV = 'Sillas voladoras'
        aptoV = True
        
        
    else:
        atraccionV = 'N/A'
        totalBoletaV = 'N/A'
        aptoV = False
        
    
        
    dicSalida = {
        'nombre':informacion['nombre'],
        'edad':informacion['edad'],
        'atraccion': atraccionV,
        'apto': aptoV,
        'primer_ingreso':informacion['primer_ingreso']
    }
    return dicSalida
    

# Esto que esta de aquí en adelante NO se sube a imaster
informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez', 
    'edad': 20, 
    'primer_ingreso': True    
}
print(cliente(informacion))