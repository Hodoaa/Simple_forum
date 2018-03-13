
import models, stores
from time import sleep

def create_members():
    member1 = models.Member("Ali", 45)
    member2 = models.Member("Mo'men", 13)
    member3 = models.Member("mazen", 19)
    member4 = models.Member("mona", 33)

    return member1, member2, member3, member4


def store_members(members, store):
    for member in members:
        store.add(member)


def print_all_members(store):
    for member in store.get_all():
        print (member)

    print ("=" * 9 + " Print All Members " + "=" * 9)


def create_posts():
    post1 = models.Post("1st Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 1)
    sleep(0.1)
    post2 = models.Post("2nd Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", 3)
    sleep(0.1)
    post3 = models.Post("3rd Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 2)
    sleep(0.1)
    post4 = models.Post("4th Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 4)
    sleep(0.1)
    post5 = models.Post("5th Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", 1)
    sleep(0.1)
    post6 = models.Post("6th Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 3)
    sleep(0.1)
    post7 = models.Post("7th Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 1)
    sleep(0.1)
    post8 = models.Post("8th Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", 3)
    sleep(0.1)
    post9 = models.Post("9th Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 1)

    return post1, post2, post3, post4, post5, post6, post7, post8, post9


def update_member(member, store):
    copy = models.Member(member.name, member.age)
    copy.id = member.id
    print (member)
    print (copy)
    copy.name = "Manar"
    store.update(copy)
    print (store.get_by_id(member.id))
    print ("=" * 11 + " Update Member " + "=" * 11)


def search_members_by_name(name, store):
    results = store.get_by_name("Manar")
    for member in results:
        print (member)
    print ("=" * 10 + " Search Members " + "=" * 10)


def view_members_with_posts(store, posts):
    members_with_posts = store.get_members_with_posts(posts)
    for member in members_with_posts:
        print ("{0} has posts".format(member.name))
        for post in member.posts:
            print ("\t{0}".format(post.title))
    print("=" * 20)


def view_top_members_with_posts(store):
    top_members_with_posts = store.get_top_members_with_posts()
    for member in top_members_with_posts:
        print ("{0} has {1} posts".format(member.name, len(member.posts)))
    print("=" * 20)


def store_posts(posts, store):
    for post in posts:
        store.add(post)


def view_posts_by_date(store):
    posts_by_date = store.get_posts_by_date()
    for post in posts_by_date:
        print ("{0} created at {1}".format(post.title, post.date))
    print("=" * 20)


members = create_members()
member_store = stores.MemberStore()
store_members(members, member_store)
# print_all_members(member_store)
# update_member(members[3], member_store)
# search_members_by_name("Manar", member_store)

posts = create_posts()
post_store = stores.PostStore()
store_posts(posts, post_store)

# view_mem
store_should_get_top_two(member_store, post_store)