# -*- coding: cp1252 -*-
import pandas as pd
import numpy as np
from tkinter import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

janela = Tk()
img = PhotoImage(file="")
label_imagem = Label(janela, image=img).pack()

def __init__():
    pass
def ok():

    # Carregando dados do arquivo CSV
    url = 'winequality-red.csv'
    base_Treinamento = pd.read_csv(url, sep=',', encoding='latin1').values
    print("---------------------------------")
    print("Dados dos Pacientes - TREINAMENTO")
    print("---------------------------------")
    print(base_Treinamento)
    print("---------------------------------")

    # Extração dos Atributos a serem utilizadas pela rede
    print("Atributos de Entrada")
    print("---------------------------------")
    print(base_Treinamento[:, 0:11])

    print("----------------------------")
    print("Classificação Supervisionada")
    print("----------------------------")
    print(base_Treinamento[:, 11])

    scaler = StandardScaler()
    X_Train = np.array(base_Treinamento[:, 0:12])

    # X_train = scaler.fit_transform(X_Train)

    # X_norm_train, X_norm_test, Y_train, Y_test = train_test_split(X_Train[:,1:7], np.array(base_Treinamento[:, 0]), test_size = 0.3)

    X_norm_train = X_Train[:, 0:11]
    # print("--------------------------------")
    print("Atributos de Entrada - Numéricos")
    print("--------------------------------")
    print(X_norm_train)

    print("----------------------------------------")
    print("Classificação Supervisionada - Numéricos")
    print("----------------------------------------")
    Y_train = np.array(base_Treinamento[:, 11])
    # Y_train = Y_train.astype('str')
    print(Y_train)

    # Treinamento da MLP a partir dos atributos de entrada e classificações
    from sklearn.neural_network import MLPClassifier
    rna = MLPClassifier(verbose=True, max_iter=300, tol=0.000010)
    rna.fit(X_norm_train, Y_train)

    # Acurácia do modelo, que é : 1 - (predições erradas / total de predições)
    # Acurácia do modelo: indica uma performance geral do modelo.
    # Dentre todas as classificações, quantas o modelo classificou corretamente;
    # (VP+VN)/N
    print('Acurácia: %.3f' % rna.score(X_norm_train, Y_train))

    from sklearn.neighbors import KNeighborsClassifier
    # Treinamento do Knn a partir dos atributos de entrada e classificações com K=3
    modelo = KNeighborsClassifier(n_neighbors=1, algorithm='ball_tree')
    modelo.fit(X_norm_train, Y_train)

    # Acurácia do modelo, que é : 1 - (predições erradas / total de predições)
    # Acurácia do modelo: indica uma performance geral do modelo.
    # Dentre todas as classificações, quantas o modelo classificou corretamente;
    # (VP+VN)/N
    print('Acurácia: %.3f' % modelo.score(X_norm_train, Y_train))


    acidez_fixa = str(CaixaDeEntrada1.get())
    acidez_volatil = str(CaixaDeEntrada2.get())
    acido_citrico = str(CaixaDeEntrada3.get())
    acucar_residual = str(CaixaDeEntrada4.get())
    cloreto = str(CaixaDeEntrada5.get())
    dioxido_enxofre = str(CaixaDeEntrada6.get())
    dioxido_enxofre_total = str(CaixaDeEntrada7.get())
    densidade = str(CaixaDeEntrada8.get())
    ph = str(CaixaDeEntrada9.get())
    sulfatos = str(CaixaDeEntrada10.get())
    alcool = str(CaixaDeEntrada11.get())



    lista = [acidez_fixa, '\n', acidez_volatil,'\n', acido_citrico,'\n', acucar_residual, '\n', cloreto, '\n', dioxido_enxofre, '\n',
             dioxido_enxofre_total, '\n', densidade,'\n', ph,'\n',  sulfatos,'\n', alcool]

    arquivo = open("texto.txt", "a")
    arquivo.writelines(lista)


    print(acidez_fixa)
    print(acidez_volatil)
    print(acido_citrico)
    print(acucar_residual)
    print(cloreto)
    print(dioxido_enxofre)
    print(dioxido_enxofre_total)
    print(densidade)
    print(ph)
    print(sulfatos)
    print(alcool)

    CaixaDeEntrada3['bg'] = 'white'

    if acidez_fixa in ' ':
        CaixaDeEntrada1['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada1['bg'] = 'white'

    if acidez_volatil in ' ':
        CaixaDeEntrada2['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada2['bg'] = 'white'

    if acido_citrico in ' ':
        CaixaDeEntrada3['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada3['bg'] = 'white'

    if acucar_residual in ' ':
        CaixaDeEntrada4['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada4['bg'] = 'white'

    if cloreto in ' ':
        CaixaDeEntrada5['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada5['bg'] = 'white'

    if dioxido_enxofre in ' ':
        CaixaDeEntrada6['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada6['bg'] = 'white'

    if dioxido_enxofre_total in ' ':
        CaixaDeEntrada7['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada7['bg'] = 'white'

    if densidade in ' ':
        CaixaDeEntrada8['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada8['bg'] = 'white'

    if ph in ' ':
        CaixaDeEntrada9['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada9['bg'] = 'white'

    if sulfatos in ' ':
        CaixaDeEntrada10['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada10['bg'] = 'white'

    if alcool in ' ':
        CaixaDeEntrada11['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        CaixaDeEntrada11['bg'] = 'white'




    if acidez_fixa != '' and acidez_volatil != '' and acido_citrico != '' and cloreto != '' and dioxido_enxofre != '' and dioxido_enxofre_total != '' and densidade != '' and ph != '' and sulfatos != '' and alcool != '':
        janela.destroy()

    Teste = [[float(acidez_fixa), float(acidez_volatil), float(acido_citrico), float(acucar_residual), float(cloreto), float(dioxido_enxofre),
             float(dioxido_enxofre_total), float(densidade), float(ph), float(sulfatos), float(alcool)]]
    print("Teste", modelo.predict(Teste))

#==========================================Janela Inicial:

titulo1 = Label(bg='#682a31', font=('Arial', '14', 'bold'), fg='white', text='BEM VINDO ao QualityVinho')
titulo1.place(x='13', y='10')

CaixaDeEntrada1 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada1.place(x=300, y=50)
Info1 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Acidez Fixa: ')
Info1.place(x=10, y=50)

CaixaDeEntrada2 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada2.place(x=300, y=75)
Info2 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Acidez Volátil: ')
Info2.place(x=10, y=75)

CaixaDeEntrada3 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada3.place(x=300, y=100)
Info3 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Ácido cítrico: ')
Info3.place(x=10, y=100)

CaixaDeEntrada4 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada4.place(x=300, y=125)
Info4 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Açucar Residual: ')
Info4.place(x=10, y=125)

CaixaDeEntrada5 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada5.place(x=300, y=150)
Info5 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Cloreto: ')
Info5.place(x=10, y=150)

CaixaDeEntrada6 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada6.place(x=300, y=175)
Info6 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Dióxido de enxofre livre: ')
Info6.place(x=10, y=175)

CaixaDeEntrada7 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada7.place(x=300, y=200)
Info7 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Dióxido de enxofre total: ')
Info7.place(x=10, y=200)

CaixaDeEntrada8 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada8.place(x=300, y=225)
Info8 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Densidade: ')
Info8.place(x=10, y=225)

CaixaDeEntrada9 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada9.place(x=300, y=250)
Info9 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='PH: ')
Info9.place(x=10, y=250)

CaixaDeEntrada10 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada10.place(x=300, y=275)
Info10 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Sulfatos: ')
Info10.place(x=10, y=275)

CaixaDeEntrada11 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
CaixaDeEntrada11.place(x=300, y=300)
Info11 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#682a31', text='Álcool:')
Info11.place(x=10, y=300)

erro = Label(bg='#682a31', fg='red', font=('Arial', '11'), text='')
erro.place(x=20, y=725)

proximo = Button(width='39', text='Próximo', font=('Arial','10'), command=ok)
proximo.place(x=20, y=700)



#=======================================FimDaJanelaInicial


#Propriedades da janela:
janela.resizable(width=False, height=False)
janela.configure(bg='#682a31')
#janela.wm_iconbitmap('ICO.ico')
janela.title('Relatórios DIC - Por WellersonOP')
janela.geometry('800x800+800+800')
janela.mainloop()

