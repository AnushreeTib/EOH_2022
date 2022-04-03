from flask import Flask, request, render_template
from flask import Flask

from backend import output, preprocess
app = Flask(__name__)

@app.route("/")
def main():
  return render_template('index.html', test = "")
@app.route("/", methods=['post'])
def firstPagePost():
    
  text = input()
  
  if len(text) > 0:
    out = output(text)
    print(out)
    
    return render_template('index.html', out = out, text = text) 
    
  else: 
    return render_template('index.html')