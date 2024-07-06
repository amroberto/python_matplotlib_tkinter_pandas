# Neste desafio, você irá criar um sistema que lê dados de um arquivo CSV, processa esses dados usando 
# NumPy e Pandas, e gera gráficos com Matplotlib. Siga o passo a passo abaixo para completar a tarefa.
#
#
# Passo 1: Instalação das Bibliotecas
# Antes de começar, você precisa instalar as bibliotecas necessárias. Abra o terminal ou prompt de 
# comando e execute os seguintes comandos:
#
# Passo 2: Preparação dos Dados
# Crie um arquivo CSV chamado dados.csv com o seguinte conteúdo:
#
# Passo 3: Criação do Sistema
# Agora, vamos criar o script Python que realizará as seguintes tarefas:
# Ler o arquivo CSV usando Pandas.
# Processar os dados usando NumPy.
# Gerar gráficos usando Matplotlib.
# Exibir a interface gráfica com Tkinter.
# Crie 5 botões 
# Em cada botão precisa mostrar um tipo de grafico
# Mostre a estatistica também

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
from tkinter import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import tkinter.filedialog
import os

def selecionar():
    Tk().withdraw()
    caminho = filedialog.askopenfilename(
        title = 'SELECIONE O ARQUIVO CSV',
        filetypes = (
            ("CSV files","*.csv"),
            ("all files", "*.*")
        )
    )
    return caminho

# grafico de linha
def data_plot():
    caminho = selecionar()

    if caminho:
        dados = pd.read_csv(caminho)
        vendedor = dados['vendedor'].to_list()
        vendas = dados['vendas'].to_list()
        fig, grafico = plt.subplots(figsize=(4, 3))
        grafico.plot(vendedor, vendas)
        plt.rcParams.update({'font.size': 8})

        # tkinter com o pyplot
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    else:
        print('Nenhum arquivo selecionado')


# gráfico de barra
def data_bar():
    caminho = selecionar()

    if caminho:
        dados = pd.read_csv(caminho)
        vendedor = dados['vendedor'].to_list()
        vendas = dados['vendas'].to_list()
        fig, grafico = plt.subplots(figsize=(4, 3))
        grafico.bar(vendedor, vendas)
        plt.rcParams.update({'font.size': 8})


        # tkinter com o pyplot
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    else:
        print('Nenhum arquivo selecionado')

# grafico de pizza
def data_pie():
    caminho = selecionar()

    if caminho:
        dados = pd.read_csv(caminho)
        vendedor = dados['vendedor'].to_list()
        vendas = dados['vendas'].to_list()
        fig, grafico = plt.subplots(figsize=(4, 3))
        grafico.pie(vendas, labels=vendedor)
        plt.rcParams.update({'font.size': 8})

        # tkinter com o pyplot
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    else:
        print('Nenhum arquivo selecionado')

# grafico de dispersão
def data_scatter():
    caminho = selecionar()

    if caminho:
        dados = pd.read_csv(caminho)
        vendedor = dados['vendedor'].to_list()
        vendas = dados['vendas'].to_list()
        fig, grafico = plt.subplots(figsize=(4, 3))
        grafico.scatter(vendedor, vendas)
        plt.rcParams.update({'font.size': 8})
        grafico.grid(True)

        # tkinter com o pyplot
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    else:
        print('Nenhum arquivo selecionado')


def data_esta():
    caminho = selecionar()

    if caminho:
        dados = pd.read_csv(caminho)
        vendedor = dados['vendedor'].to_list()
        vendas = dados['vendas'].to_list()
        media = np.mean(vendas)
        mediana = np.median(vendas)
        desvio = np.std(vendas)

        resultado_text = (f'''
                            Media: {media:.2f}
                            Mediana; {mediana:.2f}
                            Desvio padrão: {desvio:.2f}
                        ''')
        
        display_sta.config(text=resultado_text)
    else:
        print('Nenhum arquivo selecionado')

janela = tk.Tk()

btn1 = tk.Button(janela, text= 'Grafico Linha', command=data_plot)
btn1.pack(pady=5)

btn2 = tk.Button(janela, text= 'Gráfico Barra', command=data_bar)
btn2.pack(pady=5)

btn3 = tk.Button(janela, text= 'Gráfico Pizza', command=data_pie)
btn3.pack(pady=5)

btn4 = tk.Button(janela, text= 'Gráfico Dispersão', command=data_scatter)
btn4.pack(pady=5)

btn5 = tk.Button(janela, text= 'Estatística', command=data_esta)
btn5.pack(pady=5)

display_sta = tk.Label(janela, text= '', bg='black', fg='white')
display_sta.pack(pady=5)

janela.mainloop()

plt.show()