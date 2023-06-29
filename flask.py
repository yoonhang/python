from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello(): 
    return 'hello, flask...'

@app.route('/auto')
def auto():
    return render_template("test.html")

def main():
    app.run(host='localhost', debug=False, port=80)
    
if __name__ == '__main__':
    main()
    