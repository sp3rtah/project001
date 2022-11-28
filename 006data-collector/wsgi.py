from main import create_app

app = create_app()

if __name__ == '__main__':
    if app.config['ENV'] == 'production':
        app.run(debug=True, host='0.0.0.0', port=8000)
