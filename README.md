# SocialBot
SocialBot is an API created using fastapi where users can login, signup to the site and can create their post, read/get all the post, update their post and delete their post.

![ui](https://user-images.githubusercontent.com/69014454/162633411-bb8a996c-5e7b-4d18-a7da-e1ec4280e415.jpg)

# Creating a user
A user can create his profile by signing in to the socialbot site.If the user is sucessfully created a status code along with the users credentials are generated.

![create user](https://user-images.githubusercontent.com/69014454/162633497-8daeb002-5e4c-451e-b169-c3d38050c493.jpg)

# Loging in the User
A user is logged in by authenticating him using the JWT TOKEN.If the user is authorized successfully a status code is generated.

![login user](https://user-images.githubusercontent.com/69014454/162633668-7a066b44-7284-4e2c-86bd-d26eaf629431.jpg)

# Creating a Post
A user which is authorized can create their post.A successful creation of post will generate status code accordingly.

![create post](https://user-images.githubusercontent.com/69014454/162633723-74d81650-f894-4f2b-b58b-046f0f715fb6.jpg)

# Reading/Get the post
A user can either get all the post or single post.A user can limit the no of post, skip some post and search for the post with the given keyword.

![get post](https://user-images.githubusercontent.com/69014454/162633862-a4ed00c3-ae28-4fd0-a6b0-22b5b2c53af4.jpg)

# Update the post
A user can update their post and status code is generated accordingly.

![update post](https://user-images.githubusercontent.com/69014454/162633893-a8f83b45-261c-4353-8f57-a254393d5f6c.jpg)

# Deleting the post
A successful status code of 204 is generated when the post is deleted successfully.

![delete post](https://user-images.githubusercontent.com/69014454/162633918-27f1a30c-4dc7-4525-b02d-3b6324013632.jpg)

# Vote on the post
A user can vote on his post or some other post accordingly.A dir pointer has been used to tell the user if they successfully voted or not(1 means yes, 0 means no)

![vote](https://user-images.githubusercontent.com/69014454/162633964-c41ff08f-efa0-428f-b2d6-5d3fa1b23bf5.jpg)

