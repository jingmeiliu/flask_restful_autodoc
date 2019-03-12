from app import create_app

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True,host='192.168.200.77',port=8080)
    app.run(debug=True,port=8080)
