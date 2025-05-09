from flask import Flask

app = Flask(__name__)  # Aquí se encontrará el servidor web de Flask

if __name__ == "__main__":
    app.run(debug=True)  # debug=True para que reinicie solo
