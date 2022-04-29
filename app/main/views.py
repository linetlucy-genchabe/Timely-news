from flask import render_template
from . import main
from ..request import get_sources,get_articles

# Views
@main.route('/')
def index():
	'''
	View Function that returns the index page and its data
	'''
	# Getting sources according to category
	business_sources = get_sources('business')
	general_sources = get_sources('general')
	sport_sources = get_sources('sport')
	entertainment_sources = get_sources('entertainment')
	technology_sources = get_sources('technology')

	title = 'Home - Find the latest news highlights'

	return render_template('index.html', title=title,business=business_sources,general=general_sources,entertainment=entertainment_sources,sport=sport_sources,technology=technology_sources)

@main.route('/source/<id>')
def source(id):
	'''
	View Function that returns the source page and its data
	'''
	# Getting articles according to source chosen
	articles = get_articles(id)
	source_id = id.upper()
	title = f'{source_id} - Top Articles'

	return render_template('source.html',title=title,id=source_id, articles=articles)