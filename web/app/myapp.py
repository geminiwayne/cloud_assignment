#COMP90024
#Team 4
#Dong Wang (773504)
#Sixue Yang   (722804)
#Danping Zeng (777691)
#Zhen Jia (732355)
#Jinghan Liang (732329)

from couchdb.client import Server
from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)
server = Server('http://admin:password@115.146.93.201:5984/')
db = server['twitter']
db2 = server['twdata']
db3 = server['new_tweet']

@app.route('/')
def arch():

    return render_template('index.html')

@app.route('/source')
def sourcePolarity():

    return render_template('source.html')

@app.route('/userDistribution')
def userDistribution():

    return render_template('userDistribution.html')

@app.route('/negativeCity')
def negativeCity():

    return render_template('districtPolarity.html')

@app.route('/hotTopic')
def hotTopic():

    return render_template('hotTopic.html')

@app.route('/language')
def language():

    return render_template('language.html')

@app.route('/24hour')
def hour():

    return render_template('24hour.html')

@app.route('/weather')
def weather():

    return render_template('weather.html')

@app.route('/sport')
def sport():

    return render_template('sport.html')



#data API to return the data from couchdb
@app.route('/districtPolarity_data')
def districtPolarity_data():
    rows = []
    for row in list(db3.view('polarity/DistrictPolarity',group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value[0]}]})

    response = {
        'cols': [{'id': 'DistrictPolarity', 'label': 'DistrictPolarity', 'type': 'string'},
                 {'id': 'avg_polarity', 'label': 'avg_polarity', 'type': 'number'}],
        'rows': rows
    }
    return jsonify(response)

@app.route('/popular_data')
def popular_data():
    rows = []
    for row in list(db2.view('popularity/top10', group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value}]})

    response = {
        'cols': [{'id': 'popularity', 'label': 'popularity', 'type': 'string'},
                 {'id': 'numbers', 'label': 'number', 'type': 'number'}],
        'rows': rows
    }
    return jsonify(response)

@app.route('/hotTopic_data')
def hotTopic_data():
    rows = []
    for row in list(db.view('topic/top10', group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value}]})

    response = {
        'cols': [{'id': 'hotTopic', 'label': 'hotTopic', 'type': 'string'},
                 {'id': 'numbers', 'label': 'number', 'type': 'number'}],
        'rows': rows
    }
    return jsonify(response)

@app.route('/negativeCity_data')
def negativeCity_data():
    rows = []
    for row in list(db.view('polarity/NegativeCity',group = True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value}]})

    response = {
        'cols': [{'id': 'NegativeCity', 'label': 'NegativeCity', 'type': 'string'},
                 {'id': 'numbers', 'label': 'users', 'type': 'number'}],
        'rows': rows
    }

    return jsonify(response)

@app.route('/userDistribution_data')
def userDistribution_data():
    rows = []
    for row in list(db.view('location/UserDistribution',group = True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value}]})

    response = {
        'cols': [{'id': 'UserDistribution', 'label': 'UserDistribution', 'type': 'string'},
                 {'id': 'numbers', 'label': 'users', 'type': 'number'}],
        'rows': rows
    }

    return jsonify(response)

@app.route('/sourcePolarity_data')
def sourcePolarity_data():
    rows = []
    for row in list(db2.view('source/HappinessWithDevice',group = True)):
        rows.append({'c': [{'v': row.key}, {'v': row.value[0]}]})

    response = {
        'cols': [{'id': 'sourcePolarity', 'label': 'sourcePolarity', 'type': 'string'},
                 {'id': 'numbers', 'label': 'avg_polarity', 'type': 'number'}],
        'rows': rows
    }

    return jsonify(response)


@app.route('/language_data')
def language_data():
    rows = []
    for row in list(db.view('language/LanguageDistribution',group = True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value}]})

    response = {
        'cols': [{'id': 'language', 'label': 'language', 'type': 'string'},
                 {'id': 'numbers', 'label': 'users', 'type': 'number'}],
        'rows': rows
    }

    return jsonify(response)

@app.route('/sourceDistribution_data')
def sourceDistribution_data():
    rows = []
    for row in list(db.view('source/SourceEquipment', group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value}]})

    response = {
        'cols': [{'id': 'source', 'label': 'source', 'type': 'string'},
                 {'id': 'numbers', 'label': 'users', 'type': 'number'}],
        'rows': rows
    }

    return jsonify(response)

@app.route('/hour_data_avg')
def hour_data_avg():
    rows = []
    for row in list(db2.view('24HourHappiness/24Hour', group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value[0]}, {'v': row.value[1]}]})

    response = {
        'cols': [{'id': '24hour', 'label': '24hour', 'type': 'string'},
                 {'id': 'avg_polarity', 'label': 'avg_polarity', 'type': 'number'}],
        'rows': rows
    }

    return jsonify(response)

@app.route('/hour_data_number')
def hour_data_number():
    rows = []
    for row in list(db2.view('24HourHappiness/24Hour', group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value[1]}]})

    response = {
        'cols': [{'id': '24hour', 'label': '24hour', 'type': 'string'},
                 {'id': 'number', 'label': 'number_of_tweets', 'type': 'number'}],
        'rows': rows
    }

    return jsonify(response)

@app.route('/weather_data_avg')
def weather_data_avg():
    rows = []
    for row in list(db.view('Weather/BadWeather', group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value[0]}]})

    response = {
        'cols': [{'id': 'BadWeather', 'label': 'BadWeather', 'type': 'string'},
                 {'id': 'avg_polarity', 'label': 'avg_polarity', 'type': 'number'}],
        'rows': rows
    }
    return jsonify(response)

@app.route('/weather_data_number')
def weather_data_number():
    rows = []
    for row in list(db.view('Weather/BadWeather', group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value[1]}]})

    response = {
        'cols': [{'id': 'BadWeather', 'label': 'BadWeather', 'type': 'string'},
                 {'id': 'number', 'label': 'number_of_tweets', 'type': 'number'}],
        'rows': rows
    }
    return jsonify(response)

@app.route('/sport_data_avg')
def sport_data_avg():
    rows = []
    for row in list(db.view('Sport/AFL', group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value[0]}]})

    response = {
        'cols': [{'id': 'AFL', 'label': 'AFL', 'type': 'string'},
                 {'id': 'avg_polarity', 'label': 'avg_polarity', 'type': 'number'}],
        'rows': rows
    }
    return jsonify(response)

@app.route('/sport_data_number')
def sport_data_number():
    rows = []
    for row in list(db.view('Sport/AFL', group=True)):
            rows.append({'c': [{'v': row.key}, {'v': row.value[1]}]})

    response = {
        'cols': [{'id': 'AFL', 'label': 'AFL', 'type': 'string'},
                 {'id': 'number_of_tweets', 'label': 'number_of_tweets', 'type': 'number'}],
        'rows': rows
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)