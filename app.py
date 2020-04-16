from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/issue/<topic>")
def render_topic_page(topic):
    topic_2 = topic.replace(" ", "_").lower()
    path = "topics/"+topic_2+"_page.html"
    return render_template(path, topic=topic)
