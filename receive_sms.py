import plivo, plivoxml
from flask import Flask, request

app = Flask(__name__)

@app.route("/receive_sms/", methods=['GET','POST'])
def receive_sms():
    # Sender's phone numer
    from_number = request.values.get('From')
    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')
    # The text which was received
    text = request.values.get('Text')

    resp = plivo.Response()
    resp.message('Hello')
    return str(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)