# coding: utf-8
from flask import Flask, render_template

app =  Flask("projeto")

@app.route("/")
def ola_mundo():
    #criando uma variavel com o meu nome
    nome = 'Gustavo Miguel'

    return render_template("alo.html", n=nome), 200

app.run()