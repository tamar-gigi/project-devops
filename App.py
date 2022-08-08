from flask import Flask
app = Flask(__name__)

i=0

@app.route('/')
def hello():
    global i
    i+=1
    return f'Hello, Docker! {i}'


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
