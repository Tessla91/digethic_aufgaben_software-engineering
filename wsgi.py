from src.api import app

if __name__ == "__main__": #funktioniert nur mit "main", weil wsgi direkt ausgeführt wird
    app.run(debug=True)
