from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)

@app.route('/home')
def ola():
    jogo1 = Jogo('Tetris', "Puzzle", 'Atari')
    jogo2 = Jogo('GOW', 'Rack n Slash', 'PS2')
    jogo3 = Jogo('MK3', 'Luta', 'PS2')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos = lista)

app.run(host='127.0.0.1', port=8080)