import urllib.request,json
from .models import Source,Article

# Getting Api Key
api_Key = None
#Getting the base urls
sources_base_url = None
articles_base_url = None

def configure_request(app):
	'''
	Function to acquire the api key and base urls
	'''
	global api_Key,sources_base_url,articles_base_url
	api_Key = app.config['NEWS_API_KEY']
	sources_base_url = app.config['NEWS_SOURCES_BASE_URL']
	articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']

def get_sources(category):
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = sources_base_url.format(category)

	with urllib.request.urlopen(get_sources_url,data=None) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)
		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)

	return sources_results

def process_sources(sources_results):
	'''
	Function  that processes the sources result and transform them to a list of Objects
	Args:
	sources_results: A list of dictionaries that contain sources details
	Returns :
	sources_list: A list of sources objects
	'''
	sources_list = []
	for source_item in sources_results:
		id = source_item.get('id')
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')

		source_object = Source(id,name,description,url,category)
		sources_list.append(source_object)

	return sources_list

def get_articles(source):
	'''
	Function that gets the json response to our url request
	'''
	get_articles_url = articles_base_url.format(source,api_Key)

	with urllib.request.urlopen(get_articles_url,data=None) as url:
		get_articles_data = url.read()
		get_articles_response = json.loads(get_articles_data)
		articles_results = None

		if get_articles_response['articles']:
			articles_results_list = get_articles_response['articles']
			articles_results = process_articles(articles_results_list)

	return articles_results

def process_articles(articles_results):
	'''
	Function  that processes the articles result and transform them to a list of Objects
	Args:
	    articles_results: A list of dictionaries that contain articles details
	Returns :
	    articles_list: A list of articles objects
	'''
	articles_list = []
	for article_item in articles_results:
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')

		if date and author and image:
			article_object = Article(author,title,description,url,image,date)
			articles_list.append(article_object)

	return articles_list