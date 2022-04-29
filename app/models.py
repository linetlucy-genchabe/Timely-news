
  
class Source:
	'''
	Source Class to define Source Objects
	'''
	def __init__(self,id,name,description,url,category):
		'''
		Function to initialize Source Objects
		It defines the properties each Source object will hold.
	
		'''
		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.category = category

class Article:
	'''
	Article Class to define Article Objects
	'''
	def __init__(self,author,title,description,url,image,date):
		'''
		Function to initialize Article Objects
		It defines the properties each Article object will hold.
	
		'''
		self.author = author
		self.title = title
		self.description = description
		self.url = url
		self.image = image
		self.date = date