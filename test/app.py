from flask import Flask, render_template, request

app = Flask(__name__)

threshold = {'temp_low': 35, 'temp_up': 40}

text_list = ['Warm', 'Cold', 'Comfortable']


@app.route('/temp', methods=['GET'])
def temperature():
    ops = request.args.get('ops')
    if ops == '1':
        threshold['temp_low'] -= 3
        threshold['temp_up'] -= 3
    elif ops == '-1':
        threshold['temp_low'] += 3
        threshold['temp_up'] += 3
    text = text_list[checker()]
    result = {"low": threshold['temp_low'], "text": text}
    return result


def filer():
    with open("/Users/zekunzhang/PycharmProjects/test/test", 'r') as f:
        line = f.readline()
    return int(line)


def checker():
    val = filer()
    if val < threshold['temp_low']:
        return 0
    elif threshold['temp_low'] < val < threshold['temp_up']:
        return 1
    else:
        return 2


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
