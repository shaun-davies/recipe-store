# Recipe Store - Testing details

[Main README.md file](README.md)

[View website in GitHub Pages](https://dashboard.heroku.com/apps/ms3-recipe-store)

## Automated Testing

### Validation services
The following validation services and linter were used to check the validity of the website code.
-[PEP8 Online](https://pep8online.com/) was used to validate Python code.
-[W3C Markup Validation](https://validator.w3.org/) was used to validate HTML.
-[W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.



## Client stories testing

The following section goes through each of the user strories from the UX section of [README.md](README.md)

The aim of the website is to:

1. Be a visually appealing.
    - Use of colourful header image, icons and simple design
2. Be user friendly.
    - Easy to navigate with collapsable navbar which shows links to different pages, bright and bold buttons.
3. Provide a place to discover new recipes.
    - Home page displays all recipes created by users with button to view the recipe.
4. Provide a storage system for users to keep their recipes and display them.
    - Users can go to the Add Cuisine and Add recipe pages to create and store their data.
5. Provide functionality to edit and delete recipes.
    - "Buttons" on the View Recipe page allow user to edit or delete recipes.

## Manual testing
Below is an account of manual testing done.

### Testing undertaken
All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on varying different desktop screen sizes and Iphone and Ipad and in Chrome Developers Tools device simulators on all options and orientations.

#### Pages
1. Navbar
    1. All links on navbar working
2. View Recipe
    1. View Recipe button on recipes working and directs to correct recipe
    2. Edit and Delete buttons on View Page working correctly
3. Cuisines page
    1. Page clearly shows all cuisines stored on the database
4. Add Cuisines page
    1. Form to add a cuisine works correctly and redirects back to Cuisines page
5. New Recipe page
    1. Form inputs all working correctly to add new recipe to the database


### Bugs discovered:
#### Solved bugs

1. __init__.py
- Could not run application. Bug caused by syntax error. “from flask import Flask” was incorrectly typed as “import flask from Flask”.

2. Mobile nav bar would not respond correctly when opened
- When viewed on mobile device nav bar was distorted and did not function properly. Changing the css attributed with guidance from Tutor Assitance the issue was resolved and functioning correctly on all mobile device screen sizes.

3. W3C Validator and PEP8
- Typo issues resolved after using online validators.

#### Unsolved bugs

1. Could not find any bugs during time of deployment.

## Further testing:
1. Asked fellow students, friends and family to look at the site on their devices and report any issues they found.

2. Recipe Store viewed on all devices and orientations available in Chrome DevTools.