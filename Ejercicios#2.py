# RESOLUCIÓN DE EJERCICIO #2

import pandas as pd

datos = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "iq": [105, 98, 110, 95, 100],
    "amigos": [[2, 3], [1], [1, 5], [], [3]],
})


listaIqAmigos = []
listaIqSocial = []

# Impresion de datos inicialmente
print("\nDatos de las personas:\n")
print(datos)

# Se recorren los datos para hacer los calculos necesario y luego agregarlos a las listas correspondientes
for i in range(len(datos)):
 
    fila = datos.iloc[i]
    idAmigos = fila['amigos']
    iqPersona = fila['iq']
    
#    En caso que no tenga amigos
    if len(idAmigos) == 0:  
        promedioIqAmigos = 0

    else:
        listaIq = []

        for idAmigo in idAmigos:
        
            for j in range(len(datos)):
                if datos.iloc[j]['id'] == idAmigo:
                    iqAmigo = datos.iloc[j]['iq']
                    listaIq.append(iqAmigo)
                    break
        
        # Calculo para el promedio
        promedioIqAmigos = sum(listaIq) / len(listaIq)
 

    # Se agrega el promedio del amigo
    listaIqAmigos.append(promedioIqAmigos)
  
#   Si no existe el dato pasa a ser 0
    if promedioIqAmigos == 0:  IqSocialCalc = 0
    
    # En caso contrario se hacen los calculos
    else: IqSocialCalc = 0.7 * iqPersona + 0.3 * promedioIqAmigos
    
    listaIqSocial.append(IqSocialCalc)


datos['iq_amigos'] = listaIqAmigos
datos['iq_social'] = listaIqSocial


# Datos despues de los calculos
print("\nTabla de IQ Social:")
print(datos)
print("\n")