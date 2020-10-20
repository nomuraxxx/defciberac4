import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

