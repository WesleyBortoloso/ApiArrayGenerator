from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from random import randint
import random
import time
import numpy as np

app = Flask("TransformArray")
CORS(app) 

@app.route('/transformArray', methods=['POST'])
@cross_origin()


def transformArray():

  # inicia tempo de execução
  start = time.time()

  # pega a informação do body
  body = request.get_json() 
  print(body)
  n = (body["n"])
  
  # gera o array com numeros aleatorios
  array = np.random.randint(100, size=n).tolist()

  # da inicio a verificação pelo metodo de bogosort
  bogoSort(array)

  # ordenar o array pelo metodo de bogosort
  for i in range(len(array)):
    print ("%d" %array[i])

  # adiciona 1 segundo ao tempo para que seja impresso
  time.sleep(1)

  # finaliza o tempo de execução
  end = time.time()

  # retorna em formato de JSON
  return jsonify(
    array= array,
    n= n,
    tempo= (start - end),
  )

  # funções para realizar o metodo de bogo para ordenar o array
def bogoSort(array):
    n = len(array)
    while (is_sorted(array)== False):
        shuffle(array)

def is_sorted(array):
    n = len(array)
    for i in range(0, n-1):
        if (array[i] > array[i+1] ):
            return False
    return True

def shuffle(array):
    n = len(array)
    for i in range (0,n):
        r = random.randint(0,n-1)
        array[i], array[r] = array[r], array[i]

app.run()