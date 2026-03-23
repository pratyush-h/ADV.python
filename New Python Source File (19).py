class Post:
    total_posts = 0
    
    def __init__(self, content):
        self.content = content
        self.comments = []
        Post.total_posts += 1
    
    def __str__(self):
        # This defines what happens when you call print(post_object)
        return f"Post: {self.content} ({len(self.comments)} comments)"

class Comment:
    def __init__(self, text):
        self.text = text

# --- ACTION STEPS TO GET OUTPUT ---

# 1. Create a new Post object
my_post = Post("Hello world, this is my first post!")

# 2. Create a Comment object
new_comment = Comment("Great post!")

# 3. Add the comment to the post's list
my_post.comments.append(new_comment)

# 4. Print the post (this triggers the __str__ method)
print(my_post)

# 5. Check the class variable
print(f"Total posts created: {Post.total_posts}")