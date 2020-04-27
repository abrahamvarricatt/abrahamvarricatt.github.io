Note 2 self:

#######################
How to do a clean setup
#######################

1. Clone this repository
2. Clone the pelican plugins repository locally ``git clone --recursive https://github.com/getpelican/pelican-plugins``


##################
Writing a new post
##################

1. Make a new file inside the ``content/articles/20XX`` folder
2. You can preview the post via ``$ make devserver``
3. Visit http://localhost:8000/ to check new post1
4. You can kill the local server via ``$ make stopserver``

##########
Publishing
##########

After saving the changes, you can use the following to deploy to github pages,

$ make github
