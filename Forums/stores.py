import itertools
# you can lerun more abut itertools in this :https://docs.python.org/2/library/itertools.html
#----------------------------------------------------------------------------------------------------
class BaseStore():
	def __intit__(self, data_provider, last_id):
		self._data_provider = data_provider
		self._last_id = last_id

	def add(self, itme_instance):
		itme_instance.id = self._last_id
		self._data_provider.append(itme_instance)
		self._last_id += 1

	def get_all(self):
		return self.data_provider

	def get_by_id(self, id):
		for instance in self.get_all():
			if instance.id == id:
				return instance
		return None

	def update(self, update_instance):
		instance = self.get_all()
		for index, instance in enumerate(instance):
			if instance.id == update_instance.id:
				instance[index] = update_instance
	def delete(self, id):
		instance = self.get_by_id(id)
		if instance is not None:
			self._data_provider.remove(instance)

	def entity_exists(self, instance):
		if instance is not None:
			return True
		return False
#-----------------------------------------------------------------------------------------------
class MemberStore(BaseStore):
	members = []
	last_id =1	

	def __init__(self):
		super(MemberStore,self).__init__(MemberStore.members, MemberStore.last_id)

	def get_by_name(self,member_name):
		all_members = self.get_all()

		for member in all_members:
			if member.name == member_name:
				yield member
	def get_members_with_posts(self,all_posts):
		all_members = copy.deepcopy(self.get_all())
		for member, post in itertools.product(all_members, all_posts):
			if member.id == post.member_id:
				member.posts.append(post)

		for member in all_members:
			yield member
	def get_top_two(self, all_posts):
		members_with_posts = list(self.get_members_with_posts(all_posts))
		members_with_posts.sort(key=lambda member: len(member.posts), reverse=True)

		yield members_with_posts[0]
		yield members_with_posts[1]
# -----------------------------------------------------------------------------------------
class PostStore(BaseStore):
	posts = []
	last_id = 1
	def __init__(self):
		super(PostStore, self).__init__(PostStore.posts, PostStore.last_id)
	def get_posts_by_date(self):
		posts = self.get_all()
		posts.sort(key=lambda post: post.date, reverse=True)
		return posts

