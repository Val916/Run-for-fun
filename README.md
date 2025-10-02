# Run-for-fun
Where wild races meet curious souls.

Discover the world’s most extreme, quirky, and unforgettable running events—from desert ultras to cheese-rolling chaos. Whether you're chasing a personal challenge or just exploring for fun, this platform lets you browse, create, and share races that defy the ordinary.


Live link: [# Run-for-fun](https://run-for-fun-b329a2374625.herokuapp.com/)

Table of Contents


UX Design
Colour Scheme
The colour scheme for the site draws inspiration from the natural beauty of Cornwall. The primary colours are shades of blue, reflecting the sea and sky, while secondary colours include white and grey to ensure contrast and readability.


1. First ordered list item
2. Another item
⋅⋅⋅⋅* Unordered sub-list. 
[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

Tables
Tables aren't part of the core Markdown spec, but they are part of GFM and Markdown Here supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3



> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 
_____________________________________________________________


Typography
The site uses the Google Fonts "Inter" for the main text and "Lato" for the headings. These fonts were chosen for their readability and modern appearance.

Imagery
The site uses images that are sourced from the events being displayed. These images are sourced from Cloudinary and are optimised for fast loading times.

User Stories and kanban board
The user stories were used to create a kanban board to track the development of the project. The project was completed using agile methodology, ensuring iterative progress and continuous feedback.




Wireframes
Home Page



ERD Diagram
- visually represents the structure of the database and the relationships between entities (tables).



Features
Existing Features
Home Page - The home page displays a list of events with pagination. The user can click on an event to view the full text.

Event Page - The event page displays the full text of an event. The user can also view comments on the event. If logged in, the user can comment on the event. They can edit and delete their comments.

About Page - The about page displays information about the site. The user can also view a contact form.

Contact Form - The about page displays a contact form.

Navigation Bar - The navigation bar allows the user to navigate the site pages and is provided via Bootstrap.

Response Messages - The user receives messages when they perform an action such as adding a comment.

User Registration - The user can register an account to comment on events.

User Login - The user can log in to comment on events.

User Logout - The user can log out of their account.

Admin Features - The admin can create, read, update and delete events. They can also approve or disapprove comments.

Features Left to Implement
User Profile - The user can view their profile and update their details.

User Password Reset - The user can reset their password.

Search Bar - The search bar allows the user to search for events by tag.

Technologies Used

HTML5 - The structure of the site was created using HTML5.
CSS3 - The styling of the site was created using CSS3.
JavaScript - The site uses JavaScript for interactivity.
Python - The site uses Python for the backend.
Django - The site uses the Django web framework.
Bootstrap - The site uses the Bootstrap framework for styling.
Font Awesome - The site uses Font Awesome for icons.
Google Fonts - The site uses Google Fonts for typography.
Heroku - The site is deployed on Heroku.
PostgreSQL - The site uses a PostgreSQL database.
Cloudinary - The site uses Cloudinary for image hosting.
https://favicon.io/favicon-converter/


How AI Was Used
Artificial Intelligence played a significant role in the development of this project. Here are some ways AI was utilised:

Planning and Design

AI tools like Copilot were used to generate ideas and suggestions for the project. These tools provided insights and recommendations for the website's layout, features, and functionality. This helped streamline the planning and design process and ensure a more user-friendly and engaging final product.

Code Generation

AI tools like GitHub Copilot were used to generate code snippets for various parts of the website. This included HTML structure and CSS styling. The AI provided context-aware suggestions that helped streamline the coding process and reduce development time.

Debugging

AI-powered debugging tools were utilised to identify and fix issues in the code. These tools analysed the codebase, detected potential bugs, and provided recommendations for resolving them. This ensured a smoother development process and a more robust final product.

Accessibility Improvements

AI was used to analyse the website's accessibility features. Tools like Lighthouse provided insights into how accessible the website is for users with disabilities and suggested improvements to enhance user experience. By leveraging AI, the project was able to achieve a higher level of efficiency, creativity, and accessibility.

Testing
The site was tested manually and using automated tests.

Manual Testing
Manual testing was performed on the site to ensure that all features worked as expected. This included testing the following:

Test	Expected Result	Actual Result
Click Home menu	success	success
Click About menu	success	success
Click Resgister	success	success
Click Login	success	success
Click Logout	success	success
Click Contact Us button	success	success
Click Upcoming Events button	success	success
Click individual event post	success	success
Click back to event list	success	success
Create, edit, delete a personal comment	success	success
Register new account	success	success
Create contact request	success	success
Access admin interface	success	success
Responsivity	success	success
Open new page from social media links	success	success
Automated Testing
Automated tests were written using the Django test framework. These tests were run using the python manage.py test command and tested the following:

The home page loads successfully.
The event detail page loads successfully.
The about page loads successfully.
The comment form submits successfully.
The contact form submits successfully.
Code Validation
The code was validated using the following tools:

HTML was validated using the W3C Markup Validation Service.
Three errors were found in the HTML validation, however, the errors were not found on inspection of the code.

CSS was validated using the W3C CSS Validation Service.
No errors were found in the CSS validation. CSS Validation

Python was validated using the CI Python Linter.
No errors were found in the Python validation indicating that the code is PEP8 compliant.

LightHouse Testing
The site was tested using Google LightHouse to check performance, accessibility, best practices, and SEO.
The results were as follows:


The low score for best practises is caused by cloudinary images not having a secure URL which can't be altered in the code but is automatically upgraded to HTTPS.

Deployment
The site was deployed to Heroku from the main branch of the repository early in the development stage for continuous deployment and checking.

The Heroku app is setup with 3 environment variables, repalcing the environment variables stored in env.py (which doesn't get pushed to github).

In order to create an Heroku app:

Click on New in the Heroku dashboard, and Create new app from the menu dropdown.

Give your new app a unique name, and choose a region, preferably one that is geographically closest to you.

Click "Create app"

In your app settings, click on "Reveal Config Vars" and add the environment variables for your app. These are:

- DATABASE_URL - your database connection string
- SECRET_Key - the secret key for your app
- CLOUDINARY_URL - the cloudinary url for your image store
The PostgreSQL database is served from ElephantSQL

Once the app setup is complete, click on the Deploy tab and:

1. Connect to the required GitHub account
2. Select the repository to deploy from
3. Click the Deploy Branch button to start the deployment.
4. Once deployment finishes the app can be launched.
The app can be accessed at the following link: Cornwall Conservation Events

Credits and Acknowledgements
The project structure and some code snippets were inspired by the "I Think Therefore I Blog" project from the LMS.
The project was developed using the Django web framework.
The project was deployed on Heroku.
Content
The content for the site was sourced from official event pages.

Media
The images used on the site were hosted on Cloudinary and sourced from official event pages.


html 
<details>
    <summary>🚀 <strong>Project Specs</strong></summary>

<!-- Content Here -->

</details>


“”

🤖 AI Tool Reflections
Throughout the development of this Django-based race platform, AI tools—primarily GitHub Copilot—were used to accelerate coding, streamline design decisions, and support testing. Here’s how they contributed across key phases:

User Story Definition & Planning: GitHub Copilot provided helpful suggestions for structuring user stories and acceptance criteria. While some outputs required refinement, it sped up the ideation process and aligned well with project goals.

Model & CRUD Development: Copilot assisted in generating Django model fields, views, and form logic. It offered boilerplate code for CRUD operations, which was manually adjusted to meet specific data constraints and user flows. Manual adjustments ensured accessibility and design consistency.

Front-End Design & Templates: AI tools helped scaffold Bootstrap components and layout structures. Copilot offered responsive design patterns and accessible markup, which were customized to match the chosen color palette and UX goals.

Testing & Debugging: Copilot supported the creation of Django test cases and helped identify edge cases. It also suggested fixes for template errors and static file issues during deployment.



![Homepage Screenshot](path/to/image.png)

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Heroku](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=white)
[![Badges by Shields.io](https://img.shields.io/badge/Badges-by%20Shields.io-brightgreen?logo=shieldsdotio)](https://shields.io/)
[![Using MermaidChart](https://img.shields.io/badge/Using-MermaidChart-00BFA5?logo=mermaid&logoColor=white)](https://www.mermaidchart.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)



https://www.mermaidchart.com/

https://ui.dev/amiresponsive


Incredible races list

Custom Model: Race
CRUD implimantation:: Users can see create their own races, update them (distance, difficalty, date, description, country and city), or delete. 
