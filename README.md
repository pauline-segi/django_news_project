# Plus Resources: Django Project Starter

Starter code for the Plus Django project.


# {{ Pauline Segi }} - She Codes News Project


## About This Project

{{ We created a website for She Codes News using the github project template as a base line. From there, we made changes to the code by modifying views, models, forms and url files, as well as a few html files for the story. 

We used a News app to hold the stories, there were some already populated, and then created a section so users could add their own stories. 

We then created a Users app to allow users to create an account. This required a login/logout section which was created as well. From here, I modified the users app to allow users to view their profile. This is very basic and no css has been added. 

I then decided to add a Comments section to the stories. I don't know why I decided this, just got caught up in the moment. It works in a sense that the comments are added to the database, but I just couldn't figure out how to get the comments to display on the story page. 

We were asked to change the css file to make the site look awesome, but I just could not find the time to do this. I struggled on the comments section (think I went down a wormhole --- and really shouldn't have seem so much time on it as I did...) and by the end of it I just couldn't find the stamina to start working on the css. }}


## How To Run This Code

{{
Open a new terminal window. 



Give a quick step-by-step guide on how to download and run your codebase.

It's ok to assume the reader is another developer here, so don't feel like you have to explain what a virtual environment is, etc.

Give directions like "clone the repo to your local machine", "create a virtual environment", "migrate the database", etc.

When you need to specify terminal commands, you can surround them with backticks, like so: `python manage.py runserver`. This formats them as code in the markdown document. (The backtick key is to the left of the number 1 at the top of your keyboard.)

}}


## Database Schema!

[ {{ My ERD }} ]( {{ ./she_codes_news/news/static/news/images/erd.drawio.png }} )


## Project Features

- [ ] Order stories by date
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Styled "new story" form
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
    
- [ ] Story images
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Log-in/log-out
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Account view" page
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Create Account" page
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] View stories by author
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Create Story" functionality only available when user is logged in
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )


## Additional Features:

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