import itertools
# you can lerun more abut itertools in this :https://docs.python.org/2/library/itertools.html

class MemberStore():
	members = []
	last_id =1	# here counter for members
	def get_all(self):	#this function to display all members in member list
		return self.members
	#----------------------------Adding a member------------------------------------------------
	def add(self,member):
		member.id = MemberStore.last_id #adding id number for eatch member
		MemberStore.members.append(member) # update member list after adding any member
		MemberStore.last_id += 1 #after the first member take her id increase the counter one 
	#--------------------------Updating Member list ---------------------------------------------
	def update(self,member):
		all_members = self.get_all()
		for index, current_member in enumerate(all_members):
			if current_member.id == member.id:
				all_members[index] = member
				break
	#------------------------deleteing member by it's id-----------------------------------------------------
	def delete(self,id):
		member_to_delete = self.get_by_id(id)
		self.members.remove(member_to_delete)
	#-------------------------------------------------------------------------------
	def entity_exists(self,member):
		result = True
		if self.get_by_id(member.id) is None:
			result = False
		return result

	#----------------this funcation to finde amember by its id-----------------------
	def get_by_id(self,id): 
		all_members = self.last_id 
		result = None
		for member in self.members:
			if member.id == id:
				result = member
				break
			return result
	#--------------------Finde Member by name----------------------------------------
	def get_by_name(self,name):
		all_members = self.get_all()
		return (member for member in all_members() if member.name == name)
	#----------------------Findeg members and her posts----------------------------------------
	def get_member_with_posts(self,posts):
		members = self.get_all()
		for member, post in itertools.product(members, posts):
			if post.member_id == member.id:
				member.posts.append(post)
		return members
	#-------------------------------Displayin the top two member -------------------------------------------------	
	def get_top_two(self,post_store):
		all_members = self.get_member_with_posts(post_store)
		sorted_member = sorted(all_member, key=lambda x: len(x.posts), reverse=True)
		return sorted_member[2]
# -----------------------------------------------------------------------------------------
class PostStore():
	posts = []
	last_id = 1
	def get_all(self):
		return PostStore.posts
	#---------------------------------------------------------
	def add(self,post):
		post.id = self.last_id
		PostStore.posts.append(post)
		self.last_id += 1
	#-----------------Finding post by post_id----------------------------------------------
	def get_by_id(self,id):
		post = None
		for e in self.posts:
			if e.id == id:
				post = e
				break
		return post
	#-------------------delete post by post_id-----------------------
	def delelte(self,id):
		post_to_delete = self.get_by_id(id)
		self.posts.remove(post_to_delete)
	#------------------chek exists posts------------------------------
	def entity_exists(self,post):
		result = False
		if self.get_by_id(post.id) == post:
			result = True
		return result


