class WebPage(object):
	"""Class representing a WebPage which is stored in the LRU cache"""
	def __init__(self,name,url,visits):
		self.name=name
		self.url=url
		self.visits=0
	
	def visitPage(self):
		self.visits+=1

class WebBrowser(object):
	"""class to represent a WebBrowser"""
	def __init__(self):
		self.cache = LRU_Cache(5)
		self.history = History(5)

	def visitPage(self, page):
		print("Visiting ",page.name)
		if self.cache.get_page(page.name):
			print("Loading from {}...".format(self.cache.get_page(page.name)))
		else:
			print("Not found in cache. Inserting into cache")
			self.cache.insertPage(page)
		self.history.visitPage(page)
import heapq
class History(object):
 	"""docstring for History"""
 	def __init__(self,k):
 		self.top = []
 		self.capacity = k
 		self.curr_size = 0
 		self.map = {}
 		self.top_map = {}
 	def updateHeapEntry(self,name):
 		for i,entry in enumerate(self.top):
 			if entry[1]==name:
 				self.top.pop(i)
 		heapq.heappush(self.top,(self.map[name],name))

 	def updateHeap(self,name):
 		print("Updating heap for",name)
 		try:
	 		print(self.top[0],self.map[name])
	 	except:
	 		pass
 		if self.curr_size<self.capacity:
 			print("a") 
 			if not self.top_map.get(name):
				self.top_map[name]=True
	 			heapq.heappush(self.top,(self.map[name],name))
	 			self.curr_size+=1
 		
 		elif self.top_map.get(name):
 			print("b")
 			self.updateHeapEntry(name)

 		elif self.top[0][0]<self.map[name]:
 			removed = heapq.heappop(self.top)
 			print("Replaced {}".format(removed))
 			heapq.heappush(self.top,(self.map[name],name))
 			self.top_map[name]=True
 			self.top_map[removed[1]]=False


 	def visitPage(self,page):
 		if not self.map.get(page.name):
 			self.map[page.name]=1
 		else:
 			self.map[page.name]+=1
 		self.updateHeap(page.name)

 	def getTopK(self):
 		print(self.top)

class LRU_Cache(object):
	"""Class representing a cache using the least using the least recently used protocol to store WebPages"""
	def __init__(self, size):
		self.size = size
		self.cache = []
		self.map = {}
	def get_page(self,name):
		if self.map.get(name):
			return self.map[name]
		return False

	def is_full(self):
		return len(self.cache)==self.size

	def insertPage(self,page):
		if self.is_full():
			removed = self.cache.pop(0)
			print("removed {} from cache".format(removed))
			self.cache.append(page)
			self.map[removed.name]=False
		else:
			self.cache.append(page)
		self.map[page.name]=page.url


"""
from LRU import WebBrowser,WebPage,History,LRU_Cache 

fb = WebPage("facebook","www.facebook.com",0)
google = WebPage("google","www.google.com",0)
yt = WebPage("youtube","www.youtube.com",0)
net = WebPage("netflix","www.netflix.com",0)
gfg = WebPage("g4g","www.geeksforgeeks,com",0)


chrome = WebBrowser()
chrome.visitPage(fb)
chrome.visitPage(bloom)
chrome.visitPage(net)
chrome.visitPage(yt)
chrome.visitPage(google)
chrome.visitPage(gfg)
chrome.visitPage(fb)
bloom = WebPage("bloom","www.bloomberg.com",0)
chrome.visitPage(bloom)



"""

