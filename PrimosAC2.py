import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():
    limite = 100
    qtd = 2
    numero = 3
    primos = '1,2,'

    while qtd < limite:
        eprimo = 1
        for i in range (2, numero):
            if numero % i == 0:
                eprimo = 0
                break
        if (eprimo):
            primos = primos + str(numero) + ','
            qtd +=1
            if (qtd % 10 == 0):
                primos = primos + ' -> ' + str(qtd) + '<br>'  
        numero +=1
        
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
