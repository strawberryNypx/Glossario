import os
import csv
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Definindo a variável de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# Configurando o modo de depuração com base na variável de ambiente
app.debug = os.environ.get('FLASK_DEBUG') == 'True'

@app.route('/')
def ola():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/glossario')
def glossario():

    glossario_de_termos = []

    with open('bd_glossario.csv',newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            glossario_de_termos.append(l)

    return render_template('glossario.html',glossario=glossario_de_termos)


@app.route('/novo_termo')
def novo_termo():
    return render_template('adicionar_termo.html')


@app.route('/criar_termo', methods=['POST', ])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']

    with open(
            'bd_glossario.csv', 'a',
            newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))


@app.route('/excluir_termo/<int:termo_id>', methods=['POST'])
def excluir_termo(termo_id):

    with open('bd_glossario.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        linhas = list(reader)

    # Encontrar e excluir o termo com base no ID
    for i, linha in enumerate(linhas):
        if i == termo_id:
            del linhas[i]
            break

    # Salvar as alterações de volta no arquivo
    with open('bd_glossario.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(linhas)

    return redirect(url_for('glossario'))

@app.route('/ListaDeTarefas', methods=['POST'])
def listaDeTarefas():
    lista_de_tarefas = []

    with open('listaDeTarefas.csv',newline='', encoding='utf-8') as arquivo2:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            lista_de_tarefas.append(l)

    return render_template('ListaDeTarefas.Html',listaDeTarefass = lista_de_tarefas)

@app.route('/novo_termo_lista')
def novo_termo():
    return render_template('adicionar_termo-listadetarefa.html')


@app.route('/criar_termo', methods=['POST', ])
def criar_termonalista():
    tarefa = request.form['Tarefa']
    descricao = request.form['Descrição']

    with open(
            'listaDeTarefas.csv', 'a',
            newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('ListaDeTarefas'))


@app.route('/excluir_termo_listadetarefas/<int:termo_id>', methods=['POST'])
def excluir_termo_lista(termo_id):

    with open('listaDeTarefas.csv', 'r', newline='') as P:
        reader = csv.reader(file)
        linhas = list(reader)


    for i, linha in enumerate(linhas):
        if i == termo_id:
            del linhas[i]
            break

    with open('bd_glossario.csv', 'w', newline='') as P2:
        writer = csv.writer(file)
        writer.writerows(linhas)

    return redirect(url_for('ListaDeTarefas'))





if __name__ == "__main__":
    app.run()
