import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import Label, Entry, Button, PhotoImage, Tk

janela = Tk()

image = Image.open("vinho.jpg")
image = image.resize((750, 959))
photo = ImageTk.PhotoImage(image)
label_imagem = Label(janela, image=photo)
label_imagem.place(x=0, y=0)
#label_imagem.pack(side="top", fill="both", expand=True)

def classificador(teste):
  base_vinho = pd.read_csv('./winequality-red.csv').values

  x_train, x_test, y_train, y_test = train_test_split(np.array(base_vinho[:,0:11]), np.array(base_vinho[:,11]), test_size=0.3, shuffle=True, random_state=32)
  normalizador = MinMaxScaler()
  normalizador.fit(x_train)
  X_norm_train = normalizador.transform(x_train)

  knn = KNeighborsClassifier(n_neighbors=3)
  knn.fit(X_norm_train, y_train)
  
  teste = normalizador.transform(teste)
  
  return knn.predict(teste)


def classificar_dados_importados():
  caminho_do_arquivo = askopenfilename(filetypes=(("Arquivo CSV", "*.csv"), ("Arquivo Txt", "*.txt")))

  if caminho_do_arquivo:
    arquivo = pd.read_csv(caminho_do_arquivo).values
    arquivos = arquivo[:,0:11]
    with open("Classificação de Vinhos.txt", "w") as arquivo:
      arquivo.write("Classificação de vinhos gerados:\n")
      arquivo.close()
      
    with open("Classificação de Vinhos.txt", "a") as arquivo: 
      for teste in arquivos:
        testes = [teste]
        arquivo.write(str(classificador(testes)))
        arquivo.write("\n")
      arquivo.close()
      classificacao['text'] = "Classificação salva no arquivo 'Classificação de Vinhos'"
      
  else:
    classificacao['text'] = "Nenhum arquivo selecionado"


def obter_dados():
  acidez_fixa = float(CaixaDeEntrada1.get())
  acidez_volatil = float(CaixaDeEntrada2.get())
  acido_citrico = float(CaixaDeEntrada3.get())
  acucar_residual = float(CaixaDeEntrada4.get())
  cloreto = float(CaixaDeEntrada5.get())
  dioxido_enxofre = float(CaixaDeEntrada6.get())
  dioxido_enxofre_total = float(CaixaDeEntrada7.get())
  densidade = float(CaixaDeEntrada8.get())
  ph = float(CaixaDeEntrada9.get())
  sulfatos = float(CaixaDeEntrada10.get())
  alcool = float(CaixaDeEntrada11.get())
  
  dados = [[acidez_fixa, acidez_volatil, acido_citrico, acucar_residual, cloreto, dioxido_enxofre, dioxido_enxofre_total, densidade, ph, sulfatos, alcool]]
  c = classificador(dados)
  classificacao['text'] = int(c[0])

#-------------------------------------------------#
#tela

titulo1 = Label(bg='#D2D2D4', font=('Roboto', '34', 'bold'), fg='black', text='Bem Vindo ao QualityVinho!')
titulo1.place(x='40', y='2')

titul2 = Label(bg='#D2D2D4', font=('Roboto', '20', 'bold'), fg='black', text='Insira os dados do vinho:')
titul2.place(x=100, y=90)

CaixaDeEntrada1 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada1.place(x=450, y=150)
Info1 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Acidez Fixa: ')
Info1.place(x=65, y=150)

CaixaDeEntrada2 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada2.place(x=450, y=190)
Info2 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Acidez Volatil: ')
Info2.place(x=65, y=190)

CaixaDeEntrada3 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada3.place(x=450, y=230)
Info3 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Acido citrico: ')
Info3.place(x=65, y=230)

CaixaDeEntrada4 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada4.place(x=450, y=270)
Info4 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Acucar Residual: ')
Info4.place(x=65, y=270)

CaixaDeEntrada5 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada5.place(x=450, y=310)
Info5 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Cloreto: ')
Info5.place(x=65, y=310)

CaixaDeEntrada6 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada6.place(x=450, y=350)
Info6 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Dioxido de enxofre livre: ')
Info6.place(x=65, y=350)

CaixaDeEntrada7 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada7.place(x=450, y=390)
Info7 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Dioxido de enxofre total: ')
Info7.place(x=65, y=390)

CaixaDeEntrada8 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada8.place(x=450, y=430)
Info8 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Densidade: ')
Info8.place(x=65, y=430)

CaixaDeEntrada9 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada9.place(x=450, y=470)
Info9 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='PH: ')
Info9.place(x=65, y=470)

CaixaDeEntrada10 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada10.place(x=450, y=510)
Info10 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Sulfatos: ')
Info10.place(x=65, y=510)

CaixaDeEntrada11 = Entry(width=10, bg='#D2D2D4', font=('Roboto', '10'))
CaixaDeEntrada11.place(x=450, y=550)
Info11 = Label(font=('Roboto', '11', 'bold'), fg='black', bg='#D2D2D4', text='Alcool:')
Info11.place(x=65, y=550)


classificacao = Label(janela, text='', font=('Roboto', '15', 'bold'), fg='black', bg='#D2D2D4', width=46, height=2, anchor='w', justify='left')
classificacao.place(x=40, y=830)

proximo = Button(width='39', text='CLASSIFICAR', font=('Roboto','10'), command=obter_dados)
proximo.place(x=40, y=780)

importarDados = Button(width='39', text='IMPORTAR DADOS', font=('Roboto','10'), command=classificar_dados_importados)
importarDados.place(x=400, y=780)

janela.resizable(width=False, height=False)
janela.configure(bg='#D2D2D4')
janela.title('Classificador de Vinhos')
janela.geometry('750x959+300+50')
janela.mainloop()