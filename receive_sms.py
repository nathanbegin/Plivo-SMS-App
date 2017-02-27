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

    # Print the message
    print 'Message received - From: %s, To: %s, Text: %s' % (from_number, to_number, text)

    return "Message received", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)