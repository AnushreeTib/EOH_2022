from flask import Flask, request, render_template
from flask import Flask

from backend import output, preprocess
app = Flask(__name__)

@app.route("/")
def main():
  return render_template('index.html', test = "")

@app.route("/", methods=['post'])
def POST_text():
  #print("hello")    
  text = request.form['to_summarise']
  
  if len(text) > 0:
    out = output(text)

    return render_template('index.html', out = out, text = text), 200
    
  else: 
    return render_template('index.html'), 200