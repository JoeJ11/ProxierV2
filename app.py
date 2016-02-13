import proxy_manager

from flask import Flask
app = Flask(__name__)

@app.route("/create", methods=['POST'])
def create():
    target_url = request.form['target']
    proxy_addr, code = proxy_manager.GenerateProxy(target_url)
    resp = make_response(proxy_addr, code)
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route("/", methods=['GET'])
def list():
    return "List"

@app.route("/delete", methods=['POST'])
def remove():
    target_url = request.form['target']
    proxy_manager.RemoveProxy(target_url)
    return json.dumps({'status':True})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)