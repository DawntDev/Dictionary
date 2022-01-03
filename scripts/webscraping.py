from bs4 import BeautifulSoup
import requests


#Scraping
Palabra = str(input("Que palabra deseas buscar: "))
url = "https://dem.colmex.mx/Ver/" + Palabra
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
lista_false=['', '', '', '']
lista_false_1 = ['', '', '']
lista_false_2 = ['', '']
lista_false_3 = ['']
lista_false_4 = []
lista_error = [lista_false, lista_false_1, lista_false_2, lista_false_3, lista_false_4]

#Resultado
res_palabra = soup.find_all("span", id="MainContent_lblTitulo")

#Definicion
res_significado_definicion = soup.find_all("span", id="MainContent_repeater_lblDefinicion_0")
res_significado_definicion_1 = soup.find_all("span", id="MainContent_repeater_lblDefinicion_1")
res_significado_definicion_2 = soup.find_all("span", id="MainContent_repeater_lblDefinicion_2")
res_significado_definicion_3 = soup.find_all("span", id="MainContent_repeater_lblDefinicion_3")
res_significado_definicion_4 = soup.find_all("span", id="MainContent_repeater_lblDefinicion_4")


#Ejemplo
res_significado_ejemplo = soup.find_all("span", id="MainContent_repeater_lblEjemplo_0")
res_significado_ejemplo_1 = soup.find_all("span", id="MainContent_repeater_lblEjemplo_1")
res_significado_ejemplo_2 = soup.find_all("span", id="MainContent_repeater_lblEjemplo_2")
res_significado_ejemplo_3 = soup.find_all("span", id="MainContent_repeater_lblEjemplo_3")
res_significado_ejemplo_4 = soup.find_all("span", id="MainContent_repeater_lblEjemplo_4")

#Error
res_error_palabra = soup.find_all("span", id="MainContent_lblTituloPalabrasSimilares")
res_error_sugerencias = soup.find_all("p", class_="p2")

#Palabra
palabra = list()
for i in res_palabra:
    palabra.append(i.text)

#Definicion
definicion = list()
for i in res_significado_definicion:
    definicion.append(i.text)
for i in res_significado_definicion_1:
    definicion.append(i.text)
for i in res_significado_definicion_2:
    definicion.append(i.text)
for i in res_significado_definicion_3:
    definicion.append(i.text)
for i in res_significado_definicion_4:
    definicion.append(i.text)

#Ejemplo
ejemplo = list()
for i in res_significado_ejemplo:
    ejemplo.append(i.text)
for i in res_significado_ejemplo_1:
    ejemplo.append(i.text)
for i in res_significado_ejemplo_2:
    ejemplo.append(i.text)
for i in res_significado_ejemplo_3:
    ejemplo.append(i.text)
for i in res_significado_ejemplo_4:
    ejemplo.append(i.text)
#Error Palabra
error_palabra = list()
for i in res_error_palabra:
    error_palabra.append(i.text)
    
#Sugerencias
sugerencias = list()
for i in res_error_sugerencias:
    sugerencias.append(i.text)

#Contestacion
if palabra == [f'*{Palabra.lower()}*']:
    print("La palabra: ", error_palabra[0], "no se ha encontrado",  "Tal vez lo que estas buscando es: ")
    for i in sugerencias:
        print(i)
else:
    print(palabra[0])
    for i in definicion:
        print(i)
    
    if ejemplo in lista_error:
        print("No hay ejemplos")
    
    else:
        print("Algunos ejemplos son:")
        for i in ejemplo:
            print(i)
        print(ejemplo)

