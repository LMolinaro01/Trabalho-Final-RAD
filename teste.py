import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3

#adicionar mais duas entrys (cpf e estado) e suas labels - v2
#mudar o fundo para uma imagem mais bonita, adicionar readme.txt explicando como usar - v3
#adicionar clicar no botão salva os 3 dados em um sqlite - v4
#Criar uma branch em que le um config.txt com uma lista de 5 estados possiveis separados por pular linha - x1
#Mudar o separador para ; e adicionar mais 5 estados - x2
#Voltar para main, criar outra branch e criar um dropdown com 3 opções (clt, mei, socio) - y1
#Voltar para main, Corrigir o bug da função de cpf - v5
#Merge de x com v - v6
#Adicionar verificação de CPF e de estado, com base na função cpf e na lista de estados .txt antes de adicionar no sqlite v7

#Cria conexção
connection = sqlite3.connect("teste.db")

#Cria o cursos e cria a tabela
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, curso TEXT, matricula INTEGER)")
def VerificarCPF(CPF):
    #CPF deve ser na forma "123.456.789-10"
    for trecho in CPF.split("."):
        if len(trecho)!=3:
            return False
        else:
            return True

def inserevalores(Valor1, Valor2):
    #Insere linha na tabela
    cursor.execute("INSERT INTO Tabela1 VALUES ('"+Valor1+"', '"+Valor2+"')")

def pegavalores():
    #Pega valores da tabela
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def funcExemplo():
    print("Exemplo de funcao")
    
def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)
    
    label = tkinter.Label(root, text="Nome")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()

    label2 = tkinter.Label(root, text="CPF")
    label2.pack()

    textoEntrada2 = tkinter.StringVar()
    e2 = tkinter.Entry(root)
    e2.bind('<Key>', lambda x: textoEntrada2.set(e2.get() + x.char))
    e2.pack()

    label3 = tkinter.Label(root, text="Estado")
    label3.pack()

    textoEntrada3 = tkinter.StringVar()
    e3 = tkinter.Entry(root)
    e3.bind('<Key>', lambda x: textoEntrada3.set(e3.get() + x.char))
    e3.pack()

    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = funcExemplo  #alterar para chamar outra função
    test2.pack()

    root.iconify() #Minimiza a tela
    root.update()
    root.deiconify() #Maximiza a tela
    root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs
Main()