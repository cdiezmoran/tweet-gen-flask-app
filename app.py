import sample
import word_analyzer
import file_reader
from flask import Flask

app = Flask(__name__)

@app.route('/')
def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
    #words = file_reader.get_words_only('./corpus/holmes.txt')
    #histogram = word_analyzer.histogram(words)
    #return sample.get_sample_from(histogram)

if __name__ == '__main__':
    app.run()
