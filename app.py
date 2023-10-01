import json
import bisect
import time
from flask import Flask, jsonify, request

app = Flask(__name__)


words={
    'email' : [],
    'checkpoint' :[],
    'avanan' :[],
    'security':[]
}

# help function to bisect
key_func = lambda x: x[0]

# sum the number of times from the tuples in the dictionary
# for example 'email' : [(timestamp,2),(timestamp2,1)...]
def count_word(word_arr, interval):
    timestamps = [occurrence[0] for occurrence in word_arr]
    # using binary search find the index of the interval o(n)
    index_of_start = bisect.bisect_left(timestamps, interval)
    return sum(occurrence[1] for occurrence in word_arr[index_of_start:])

    
def get_words(interval):
    data = {
        'email' : count_word(words['email'], interval),
        'checkpoint' :count_word(words['checkpoint'], interval),
        'avanan' :count_word(words['avanan'], interval),
        'security':count_word(words['security'], interval)
    }
    return data
    
    
@app.route("/stats", methods=['GET'])
def stats():
    try:
        interval = int(time.time()) - int(request.args.get('interval'))
        return_data = get_words(interval)
        return jsonify(return_data), 200
    except ValueError:
        return jsonify({'error': 'Bad Request', 'message': 'Invalid input provided'}), 400
    
def count_and_update(sentence, phrase, now_time):
    tmp_count = sentence.count(phrase)
    words[phrase].append((now_time, tmp_count))
    
    
@app.route("/events", methods=['POST'])
def events():
    current_time = int(time.time())
    sentence = request.get_data(as_text=True).lower()
    count_and_update(sentence, 'email', current_time)
    count_and_update(sentence, 'checkpoint', current_time)
    count_and_update(sentence, 'avanan', current_time)
    count_and_update(sentence, 'security', current_time)
    return jsonify({'message': 'Updated successfuly'}), 200


if __name__ == '__main__':
    app.run(debug=True)