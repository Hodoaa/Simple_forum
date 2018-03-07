class Member:
	def __init__(self,name,age):
		self.name = name
		self.age = age
class MemberStore():
	members = []
	def add(self,member):
		MemberStore.members.append(member)
	def get_all(self):
		return MemberStore.members
class Post:
	def __init__(self,Post_Title,Post_Content):
		self.Post_Title = Post_Title
		self.Post_Content = Post_Content
class PostStore():
	posts = []
	def add(self,post):
		PostStore.posts.append(post)
	def get_all(self):
		return PostStore.posts