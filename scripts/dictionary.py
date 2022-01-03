import tkinter as tk
from tkinter.constants import CENTER
import pyttsx3
import speech_recognition as sr
from bs4 import BeautifulSoup
import requests

#Voz a Texto
r = sr.Recognizer()


#Voz
engine = pyttsx3.init()
voices = engine.getProperty("voices")
e = 0
for i in range(len(voices)):
    if str(voices[i].name) == "Microsoft Sabina Desktop - Spanish (Mexico)":
        e = i
    else:
        print(voices[i])
print(e)
engine.setProperty("voice", voices[e].id)

#GUI
window=tk.Tk()
window.geometry("964x567")
window.title("Diccionario")
window.config(bg="#EBEBEB")

#Ventana
title=tk.Label(window, text="Diccionario",font="TradeGothic 28", bg="#EBEBEB", justify=CENTER).place(x=434, y=57)

#Barra
barra=tk.Entry(window, font="Arial 12 italic", bg="#EBEBEB",justify=CENTER)
#Funciones
def dictar ():
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            rec = r.recognize_google(audio) 
        barra.delete(0, "end")
        barra.insert(0, rec)
    except:
        engine.say("LO SIENTO NO TE HE ESCUCHADO")
        engine.runAndWait()      

def deletrear():
    ent_del = barra.get()
    word=str()
    for i in ent_del:
        engine.say(i.upper())
        engine.runAndWait()
        word= word + i
        if i == (" "):
            engine.say(word.upper())
            word = str()
    engine.say(word.upper())
    engine.runAndWait()
    barra.delete(0, "end")

