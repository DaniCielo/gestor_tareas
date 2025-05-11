from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Aquí se encontrará el servidor web de Flask


# La barra (el slash) se conoce como la página de inicio (página home)
@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)  # debug=True para que reinicie solo
