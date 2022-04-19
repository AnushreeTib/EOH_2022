from flask import Flask, request, render_template
from flask import Flask

from backend import output, preprocess
app = Flask(__name__)

@app.route("/")
def main():
  return render_template('index.html', test = "")

@app.route("/", methods = ['post'])
def POST_text():
  text = request.form['to_summarise']
  sentence_number = None
  # sentence_number = request.form['sentence_number']
  
  if len(text) > 0:
    if sentence_number:
      out = output(text, summary_sentence_count = sentence_number)
    else:
      out = output(text)
    print(out)

    return render_template('index.html', out = out, text = text), 200
    
  else: 
    return render_template('index.html'), 200