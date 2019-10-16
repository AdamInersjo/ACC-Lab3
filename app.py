#!flask/bin/python
from flask import Flask, jsonify, request, abort

from tasks import celery_app, count_words

app = Flask(__name__)

BASE_URL = '/wordcount/api/v1.0'

@app.route(BASE_URL + '/count', methods=['POST'])
def count():
    content = request.json
    if 'words' not in content.keys():
        abort(400, "Missing parameter 'words'")
    words = content['words']


    task = count_words.delay(words)
    return {'task_id': task.id}

@app.route(BASE_URL + '/status/<task_id>', methods=['GET'])
def status(task_id):
    print(task_id)
    task = count_words.AsyncResult(task_id)
    ready = task.ready()
    if ready:
        return {'status': task.status, 'result': task.get()}
    return {'status': task.status}


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)