def silabas():
    #Pantalla 2 Config
    window_silabas = tk.Tk()
    window_silabas.geometry("435x480")
    window_silabas.title("Silabas")
    window_silabas.config(bg="#EBEBEB")

    #Lista botones
    b_list = ["ba", "be", "bi", "bo", "bu", "bla", "ble", "bli", "blo", "blu", "bra", "bre", "bri", "bro", "bru"]
    c_list = ["ca", "ce", "ci", "co", "cu", "cha", "che", "chi", "cho", "chu", "cla", "cle", "cli", "clo", "clu", "cra", "cre", "cri", "cro", "cru"]
    d_list = ["da", "de", "di", "do", "du", "dra", "dre", "dri", "dro", "dru"]
    f_list = ["fa", "fe", "fi", "fo", "fu", "fla", "fle", "fli", "flo", "flu", "fra", "fre", "fri", "fro", "fru"] 
    g_list = ["ga", "ge", "gi", "go", "gu", "gla", "gle", "gli", "glo", "glu", "gra", "gre", "gri", "gro", "gru", "gua", "gue", "gui", "guo"]
    h_list = ["ha", "he", "hi", "ho", "hu"]
    j_list = ["ja", "je", "ji", "jo", "ju"]
    k_list = ["ka", "ke", "ki", "ko", "ku"]
    l_list = ["la", "le", "li", "lo", "lu", "lla", "lle", "lli", "llo", "llu"]
    m_list = ["ma", "me", "mi", "mo", "mu"]
    n_list = ["na", "ne", "ni", "no", "nu"]
    ñ_list = ["ña", "ñe", "ñi", "ño", "ñu"]
    p_list = ["pa", "pe", "pi", "po", "pu", "pla", "ple", "pli", "plo", "plu", "pra", "pre", "pri", "pro", "pru"]
    q_list = ["que", "qui"]
    r_list = ["ra", "re", "ri", "ro", "ru", "rra", "rre", "rri", "rro", "rru"]
    s_list = ["sa", "se", "si", "so", "su"]
    t_list = ["ta", "te", "ti", "to", "tu", "tla", "tle", "tli", "tlo", "tlu", "tra", "tre", "tri", "tro", "tru"]
    v_list = ["va", "ve", "vi", "vo", "vu"]
    w_list = ["wa", "we", "wi", "wo", "wu"]
    x_list = ["xa", "xe", "xi", "xo", "xu"]
    y_list = ["ya", "ye", "yi", "yo", "yu"]
    z_list = ["za", "ze", "zi", "zo", "zu"]

    #Say lista
    b_say = ["ba", "bé", "bí", "bo", "bu", "bla", "blé", "blí", "bló", "blu", "bra", "bré", "brí", "bró", "bru"]
    c_say = ["ca", "cé", "cí", "có", "cú", "chá", "ché", "chí", "chó", "chú", "clá", "clé", "clí", "cló", "clú", "crá", "cré", "crí", "cró", "cru"]
    d_say = ["da", "dé", "dí", "dó", "dú", "drá", "dré", "drí", "dró", "drú"]
    f_say = ["fa", "fé", "fí", "fó", "fú", "flá", "flé", "flí", "fló", "flú", "frá", "fré", "frí", "fró", "fru"] 
    g_say = ["ga", "gé", "gí", "gó", "gú", "glá", "glé", "glí", "gló", "glú", "grá", "gré", "grí", "gro", "gru", "guá", "gué", "guí", "guó"]
    h_say = ["ha", "hé", "hí", "hó", "hú"]
    j_say = ["ja", "jé", "jí", "jó", "jú"]
    k_say = ["ka", "ké", "kí", "kó", "kú"]
    l_say = ["la", "lé", "lí", "ló", "lú", "llá", "llé", "llí", "lló", "llú"]
    m_say = ["ma", "mé", "mí", "mó", "mú"]
    n_say = ["ná", "né", "ní", "nó", "nú"]
    ñ_say = ["ña", "ñé", "ñí", "ñó", "ñú"]
    p_say = ["pa", "pé", "pí", "pó", "pú", "plá", "plé", "plí", "pló", "plú", "prá", "pré", "prí", "pró", "prú"]
    q_say = ["qué", "quí"]
    r_say = ["hrá", "hré", "hrí", "hró", "hrú", "rrá", "rré", "rrí", "rró", "rrú"]
    s_say = ["sá", "sé", "sí", "só", "sú"]
    t_say = ["ta", "té", "tí", "tó", "tú", "tlá", "tlé", "tlí", "tló", "tlú", "trá", "tré", "trí", "tró", "trú"]
    v_say = ["va", "vé", "ví", "vó", "vú"]
    w_say = ["wa", "we", "wí", "wó", "wu"]
    x_say = ["xá", "xé", "xí", "xó", "xú"]
    y_say = ["ya", "yé", "yí", "yó", "yú"]
    z_say = ["zá", "zé", "zí", "zó", "zú"]

    class BL:

        def __init__(self, texto, X, Y, lista, say_lista):
            self.lista = lista
            self.say_lista = say_lista

            def say(i):
                engine.say(f"{say_lista[i]}")
                engine.runAndWait()
                

            def ls ():
                #Ventana de Silabas
                window_ls = tk.Tk()
                window_ls.geometry("760x280")
                window_ls.title(texto)
                XiF = 50 
                XiF_1 = 50
                XiF_2 = 50
                XiF_3 =50
                try:
                    for i in range(0, len(lista)):
                        if i <= 4:
                            if i == 0:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(0)).place(x=XiF, y=40, width=120, height=40)
                            elif i == 1:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(1)).place(x=XiF, y=40, width=120, height=40)
                            elif i == 2:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(2)).place(x=XiF, y=40, width=120, height=40)
                            elif i == 3:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(3)).place(x=XiF, y=40, width=120, height=40)
                            elif i == 4:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(4)).place(x=XiF, y=40, width=120, height=40)
                            XiF = XiF + 135  
                        elif i <= 9:
                            if i == 5:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(5)).place(x=XiF_1, y=90, width=120, height=40)
                            elif i == 6:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(6)).place(x=XiF_1, y=90, width=120, height=40)
                            elif i == 7:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(7)).place(x=XiF_1, y=90, width=120, height=40)
                            elif i == 8:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(8)).place(x=XiF_1, y=90, width=120, height=40)
                            elif i == 9:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(9)).place(x=XiF_1, y=90, width=120, height=40)
                            XiF_1 = XiF_1 + 135
                        elif i <= 14:
                            if i == 10:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(10)).place(x=XiF_2, y=140, width=120, height=40)
                            elif i == 11:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(11)).place(x=XiF_2, y=140, width=120, height=40)
                            elif i == 12:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(12)).place(x=XiF_2, y=140, width=120, height=40)
                            elif i == 13:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(13)).place(x=XiF_2, y=140, width=120, height=40)
                            elif i == 14:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(14)).place(x=XiF_2, y=140, width=120, height=40)
                            XiF_2 = XiF_2 + 135
                        elif i <= 19:
                            if i == 15:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(15)).place(x=XiF_3, y=190, width=120, height=40)
                            elif i == 16:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(16)).place(x=XiF_3, y=190, width=120, height=40)
                            elif i == 17:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(17)).place(x=XiF_3, y=190, width=120, height=40)
                            elif i == 18:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(18)).place(x=XiF_3, y=190, width=120, height=40)
                            elif i == 19:
                                tk.Button(window_ls, text=lista[i], font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command= lambda: say(19)).place(x=XiF_3, y=190, width=120, height=40)
                            XiF_3 = XiF_3 + 135
                except:
                    pass

                window_ls.mainloop()
                
            self.texto = texto
            self.X = X
            self.Y = Y
            self = tk.Button(window_silabas, text=texto, font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command=ls).place(x=X, y=Y, width=100, height=40)

        
    #Botones
    b = BL("B", 50, 40, b_list, b_say)
    c = BL("C", 165, 40, c_list, c_say)
    d = BL("D", 280, 40, d_list, d_say)
    f = BL("F", 50, 90, f_list, f_say)
    g = BL("G", 165, 90, g_list, g_say)
    h = BL("H", 280, 90, h_list, h_say)
    j = BL("J", 50, 140, j_list, j_say)
    k = BL("K", 165, 140, k_list, k_say)
    l = BL("L", 280, 140, l_list, l_say)
    m = BL("M", 50, 190, m_list, m_say)
    n = BL("N", 165, 190, n_list, n_say)
    ñ = BL("Ñ", 280, 190, ñ_list, ñ_say)
    p = BL("P", 50, 240, p_list, p_say)
    q = BL("Q", 165, 240, q_list, q_say)
    r = BL("R", 280, 240, r_list, r_say)
    s = BL("S", 50, 290, s_list, s_say)
    t = BL("T", 165, 290, t_list, t_say)
    v = BL("V", 280, 290, v_list, v_say)
    w = BL("W", 50, 340, w_list, w_say)
    x = BL("X", 165, 340, x_list, x_say)
    y = BL("Y", 280, 340, y_list, y_say)
    z = BL("Z", 165, 390, z_list, z_say)

    window_silabas.mainloop()
    

