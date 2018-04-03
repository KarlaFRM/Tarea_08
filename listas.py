#Autor Karla Fabiola Ramirez Martines - A01746769





#Primera funcion/La acabo de probar en pythontutor y funciona!
def sumarAcumulado(lista):
    suma=0
    nuevaLista=[]
    for dato in lista:
        suma+=dato
        nuevaLista.append(suma)
    return nuevaLista


#Segunda funcion/ Probada en pythontutor ! funciona perfectamente
def recortarLista(lista):
    nuevaLista = []
    acumulador = 0
    for k in lista:
        acumulador += 1
        if acumulador != 1 and acumulador != len(lista):
            nuevaLista.append(k)

    return nuevaLista


#Tercera función <3/la probe dos casos pero necesito probarla mas(por ahora funciona)
def estanOrdenados(lista):
    suma = 0
    primerValor = 0
    for dato in lista:
        if dato > primerValor:
            suma += 1
            primerValor = dato
    if suma == len(lista):
        return "True"
    else:
        return "False"

#Cuarta funcion/Por ahora ni puta idea de como hacerla, ok se podria usar in pero aun no se como utilizarla
def sonAnagramas(lista):



#Quinta funcion/Tiene bastant eproblemas el mayor es como arreglar lo de la suma y hacerlo eficiente
#Nenesita arreglarse
def hayDuplicados(lista):
    def hayDuplicados(lista):
        contador = 0
        valor = 0
        resultado = False
        for dato in lista:
            valor = dato
            for dat in lista:
                if valor != dat:
                    contador += 1

        if contador == (len(lista) - 1):
            resultado = True
        return resultado


#Sexta funcion/no regresa una nueva lista asi que habria que utilizar remove :)
def borrarDuplicados(lista):






def main():








main()
