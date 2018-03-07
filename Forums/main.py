import models
#-----------------------------------------------------
#Creating Members
#-----------------------------------------------------
member1 = models.Member("member1",25)
member2 = models.Member("member2",35)
#-----------------------------------------------------
#ending of create mebers
#-----------------------------------------------------
#Creating Posts
#-----------------------------------------------------
post1 = models.Post("post1","Content1")
post2 = models.Post("post2","Content2")
post3 = models.Post("post3","Content3")
#-----------------------------------------------------
#ending of create posts
#-----------------------------------------------------
members_store = models.MemberStore()
members_store.add(member1)
members_store.add(member2)
#-------------------------------------------------------
post_store = models.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)


