import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3
from tkinter import *
import sqlite3
from PIL import Image, ImageTk

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
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado INTEGER)")
def VerificarCPF(CPF):
    # CPF deve ser na forma "123.456.789-10"
    if len(CPF) != 14: #verificando se o tamanho total do CPF é 14 caracteres.
        return False
    partes = CPF.split(".") #dividido em três partes
    if len(partes) != 3:
        return False
    if len(partes[2].split("-")) != 2: #dividido em duas partes
        return False
    for trecho in partes[:2] + partes[2].split("-"): #garantir que possuem apenas dígitos e tenham o tamanho correto (3 para as três primeiras partes e 2 para a última).
        if not trecho.isdigit() or len(trecho) != 3 and len(trecho) != 2:
            return False
    return True

def inserevalores(nome, cpf, estado):
    #Insere linha na tabela
    cursor.execute("INSERT INTO Tabela1 (nome, cpf, estado) VALUES (?, ?, ?)", (nome, cpf, estado))

def salvarDados():
    nome = textoEntrada.get()
    cpf = textoEntrada2.get()
    estado = textoEntrada3.get()

    inserevalores(nome, cpf, estado)

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