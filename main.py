from facebook_scraper import get_posts




if __name__ == '__main__':


    posts = []
    for post in get_posts("DRNyheder", options={"comments":True,"progress":True, "sleep":10}):
        posts.append(post)

    print(posts[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