def significado():
    
    #Variables
    ent_sig = barra.get()
    url = "https://dem.colmex.mx/Ver/" + ent_sig
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    #Listas de Error
    lista_false_0 = []
    lista_false_1 = ['']
    lista_false_2 = ['', '']
    lista_false_3 = ['', '', '']
    lista_false_4 = ['', '', '', '']
    lista_false_5 = ['', '', '', '', '']
    lista_false_6 = ['', '', '', '', '', '']
    lista_false_7 = ['', '', '', '', '', '', '']
    lista_false_8 = ['', '', '', '', '', '', '', '']
    lista_false_9 = ['', '', '', '', '', '', '', '', '']
    lista_error = [lista_false_0, lista_false_1, lista_false_2, lista_false_3, lista_false_4, lista_false_5, lista_false_6, lista_false_7, lista_false_8, lista_false_9]

    #Resultados
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
    if palabra == [f'*{ent_sig.lower()}*']:
        engine.say(f"La palabra:, {error_palabra[0]}, no se ha encontrado, Tal vez lo que estas buscando es: ")
        engine.runAndWait()
        for i in sugerencias:
            engine.say(f"{i}")
            engine.runAndWait()
        barra.delete(0, "end")
    else:
        engine.say(f"{palabra[0]}")
        engine.runAndWait
        for i in definicion:
            engine.say(f"{i}")
            engine.runAndWait()
        
        if ejemplo in lista_error:
            engine.say("No hay ejemplos")
            engine.runAndWait()

        else:
            engine.say("Algunos ejemplos son:")
            engine.runAndWait()
            for i in ejemplo:
                engine.say(f"{i}")
                engine.runAndWait()
        barra.delete(0, "end")
        
barra.place(x=255, y=283, width= 504, height=27)

#Botones
b_Dictar=tk.Button(window, text="Dictar", font="TradeGothic 18",bg="#EBEBEB",activebackground="#EBEBEB",justify=CENTER, command=dictar).place(x=57, y=142, width=182, height=52)

b_Deletrear=tk.Button(window, text="Deletrear", font="TradeGothic 18", bg="#EBEBEB",activebackground="#EBEBEB", justify=CENTER, command=deletrear).place(x=170, y=383, width=182, height=52)

b_Silabas = tk.Button(window, text="Silabas", font="TradeGothic 18", bg="#EBEBEB", activebackground="#EBEBEB", justify=CENTER, command=silabas).place(x=425, y=383, width=182, height=52)

b_Significado = tk.Button(window, text="Significado", font="TradeGothic 18", bg="#EBEBEB", activebackground="#EBEBEB", justify=CENTER, command=significado).place(x=652, y=383, width=182, height=52)

window.mainloop()
