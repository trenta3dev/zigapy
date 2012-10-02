from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/send/', methods=['POST'])
def send():
    from zigapy import Ziga, Channel

    data = request.form
    channel_name, message = data['channel'], data['message']

    ziga = Ziga('sse')
    channel = Channel(ziga, channel_name)
    channel.trigger('message', dict(text=message))

    return jsonify(status='success')


if __name__ == "__main__":
    app.run(port=5335, debug=True)
