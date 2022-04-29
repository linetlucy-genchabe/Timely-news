from flask import render_template
from app import app

#views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html', id= news_id)