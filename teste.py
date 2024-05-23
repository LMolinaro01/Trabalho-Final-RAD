import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3
from tkinter import *
import sqlite3
from PIL import Image, ImageTk

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
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado INTEGER)")
def VerificarCPF(CPF):
    #CPF deve ser na forma "123.456.789-10"
    for trecho in CPF.split("."):
        if len(trecho)!=3:
            return False
        else:
            return True

def inserevalores(nome, cpf, estado):
    #Insere linha na tabela
    cursor.execute("INSERT INTO Tabela1 (nome, cpf, estado) VALUES (?, ?, ?)", (nome, cpf, estado))

def salvarDados():
    nome = textoEntrada.get()
    cpf = textoEntrada2.get()
    estado = textoEntrada3.get()

    inserevalores(nome, cpf, estado)

def carregarEstados():
    with open("config.txt", "r") as file:
        linha = file.readline().strip()
        estados = linha.split(';')
    return estados

def pegavalores():
    #Pega valores da tabela
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def funcExemplo():
    print("Exemplo de funcao")
    
def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    #root.resizable(False, False)

    image1 = Image.open("wallpaper.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(root, image=test)
    label1.image = test
    label1.place(x=0, y=0)

    label = tkinter.Label(root, text="Nome", bg = "#003366", fg="white")
    label.grid(row=1, column=1, pady=10)

    global textoEntrada
    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root, textvariable=textoEntrada)
    e1.grid(row=2, column=1, pady=10)

    label2 = tkinter.Label(root, text="CPF", bg="#003366", fg="white")
    label2.grid(row=3, column=1, pady=10)

    global textoEntrada2
    textoEntrada2 = tkinter.StringVar()
    e2 = tkinter.Entry(root, textvariable=textoEntrada2)
    e2.grid(row=4, column=1, pady=10)

    label3 = tkinter.Label(root, text="Estado", bg="#003366", fg="white")
    label3.grid(row=5, column=1, pady=10)

    global textoEntrada3
    textoEntrada3 = tkinter.StringVar()
    e3 = tkinter.Entry(root, textvariable=textoEntrada3)
    e3.grid(row=6, column=1, pady=10)

    test2 = tkinter.Button(root, text="Salvar", command=salvarDados)
    test2.grid(row=7, column=1, pady=10)

    root.iconify() #Minimiza a tela
    root.update()
    root.deiconify() #Maximiza a tela
    root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs
Main()