from flask import Flask
import redis
import os
import time

app = Flask(__name__)

# Koneksi ke Redis. Host menggunakan nama service di docker-compose
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Halo! Aplikasi ini telah dikunjungi sebanyak {count} kali.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
