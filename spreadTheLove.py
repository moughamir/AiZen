from onegram import following, posts, like, followers, follow

fellas = []

# Get the fellas and like thy posty
for fella in following('omnizya'):
  #fellas.append(fella['username'])
  for post in posts(fella['username']):
    like(post)

# Follow the followers
for follower in followers('omnizya'):
  follow(follower['username'])