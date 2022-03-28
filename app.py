from flask import Flask, Response, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    
    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

@app.route('/status')
def status():
    return Response("204 No Content", status=204)

@app.route('/info')
def info():
    the_url = jsonify(url=request.base_url)
    return the_url, 200

@app.route('/security', methods=["DELETE"])
def delete():
    return Response(status=401)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
