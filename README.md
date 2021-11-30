# mini-twitter
This README file documents the routes, design considerations made, and collaborators. The file also includes information on how to run the server.

collaborators: Akshat Shah, Yiwei(Ellen) Yan
## installation
you can install dependencies with the following
```
poetry install
```

## how to run the server: 

```
cd twitter

poetry run python3 manage.py makemigrations

poetry run python3 manage.py migrate

poetry run python3 manage.py runserver
```

## routes:
* '/admin': access the admin page to the server
* '/' : the landing page where the user have the option to the login page and the signup page
* '/login' :  user login page, can access the sign up page here, if logged in, redirects to '/feed'
* '/logout' : returns to the landing page 
* '/signup' : sign up page, redirects to /feed
* '/feed' : the home page, user needs to be logged in to see its contents
    * if not logged in, a refresh leads to login page
    * display posts in reverse chronological order, allow likes 
    * if the current user is the creator of a tweet, the post offers a link to delete it
    * provides a link for visiting each post's creator's profile
    * provides a link for logging out
    * allows creation of a new post though hyperlink "Create a Post"
* '/feed/<str:hashtag>': display the tweets which includes the hashtag word 
    * display posts in reverse chronological order, allow likes 
    * provides a link for visiting each post's creator's profile
    * if the current user is the creator of a tweet, the post offers a link to delete it
    * provides a link for logging out
* '/posts': add the new post to database if valid, find tags within the content and save the tags in a separate database column, return to home page. If the post invalid, refresh to the same page
* '/<str:username>': display the tweets of the specifc user
    * display posts in reverse chronological order, allow likes 
    * provides a link for visiting each post's creator's profile
    * if the current user is the creator of a tweet, the post offers a link to delete it
    * provides a link for logging out
* '/delete/<post_id>': delete the post in the database and redirects to home page

