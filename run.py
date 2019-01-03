from flaskblog import create_app

host = "0.0.0.0"
port = "5000"

app = create_app()

if __name__ == '__main__':
    app.run(debug=False, host=host, port=port)
