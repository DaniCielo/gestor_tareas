from flask import Flask

app = Flask(__name__)  # Aquí se encontrará el servidor web de Flask


# La barra (el slash) se conoce como la página de inicio (página home)
@app.route('/')
def home():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)  # debug=True para que reinicie solo
