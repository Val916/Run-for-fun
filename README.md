# Run for fun

_Where wild races meet curious souls._

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Heroku](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=white)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Badges by Shields.io](https://img.shields.io/badge/Badges-by%20Shields.io-brightgreen?logo=shieldsdotio)](https://shields.io/)
[![Using MermaidChart](https://img.shields.io/badge/Using-MermaidChart-00BFA5?logo=mermaid&logoColor=white)](https://www.mermaidchart.com/)

</div>
<div align="center">
Discover the world's most extreme, quirky, and unforgettable running events—from desert ultras to cheese-rolling chaos. Whether you're chasing a personal challenge or just exploring for fun, this platform lets you browse, create, and share races that defy the ordinary.
</div>
<br>

🌟 **Deployed Link**: [<span style="color: #FF6B35;">Run-for-fun</span>](https://run-for-fun-b329a2374625.herokuapp.com/)

---

## Table of Contents

1. [Features](#features)
   - [Existing Features](#existing-features)
   - [Features Left to Implement](#features-left-to-implement)
2. [Wireframes](#wireframes)
   - [Color Scheme](#color-scheme)
   - [Typography](#typography)
   - [Imagery](#imagery)
3. [Technologies Used](#technologies-used)
4. [User Stories & Planning](#user-stories--planning)
5. [Database Design](#database-design)
6. [Testing](#testing)
   - [Manual Testing Results](#manual-testing-results)
   - [Code Validation](#code-validation)
   - [Lighthouse Performance Testing](#lighthouse-performance-testing)
7. [Deployment](#deployment)
8. [AI Integration](#-ai-integration)
9. [Credits and Acknowledgements](#credits-and-acknowledgements)

---

## Features

### Existing Features

#### Core Functionality

- **Home Page** - Browse races with pagination and responsive design [<span style="color: #FF6B35;">Here</span>](docs/images/features/home-pagination.png)
- **Race Detail Pages** - Complete race information with comments system [<span style="color: #FF6B35;">Here</span>](docs/images/features/registration.png)
- **User Authentication** - Register, login, logout functionality, Password Reset
- **Comment System** - Add, view, and delete comments on races
- **Race Management** - Create, read, update, and delete races (CRUD)
- **My Races Page** - Personal dashboard for managing your races

#### User Experience

- **Responsive Design** - Works perfectly on all devices [<span style="color: #FF6B35;">Here</span>](docs/images/features/home-tablet.png)
- **Modern UI** - Clean, accessible interface with Bootstrap 5
- **Fast Loading** - Optimized images and performance enhancements
- **User Feedback** - Success/error messages for all actions with celebrational Fireworks
- **Image Upload** - Cloudinary integration for race images

#### Administrative Features

- **Admin Interface** - Full Django admin for content management
- **Comment Moderation** - Approve/disapprove user comments
- **Race Approval** - Review and approve user-submitted races

### Wireframes

## [<span style="color: #FF6B35;">Wireframes</span>](https://github.com/Val916/Run-for-fun/blob/main/docs/images/wireframes/wireframe!!!.png)

### Color Scheme

This color scheme blends bold adventure with warm accessibility, featuring vibrant orange and deep navy for headers and buttons, contrasted against soft beige backgrounds and accented with cheerful yellow highlights.

![<span style="color: #FF6B35;">Color Palette</span>](https://github.com/Val916/Run-for-fun/blob/main/docs/images/features/palette.png)

### Typography

The site uses **Google Fonts**:

- **[Inter](https://fonts.google.com/specimen/Inter)** - Main text font for excellent readability
- **[Lato](https://fonts.google.com/specimen/Lato)** - Heading font for modern appearance

### Imagery

- **Source**: Race images from official event pages
- **Hosting**: [Cloudinary](https://cloudinary.com/) for optimized loading
- **Optimization**: Responsive images with proper aspect ratios
- **Performance**: Lazy loading and fetchpriority for critical images

---

## Technologies Used

### Backend

- **[Python 3.12](https://www.python.org/)** - Core programming language
- **[Django 4.2](https://www.djangoproject.com/)** - Web framework
- **[PostgreSQL](https://www.postgresql.org/)** - Database system
- **[Django Allauth](https://django-allauth.readthedocs.io/)** - Authentication system

### Frontend

- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)** - Markup language
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)** - Styling
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** - Interactive functionality
- **[Bootstrap 5](https://getbootstrap.com/)** - CSS framework
- **[Font Awesome](https://fontawesome.com/)** - Icons
- **[Google Fonts](https://fonts.google.com/)** - Typography (Inter & Lato)

### Cloud Services & Deployment

- **[Heroku](https://www.heroku.com/)** - Application hosting
- **[Cloudinary](https://cloudinary.com/)** - Image hosting and optimization
- **[WhiteNoise](https://whitenoise.evans.io/)** - Static file serving

### Development Tools

- **[GitHub](https://github.com/)** - Version control
- **[GitHub Copilot](https://github.com/features/copilot)** - AI-assisted development
- **[VS Code](https://code.visualstudio.com/)** - Code editor
- **[Chrome DevTools](https://developer.chrome.com/docs/devtools/)** - Testing and debugging

## User Stories & Planning

- **[<span style="color: #FF6B35;">Project Board</span>](https://github.com/users/Val916/projects/6)**

The project was developed using Agile methodology [**(<span style="color: #FF6B35;">see Board in process</span>)**](https://github.com/Val916/Run-for-fun/blob/main/docs/images/features/project-board.png) with iterative progress and continuous feedback. User stories were tracked using a Kanban board to ensure systematic development, using categorized tasks into Must have, Should have, Could have, and Won’t have to clarify what’s essential, desirable, optional, or excluded for a project’s success.

### As a visitor, I want to browse available races so that I can find interesting events.

**Acceptance Criteria:**
The homepage displays a list of races with name, date, location, and image.
Each race links to a detail page.
The layout is responsive across devices using Bootstrap or CSS Grid/Flexbox.
Images have alt text and semantic HTML is used.

**Tasks:**

1. ✅ Create race list view and template
2. ✅ Display race name, date, location, and image
3. ✅ Link each race to its detail page
4. ✅ Use semantic HTML for structure and accessibility
5. ✅ Apply responsive layout using Bootstrap grid or Flexbox
6. ✅ Ensure images have alt text

</details>

<details>

  <summary>- As a new user, I want to register and log in so I can access personalized features and manage races.</summary>

**Acceptance Criteria:**

- A registration form is available and functional.
- A login form allows existing users to authenticate.
- After login, the user is redirected to the homepage with a personalized greeting.
- Navigation updates to show “Logout” and “Create Race” links.
- Only authenticated users can access race creation/editing views.
- Invalid login attempts show error messages.

**Tasks:**

1. ✅ Enable Django’s built-in authentication system
2. ✅ Create registration and login templates with Bootstrap styling
3. ✅ Add login/logout links to base navigation
4. ✅ Redirect users after login with personalized greeting
5. ✅ Protect race creation/editing views with @login_required
6. ✅ Handle invalid login attempts with error messages
7. ✅ Commit changes with descriptive messages

</details>

<details>

  <summary>- As a logged-in user, I want the UI to reflect my login state so I know what actions I can take.</summary>

**Acceptance Criteria:**

- Navigation bar updates dynamically based on authentication status.
- Logged-in users see “Create Race” and “Logout” links.
- Logged-out users see “Login” and “Register” links.
- A welcome message appears for authenticated users.

Tasks:

1. ✅ Update navigation bar to show/hide links based on login status
2. ✅ Display “Create Race” and “Logout” for logged-in users
3. ✅ Show “Login” and “Register” for anonymous users
4. ✅ Add welcome message for authenticated users

</details>

<details>

  <summary>- As a race organizer, I want to create and edit race pages with images, maps, and descriptions so I can promote my event effectively.</summary>

**Acceptance Criteria:**

- A logged-in user can access a “Create Race” form via the navigation bar.
- The form includes fields for name, date, location, description, image upload, and coordinates.
- Upon submission, the race is saved to the database and visible on the race list page.
- The user can edit or delete their own races via dedicated buttons.
- Image uploads are resized (via Pillow or Cloudinary) and displayed correctly.
- A map is rendered on the race detail page using Leaflet or Google Maps.
- Success messages are shown after creation or editing.

Tasks:

1. ✅ Define Race model with fields: name, date, location, description, image, latitude, longitude
2. ✅ Create race creation form using Django ModelForm
3. ✅ Build race creation and editing views (CreateView, UpdateView)
4. ✅ Add image upload handling (Pillow or Cloudinary)
5. ✅ Resize or optimize images on upload
6. ✅ Render race detail page with map (Leaflet or Google Maps)
7. ✅ Restrict race creation/editing to authenticated users
8. ✅ Add success messages after create/edit/delete
9. ✅ Test model behavior and form validation

</details>

<details>

  <summary>- As a user, I want to receive feedback when I create or edit a race, so I know my action was successful.</summary>

**Acceptance Criteria:**

- Django messages appear after race creation, editing, or deletion.
- Messages are styled using Bootstrap alerts.
- Errors (e.g., missing fields) are clearly displayed on the form.

Tasks:

1. ✅ Enable Django messaging framework
2. ✅ Add success messages for race creation/editing/deletion
3. ✅ Style messages using Bootstrap alerts
4. ✅ Display form errors clearly on submission

</details>

<details>

  <summary>- As a visitor, I want the site to feel visually consistent and adventurous so I enjoy exploring it.</summary>
  
  **Acceptance Criteria:**

- A consistent color palette and font style are applied across all pages.
- Buttons, cards, and headings follow a unified design system.
- Accessibility checks confirm sufficient contrast and readable font sizes.
- The layout adapts to mobile, tablet, and desktop views.

Tasks:

1. ✅ Apply consistent color palette across templates
2. ✅ Use unified font styles and spacing
3. ✅ Style buttons, cards, and headings with Bootstrap/custom CSS
4. ✅ Check accessibility contrast and font sizes
5. ✅ Test layout on mobile, tablet, and desktop

</details>

<details>

  <summary>- As a joyful user I would like to celebrate any action on the website I made.</summary>
  Task:

✅ Find a library and make a css styling for a Firework, that will be popping out after every successful message about creating a new race or creating or deleting a comment the existing race.

![<span style="color: #FF6B35;">Fireworks</span>](https://github.com/Val916/Run-for-fun/blob/main/docs/images/features/fireworks.png)

</details>

<details>

  <summary>- As a user I want to comment the races, edit and delete my comments, if I need to.</summary>
  
  **Acceptance Criteria:**
- Users must be authenticated to post, edit, or delete comments.
- Comments are linked to specific race entries and user accounts.
- Only the comment author can edit or delete their own comments.
- Unapproved comments are hidden from other users but visible to the author.
- A confirmation message appears after each action (create, edit, delete).
- Comments are displayed in reverse chronological order.

Tasks:

1. ✅ Create Comment model with fields: body, author, race, created_on, approved
2. ✅ Build CommentForm using Django’s ModelForm
3. ✅ Display approved comments on race detail page with count
4. ✅ Add comment form for logged-in users using crispy forms
5. ✅ Handle POST request to save new comments
6. ✅ Create views for editing and deleting comments (restricted to author)
7. ✅ Add success messages for create/edit/delete actions
8. ✅ Style comments and form using Bootstrap
9. ✅ Write basic tests for comment functionality and access control

## </details>

## Database Design

### ERD Diagram

The Entity Relationship Diagram visually represents the structure of the database and the relationships between entities (tables).

<details>

<summary><b><span style="color: #FF6B35;">Tables</span></b> </summary>

![Tables](https://github.com/Val916/Run-for-fun/blob/main/docs/images/wireframes/2_diagram_tables.png)

</details>

<details>

  <summary><b><span style="color: #FF6B35;">Click to view relationships between entities diagram</b> </span> </summary>
  <img src="https://github.com/Val916/Run-for-fun/blob/main/docs/images/wireframes/main_diagram.png" alt="Entities">

</details>

### Core Models

**CRUD Implementation**: Users can create their own races, update them (distance, difficulty, date, description, country and city), or delete them.

#### Race Model

```python
class Race(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    distance = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    race_date = models.DateTimeField()
    location_country = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
```

#### Comment Model

```python
class Comment(models.Model):
    race = models.ForeignKey(Race, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
```

---

## Testing

### Manual Testing Results

| Test Case                  | Expected Result              | Actual Result | Status |
| -------------------------- | ---------------------------- | ------------- | ------ |
| Click Home menu            | Navigate to homepage         | ✅ Success    | PASS   |
| Click Register             | Open registration form       | ✅ Success    | PASS   |
| Click Login                | Open login form              | ✅ Success    | PASS   |
| Click Logout               | User logged out successfully | ✅ Success    | PASS   |
| Click individual race post | Navigate to race detail      | ✅ Success    | PASS   |
| Click back to race list    | Return to race listing       | ✅ Success    | PASS   |
| Create/edit/delete comment | Comment CRUD operations      | ✅ Success    | PASS   |
| Register new account       | Account created successfully | ✅ Success    | PASS   |
| Access admin interface     | Admin panel accessible       | ✅ Success    | PASS   |
| Responsivity               | Works on all devices         | ✅ Success    | PASS   |

**Test Coverage:**

- ✅ Home page loads successfully
- ✅ Race detail page loads successfully
- ✅ Comment form submits successfully
- ✅ User authentication flows
- ✅ CRUD operations for races

### Code Validation

#### HTML Validation

- **Tool**: [W3C Markup Validation Service](https://validator.w3.org/)
- **Result**: Minor template-related warnings (Django syntax)

#### CSS Validation

- **Tool**: [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- **Result**: ✅ No errors found - [CSS Validation](https://jigsaw.w3.org/css-validator/)

#### Python Validation

- **Tool**: [CI Python Linter](https://pep8ci.herokuapp.com/)
- **Result**: ✅ PEP8 compliant, no errors found

### Lighthouse Performance Testing

[<span style="color: #FF6B35;">Mobile View Link</span>](docs/images/testing/mobile-lighthouse.png)

**Performance Metrics:**

- **Performance**: 80/100
- **Accessibility**: 93/100
- **Best Practices**: 93/100
- **SEO**: 91/100

[<span style="color: #FF6B35;">Desktop View Link</span>](docs/images/testing/screen-lighthouse.png)

**Performance Metrics:**

- **Performance**: 99/100
- **Accessibility**: 93/100
- **Best Practices**: 93/100
- **SEO**: 91/100

---

## Deployment

### Heroku Deployment Process

The site is deployed to **[Heroku](https://www.heroku.com/)** with continuous deployment from the main branch.

#### Deployment Steps

1. **Create Heroku App**
   - Create new "run-for-fun" app on Heroku dashboard
   - Note the app name for later configuration

2. **Configure Environment Variables**
   - Navigate to app Settings → "Reveal Config Vars"
   - Add all required environment variables:
     - `DATABASE_URL` - PostgreSQL connection string
     - `SECRET_KEY` - Django secret key
     - `CLOUDINARY_URL` - Cloudinary API configuration

3. **Prepare Project Files**
   - Create a `Procfile` with: `web: gunicorn project_name.wsgi`
   - Ensure `Debug = False` in `settings.py`
   - Add `'localhost'` and `'project_name.herokuapp.com'` to `ALLOWED_HOSTS`
   - Update `requirements.txt` with all dependencies

4. **Database Setup**
   - **Service**: PostgreSQL from Code Institute
   - Copy DATABASE_URL from dashboard
   - Add DATABASE_URL to both Heroku Config Vars and local `env.py`
   - Run migrations:
     ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     ```

5. **Deploy Application**
   - Connect GitHub repository to Heroku
   - Enable automatic deploys from main branch
   - Perform initial manual deploy
   - Verify deployment success

**Live Application**: [<span style="color: #FF6B35;">Run-for-fun</span>](https://run-for-fun-b329a2374625.herokuapp.com/)

---

## 🤖 AI Integration

**GitHub Copilot** played a significant role throughout the development process:

### Planning & Design

Structured user stories, suggested features, and improved UX layout.

### Code Development

Generated Django scaffolding, CRUD logic, templates, and optimized ORM queries.

### Frontend Development

Recommended responsive design, semantic HTML, and streamlined Bootstrap use.

- **Error Resolution**: Suggested fixes for template and deployment errors
- **Performance Analysis**: Recommended optimization strategies

### Deployment Support

Assisted with WhiteNoise and Cloudinary integration

---

## Credits and Acknowledgements

### Project Foundation

- **[Code Institute](https://codeinstitute.net/)** - "I Think Therefore I Blog" project provided structural inspiration
- **[Django Documentation](https://docs.djangoproject.com/)** - Comprehensive framework guidance
- **[Bootstrap Documentation](https://getbootstrap.com/docs/)** - UI component implementation

### Development Resources and Tools

- **[Django Girls Tutorial](https://tutorial.djangogirls.org/)** - Additional Django learning
- **[Real Python](https://realpython.com/)** - Python best practices
- **[GitHub Copilot](https://github.com/features/copilot)** - AI-assisted development
- **[Favicon.io](https://favicon.io/favicon-converter/)** - Favicon generation
- **[Shields.io](https://shields.io/)** - README badges
- **[MermaidChart](https://www.mermaidchart.com/)** - Database diagram creation

### Content Sources and Media Attribution

The race content and event information displayed on the site were sourced from:

- **Official race event websites** - Verified race details and descriptions

Race images used throughout the platform are sourced from:

- **Official event photography** - Race organizers and event websites (all the links for oficial websites could be found on the Race Details pages)
- **[Cloudinary](https://cloudinary.com/)** - Image hosting and optimization
- **User-submitted content** - Race creators' personal event photos

> **Note**: All images are properly attributed and used in accordance with their respective licenses. Original creators retain all rights to their content.

---

### Features Left to Implement

- [ ] **Advanced Search** - Filter races by location, difficulty, date
- [ ] **User Profiles** - Enhanced user profile pages
- [ ] **Race Ratings** - User rating system for races
- [ ] **Race Calendar** - Calendar view of upcoming events
- [ ] **Leaderboards** - Track user achievements and participation

---

### Known nugs, to be fixed

[<span style="color: #FF6B35;">The image on "My Races" page is not responsive</span>](https://github.com/Val916/Run-for-fun/blob/main/docs/images/testing/bug-detected.png)

---

<details>
<summary> <strong>Project Specifications</strong></summary>

### Custom Model Implementation

- **Race Model**: Complete CRUD functionality for race management
- **Comment System**: User engagement with approval workflow
- **User Authentication**: Django Allauth integration
- **Image Handling**: Cloudinary for optimized media storage

### Technical Achievements

- **Performance Optimization**: LCP improvements with fetchpriority
- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Accessibility**: WCAG compliant with semantic HTML
- **Security**: CSRF protection and secure authentication

### Deployment Features

- **Continuous Deployment**: Heroku integration with GitHub
- **Environment Management**: Secure configuration variables
- **Static File Handling**: WhiteNoise for production efficiency
- **Database**: PostgreSQL with ElephantSQL hosting

</details>

---

### Special Thanks

- **Course Mentors** - Guidance throughout development process (Mark, Alex 💛)
- **Code Institute Community** - Peer support and code reviews
- **Testing Volunteers** - User experience feedback and bug reports (thank you, 🎆 guys!)
- **Open Source Community** - Libraries and tools that made this project possible
