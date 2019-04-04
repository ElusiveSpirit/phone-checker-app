import rq
from flask import Flask, request, jsonify
from redis import Redis

app = Flask(__name__)

queue = rq.Queue('normal', connection=Redis.from_url('redis://redis:6379'))


@app.route('/phone-process', methods=['POST'])
def phone_process_post():
    """Started site analysing process in redis queue
    """
    data = request.json
    if 'url' not in data:
        return jsonify(error='field \'url\' is required'), 400

    job = queue.enqueue('app.scrapper.find_phones', data['url'])

    return jsonify(task_id=job.get_id()), 201


@app.route('/phone-process', methods=['GET'])
def phone_process_get():
    """Get phone process result
    """
    data = request.args
    if 'task_id' not in data:
        return jsonify(error='field \'task_id\' is required'), 400

    job = queue.fetch_job(data['task_id'])
    if not job:
        return jsonify(error='Job not found'), 404

    status = job.get_status()
    if job.is_finished:
        return jsonify(status=status, phone_numbers=job.result)

    return jsonify(status=status)
