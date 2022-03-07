from __future__ import print_function
from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_session import Session
from forms import SearchForm
import sys

app = Flask(__name__)
sess = Session()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lucene", methods=['GET', 'POST'])
def lucene():
    search = SearchForm(request.form)
    search_string = search.data['search']
    if request.method == 'POST':
        return lucene_results(search)

    return render_template("lucene.html", form=search)

@app.route("/hadoop", methods=['GET', 'POST'])
def hadoop():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return hadoop_results(search)

    return render_template("hadoop.html", form=search)

@app.route("/lucene_results")
def lucene_results(search):
    results = []
    search_string = search.data['search']
    #print(search.data['search'], file=sys.stdout)
    if search.data['search'] == '':
        flash('Please enter a search query. Try again?')
        return redirect('/lucene')
    if not results:
        flash('No results found. Try again?')
        return redirect('/lucene')
    else:
        #display results
        return render_template('lucene_results.html', results=results)

@app.route("/hadoop_results")
def hadoop_results(search):
    results = []
    search_string = search.data['search']
    #print(search.data['search'], file=sys.stdout)
    if search.data['search'] == '':
        flash('Please enter a search query. Try again?')
        return redirect('/hadoop')
    if not results:
        flash('No results found. Try again?')
        return redirect('/hadoop')
    else:
        #display results
        return render_template('hadoop_results.html', results=results)

if __name__ == "__main__":
    app.secret_key = 'ooga booga'
    app.config['SESSION_TYPE'] = 'filesystem'

    #sess.init_app(app)

    app.run(debug=True)
