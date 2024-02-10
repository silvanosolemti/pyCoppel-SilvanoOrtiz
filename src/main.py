from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/search/<search_query>")
def get_search(search_query):
    url = 'http://api.tvmaze.com/search/shows?q=' + search_query
    data = requests.get(url)

    data_list = []

    if data.status_code == 200:
        data = data.json()
        for item in data:
            item = json.dumps(item['show'])
            new_json = json.loads(item)
            array_data = {'id':None, 'name':None, 'channel':None, 'summary':None, 'genres':None}
            array_data['id'] = new_json['id']
            array_data['name'] = new_json['name']

            channel = json.dumps(new_json['network'])
            channel = json.loads(channel)
            array_data['channel'] = channel['name']
            array_data['summary'] = new_json['summary']
            array_data['genres'] = new_json['genres']
            data_list.append(array_data)

    return jsonify(data_list), 200


@app.route("/show/<show_id>")
def get_show(show_id):
    url = 'https://api.tvmaze.com/shows/' + show_id
    data = requests.get(url)


    return jsonify(data.json()), 200

if __name__ == "__main__":
    app.run(debug = True)