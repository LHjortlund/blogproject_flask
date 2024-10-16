import requests

BLOG_URL = "https://api.npoint.io/c10781c59f247ee64d13"

class Post:
    def get_post(self, index=None):
        response = requests.get(BLOG_URL)
        all_posts = response.json()
        if index is not None:
            return [all_posts[index]]
        return all_posts