class Member:
	def __init__(self,name,age):
		self.id = 0
		self.name = name
		self.age = age
		self.posts = []
	def __str__(self):
		return "{0}, {1} Years Old".format(self.name, self.age)
class Post:
	def __init__(self,Post_Title,Post_Content,member_id = 0):
		self.id = 0
		self.date = datetime.datetime.now()
		self.Post_Title = Post_Title
		self.Post_Content = Post_Content
		self.member_id = member_id
	def __str__(self):
		return "{0}: {1}...".format(self.Post_Title, self.Post_Content[:10])
