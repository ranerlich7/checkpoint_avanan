import json
import bisect
import time
# from flask import Flask, jsonify, request

# app = Flask(__name__)

from fastapi import FastAPI, HTTPException, Body

app = FastAPI()


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
    print(interval,word_arr[index_of_start:])
    return sum(occurrence[1] for occurrence in word_arr[index_of_start:])

    
def get_words(interval):
    data = {
        'email' : count_word(words['email'], interval),
        'checkpoint' :count_word(words['checkpoint'], interval),
        'avanan' :count_word(words['avanan'], interval),
        'security':count_word(words['security'], interval)
    }
    return data
    
    
@app.get("/stats")
async def stats(interval: int):
    try:
        interval = int(time.time()) - interval
        return_data = get_words(interval)
        return return_data
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input provided")

    
def count_and_update(sentence, phrase, now_time):
    print(f"sentence:{sentence}, phrase:{phrase},now_time:{now_time}")
    tmp_count = sentence.count(phrase)
    print(f"tmp_count:{tmp_count}")
    print(f"words:{words}")
    if tmp_count > 0:
        words[phrase].append((now_time, tmp_count))
    
def get_events(sentence, current_time):
    count_and_update(sentence, 'email', current_time)
    count_and_update(sentence, 'checkpoint', current_time)
    count_and_update(sentence, 'avanan', current_time)
    count_and_update(sentence, 'security', current_time)
    

@app.post("/events")
async def events(sentence: str = Body(..., media_type="text/plain")):
    current_time = int(time.time())
    get_events(sentence.lower(), current_time)
    return {'message': 'Updated successfuly'}


