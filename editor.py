import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

janela = tk.Tk()
janela.geometry("800x800")
janela.resizable(0, 0)
janela.title("Editor de texto")

def novoArquivo():
    caixaDeTexto.delete(1.0, tk.END)
    janela.title(f"Editor de Texto")

def abrirArquivo():
    arquivo = askopenfilename(filetypes=[["Arquivos de texto", "*.txt"],["Todos os arquivos","."]])
    if not arquivo:
        return
    caixaDeTexto.delete(1,0, tk.END)
    with open(arquivo, "r") as arquivoDeEntrada:
        texto = arquivoDeEntrada.read()
        caixaDeTexto.insert(tk.END, texto)
    janela.title(f"Editor de Texto - {arquivo}")

def salvaArquivo():
    arquivo = asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt"),("All Files", "*.*")])      
    if not arquivo:
        return
    with open(arquivo, "w") as arquivoDeSaida:
        texto = caixaDeTexto.get(1.0, tk.END)
        arquivoDeSaida.write(texto)
    janela.title(f"Editor de Texto -{arquivo} ")

barraDeMenu = tk.Menu(janela)

menuArquivo = tk.Menu(barraDeMenu, tearoff=0)         
menuArquivo.add_command(label="Novo", command=novoArquivo)
menuArquivo.add_command(label="Abrir", command=abrirArquivo)
menuArquivo.add_command(label="Salvar como...", command=salvaArquivo)
menuArquivo.add_separator()
menuArquivo.add_command(label="Sair", command=janela.quit)

barraDeMenu.add_cascade(label="Arquivo", menu=menuArquivo)

janela.config(menu=barraDeMenu)

barraDeRolagem = tk.Scrollbar(janela)
caixaDeTexto = tk.Text(janela, yscrollcommand=barraDeRolagem.set)
barraDeRolagem.config(command=caixaDeTexto.yview)

barraDeRolagem.pack(side=tk.RIGHT, fill="y")
caixaDeTexto.pack(expand=True, fill="both")

janela.mainloop()