from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = json.loads(request.data)
    form_data = data['data']
    name = form_data['Name 2']
    email = form_data['Email 2']

    return {'name': name, 'email': email, 'form_name': form_data['formName']}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
