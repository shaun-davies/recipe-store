# [Recipe Store](https://dashboard.heroku.com/apps/ms3-recipe-store)

Recipe Store is a simple website with a database which allows users to find new recipes, create and store new recipes and display them and have the ability to edit and delete recipes.


## UX
 
The aim of the website is to:

1. Be a visually appealing.
2. Be user friendly.
3. Provide a place to discover new recipes.
4. Provide a storage system for users to keep their recipes and display them.
5. Provide functionality to edit and delete recipes.

### User stories

As a user, I want:

1. A simple easy to understand the interface.
2. Simple buttons and mechanisms.
3. A place to discover new recipes.
4. A place to safely store and view recipes as well as edit and delete functionality.



### Design Choices

The aesthetic of the website is simple yet visually appealing:


**Colours**

- Tones of blue and white for simplicity and profesionalism and green and yellow accents in header image to provide interest.

**Images**

- One colourful image used throughout for interest and uniformity.

**Forms**

- Basic, easy to use and read for a simplistic look.

**Buttons**

- Uniformed and brightly coloured buttons to stand out against the white background.

**Cards**

- Cards displaying Recipe names and Cuisine names for a simple and modern look. 

**Theme**

- Basic theme 'Freelancer' installed and modified from [Start Bootstrap](https://startbootstrap.com/)

### Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.

- [Homepage Wireframe](../blob/master/recipestore/static/images/readme-images/wireframes/homepage.png)
- [View Recipe Wireframe](../blob/master/recipestore/static/images/readme-images/wireframes/view-recipe-page.png)
- [Edit Recipe Wireframe](../blob/master/recipestore/static/images/readme-images/wireframes/edit-recipe-page.png)
- [New Recipe Wireframe](../blob/master/recipestore/static/images/readme-images/wireframes/new-recipe-page.png)
- [Cuisines Wireframe](../blob/master/recipestore/static/images/readme-images/wireframes/cuisines-page.png)
- [New Cuisine Wireframe](../blob/master/recipestore/static/images/readme-images/wireframes/new-cuisine-page.png)

## Features 

### Existing Features
1. **Create**
- New Recipe and Add Cuisine functions add new data to the database.

2. **Read**
- Display of Recipes and Cuisine names on home and other pages.

3. **Update**
- Edit Recipe function 

4. ** Delete **
- Delete Recipe function

### Features Left to Implement

1. User Registration and Log-in
- Personal accounts for users to edit and/or delete their own recipes. 

2. Search 
- Search functionality for users to search for recipes under any criteria.

3. Modals
- Damage control modals to confirm deletion of recipes.

4. Images
- Input field for users to add image to their recipe.

## Technologies Used 

- This project uses HTML, CSS, Javascript and Python programming languages.
- [Flask](https://flask.palletsprojects.com/)
    - Developer used Flask as a framework.
- [SQLAlchemy](https://sqlalchemy.org/)
    - The project uses SQLAlchemy as a database management system.
- [Bootstrap](https://bootstrapcdn.com/)
    - The project uses Bootstrap to simplify the structure of the website and make the website responsive.
- [Font Awesome](https://www.fontawesome.com/)
    - Icons for this project have been sourced from flaticon.com
- [GitHub](https://github.com)
    - This project uses Github to store and share all project code remotely.
- [Heroku](https://heroku.com)
    - This project was deployed via Heroku.

## Testing

Testing information can be found in seperate [testing.md](testing.md) file.

## Deployment

The code for this website was written in [Gitpod](https://gitpod.io/), pushed to [Github](https://github.com/) and was deployed via [Heroku](https://heroku.com/).

The database used was [SQLAlchemy](https://sqlalchemy.org/)

The following was used to deploy the website:

1. Create a "requirements.txt" file using the command "pip3 freeze --local > requirements.txt"
2. Create a "Procfile" using the command "echo web: python routes.py > Procfile"
3. Push these changes to the repository using "git add -A","git commit -m 'commit message here' then "git push"
4. Ensure a .gitignore file is in the repository
5. Add "env.py" and "pycache/" to .gitignore file to ensure no sensitive information is added to repository
6. Login or sign up to Heroku
7. Click "New" on the top right of the dashboard and select "Create new app"
8. Include an "App name", choose a region and click "Create app"
9. Click the "Deploy" tab and under "Deployment method" select "GitHub"
10. Search to find your GitHub repository and click "Connect". Please note: do not enable automatic deployment yet as this will cause errors
11. Click the "Settings" tab and click "Reveal Config Vars" from Config Vars
12. Enter the key value pairs that match those in your env.py file:

| Key           | Value                      |
| ------------- |:--------------------------:|
| IP            | 0.0.0.0                    |
| PORT          | 5000                       |
| SECRET_KEY    | "secret_key"               |
| DB_URL        | "postgresql:///recipestore"|

13. Go back to the "Deploy" tab and click "Enable Automatic Deployment"
14. Still in the "Deploy" tab under "Manual deploy", select "main"
15. Click "Deploy Branch"
16. Once the app has finished building click "Open App" to open your site.


### How to run this project locally

To clone this project from GitHub:

1. Follow this link to the [Memory Farm GitHub repository](https://github.com/shaun-davies/memory-farm-game).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the url you copied in Step 3.
```console
git clone https://github.com/USERNAME/REPOSITORY
```
7. Press Enter. Your clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://help.github.com/en/articles/cloning-a-repository).

## Credits

- All text in this project was written by the developer.

### Media 

#### Images
- The Header Image was created by Adonyi Gabor and sourced from [Pexels](https://pexels.com).

### Acknowledgements

Special thanks to:
- Kieron from Code Institute Student Care for his help and support which has allowed me to continue learning and to submit my second Milestone Project for Code Institute.

- My mentor Akshat Garg for his guidance and coding knowledge.

- Anna Greaves for her teachings and for allowing me to learn how to structure and format a good readme from her example.

#### Disclaimer
The content of this website, including the images used, are for educational purposes only.