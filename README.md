# Plus Resources: Django Project Starter

Starter code for the Plus Django project.


# {{ Pauline Segi }} - She Codes News Project


## About This Project

{{ 

We created a website for She Codes News using the github project template as a base line. From there, we made changes to the code by modifying views, models, forms and url files, as well as a few html files for the story. 

We used a News app to hold the stories, there were some already populated, and then created a section so users could add their own stories. 

We then created a Users app to allow users to create an account. This required a login/logout section which was created as well. From here, I modified the users app to allow users to view their profile. This is very basic and no css has been added. 

I then decided to add a Comments section to the stories. I don't know why I decided this, just got caught up in the moment. It works in a sense that the comments are added to the database, but I just couldn't figure out how to get the comments to display on the story page. 

We were asked to change the css file to make the site look awesome, but I just could not find the time to do this. I struggled on the comments section (think I went down a wormhole --- and really shouldn't have seem so much time on it as I did...) and by the end of it I just couldn't find the stamina to start working on the css. 

}}


## How To Run This Code

{{
Open a new terminal window. 

You'll then want to head to the directory you want your project to be stored. 

Then you can clone the github repo by entering: 
git clone — then paste the repository link here In this case:
`git clone https://github.com/pauline-segi/django_news_project.git`

Once you're set here, you'll want to activate the Virtual Environment.

This step will need to be performed every time you work a Django project!

Jump back to the terminal, and make sure you’re in the folder that contains your requirements.txt file

On Mac, run this command:
`source venv/bin/activate`

Then head to the folder you want to run and enter this:
`python3 manage.py runserver`

Once you've made any big changes, you can migrate your database. To do this first enter:
`python3 manage.py makemigrations`

Then: 
`python3 manage.py migrate`

If you ever need to load new data to your webpage, you can use:
`python3 manage.py loaddata news`

When you're ready to commit any changes, run through these steps in terminal:

'git add .'        
This is putting together my draft of files I am adding to git — so it’s saying everything in this folder I want to add

'git status'
shows the list of files it wants to add

'git commit -m “Example Commit Code”'
( -m means message) ---- in this section you can write any bit of helpful code you can to help you remember what it is (so like uploading my work in progress or something)

'git push'
When ready to push, just type in

Then if you need to pull your code you can, as long as you’re in the project folder, so for example you need to be in the django_news_project folder in terminal, and then just write ‘git pull’ to update the folder:
'git pull'

Some helpful paths to navigate in the directory:

mkdir  — makes a new directory
mv — move
pwd — path in the directory of where you are now
cd .. — means go back a level
cd --- take you back to the home level
}}


## Database Schema!

[ {{ My ERD }} ]( {{ ./she_codes_news/news/static/news/images/erd.drawio.png }} )


## Project Features

- [x] Order stories by date
    ![ {{ This is showing the News stories sorted by date }} ]( {{ ./img/4-Sorted-by-date.png }} )

- [ ] Styled "new story" form
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
    
- [x] Story images
    ![ {{ Added some static images }} ]( {{ ./she_codes_news/news/static/news/images }} )

- [x] Log-in/log-out
    ![ {{ Created a login/logout button on the menu }} ]( {{ ./img/1-Home-page.png}} )

- [x] "Account view" page
    ![ {{ Allowed user to view their profile page }} ]( {{ ./img/3-Profile-page.png }} )

- [x] "Create Account" page
    ![ {{ Allowed users to create a new account }} ]( {{ ./img/7-Create-Account.png}} )

- [ ] View stories by author
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] "Create Story" functionality only available when user is logged in
    ![ {{ Allow users to write and publish their own story. }} ]( {{ ./img/6-Write-your-story.png }} )


## Additional Features:

- [x] Add comments to the stories.
    ![ {{ Allow users to add comments to stories (this function is not working properly) }} ]( {{ ./img/5-Have-your-say.png }} )

- [ ] Add categories to the stories and allow the user to search for stories by category.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to update and delete stories (consider permissions - who should be allowed to update or and/or delete stories).
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to “favourite” stories and see a page with your favourite stories.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Our form for creating stories requires you to add the publication date, update this to automatically save the publication date as the day the story was first published (maybe you could then add a field to show when the story was updated).
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Gracefully handle the error where someone tries to create a new story when they are not logged in.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )