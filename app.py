import sample
import word_analyzer
import file_reader
from flask import Flask

app = Flask(__name__)

@app.route('/')
def app(environ, start_response):
    words = file_reader.get_words_only('./corpus/holmes.txt')
    histogram = word_analyzer.histogram(words)
    word = sample.get_sample_from(histogram)

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(word)))
    ])
    return iter([word])


if __name__ == '__main__':
    app.run()
