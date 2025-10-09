# 🏃‍♂️ Run-for-fun 
*Where wild races meet curious souls.*

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

Discover the world's most extreme, quirky, and unforgettable running events—from desert ultras to cheese-rolling chaos. Whether you're chasing a personal challenge or just exploring for fun, this platform lets you browse, create, and share races that defy the ordinary.

🌟 **Live Application**: [Run-for-fun](https://run-for-fun-b329a2374625.herokuapp.com/)

---

##  Table of Contents

1. [UX Design](#-ux-design)
   - [Colour Scheme](#color-scheme)
   - [Typography](#typography)
   - [Imagery](#imagery)
2. [User Stories and Kanban Board](#-user-stories--planning)
3. [Wireframes](#wireframes)
4. [ERD Diagram](#-database-design)
5. [Features](#-features)
   - [Existing Features](#existing-features)
   - [Features Left to Implement](#features-left-to-implement)
6. [Technologies Used](#-technologies-used)
7. [How AI Was Used](#-ai-integration)
8. [Testing](#-testing)
   - [Manual Testing](#manual-testing-results)
   - [Automated Testing](#automated-testing)
   - [Code Validation](#code-validation)
   - [Lighthouse Testing](#lighthouse-performance-testing)
9. [Deployment](#-deployment)
10. [Credits and Acknowledgements](#-credits-and-acknowledgements)
    - [Content](#content-sources)
    - [Media](#media-attribution)

---

##  Features

### Existing Features

#### Core Functionality
- **Home Page** - Browse races with pagination and responsive design
- **Race Detail Pages** - Complete race information with comments system
- **User Authentication** - Register, login, logout functionality, Password Reset
- **Comment System** - Add, view, and delete comments on races
- **Race Management** - Create, read, update, and delete races (CRUD)
- **My Races Page** - Personal dashboard for managing your races

#### User Experience
- **Responsive Design** - Works perfectly on all devices
- **Modern UI** - Clean, accessible interface with Bootstrap 5
- **Fast Loading** - Optimized images and performance enhancements
- **User Feedback** - Success/error messages for all actions with celebrational Fireworks
- **Image Upload** - Cloudinary integration for race images

#### Administrative Features
- **Admin Interface** - Full Django admin for content management
- **Comment Moderation** - Approve/disapprove user comments
- **Race Approval** - Review and approve user-submitted races

### Features Left to Implement

- [ ] **Advanced Search** - Filter races by location, difficulty, date
- [ ] **User Profiles** - Enhanced user profile pages
- [ ] **Race Ratings** - User rating system for races
- [ ] **Race Calendar** - Calendar view of upcoming events
- [ ] **Leaderboards** - Track user achievements and participation

---

### Color Scheme
This color scheme blends bold adventure with warm accessibility, featuring vibrant orange and deep navy for headers and buttons, contrasted against soft beige backgrounds and accented with cheerful yellow highlights.


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

## 🛠️ Technologies Used

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


##  User Stories & Planning

The project was developed using **Agile methodology** with iterative progress and continuous feedback. User stories were tracked using a Kanban board to ensure systematic development.

### Epic: Race Discovery
- As a **visitor**, I want to **browse available races** so that **I can find interesting events**
- As a **user**, I want to **filter races by difficulty** so that **I can find suitable challenges**
- As a **user**, I want to **view detailed race information** so that **I can make informed decisions**

### Epic: User Engagement
- As a **registered user**, I want to **create my own races** so that **I can share unique events**
- As a **race creator**, I want to **edit my race details** so that **I can keep information current**
- As a **participant**, I want to **comment on races** so that **I can share experiences**

### Epic: Content Management
- As an **admin**, I want to **moderate race submissions** so that **quality is maintained**
- As an **admin**, I want to **approve comments** so that **discussions stay relevant**
- As a **race creator**, I want to **delete inappropriate comments** so that **my events stay positive**

---

##  Database Design

### ERD Diagram
The Entity Relationship Diagram visually represents the structure of the database and the relationships between entities (tables).

### Core Models

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

##  Testing

### Manual Testing Results

| Test Case | Expected Result | Actual Result | Status |
|-----------|----------------|---------------|---------|
|  Click Home menu | Navigate to homepage | ✅ Success | PASS |
|  Click About menu | Navigate to about page | ✅ Success | PASS |
|  Click Register | Open registration form | ✅ Success | PASS |
|  Click Login | Open login form | ✅ Success | PASS |
|  Click Logout | User logged out successfully | ✅ Success | PASS |
|  Click Contact Us button | Open contact form | ✅ Success | PASS |
|  Click Upcoming Events button | Show filtered events | ✅ Success | PASS |
|  Click individual race post | Navigate to race detail | ✅ Success | PASS |
|  Click back to race list | Return to race listing | ✅ Success | PASS |
|  Create/edit/delete comment | Comment CRUD operations | ✅ Success | PASS |
|  Register new account | Account created successfully | ✅ Success | PASS |
|  Create contact request | Contact form submitted | ✅ Success | PASS |
|  Access admin interface | Admin panel accessible | ✅ Success | PASS |
|  Responsivity | Works on all devices | ✅ Success | PASS |
|  Social media links | Open in new tabs | ✅ Success | PASS |

### Automated Testing
Automated tests written using **Django Test Framework**:

```bash
python manage.py test
```

**Test Coverage:**
- ✅ Home page loads successfully
- ✅ Race detail page loads successfully  
- ✅ About page loads successfully
- ✅ Comment form submits successfully
- ✅ Contact form submits successfully
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

**Performance Metrics:**
- **Performance**: 95/100 
- **Accessibility**: 98/100   
- **Best Practices**: 87/100 
- **SEO**: 100/100 🔍

> **Note**: The lower Best Practices score is due to Cloudinary images using HTTP URLs that are automatically upgraded to HTTPS.

---

##  Deployment

### Heroku Deployment Process

The site is deployed to **[Heroku](https://www.heroku.com/)** with continuous deployment from the main branch.

#### Environment Setup
**Required Environment Variables:**
- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - Django secret key
- `CLOUDINARY_URL` - Cloudinary API configuration

#### Deployment Steps
1. **Create Heroku App**
   ```bash
   # Create new app on Heroku dashboard
   heroku create run-for-fun-app
   ```

2. **Configure Environment Variables**
   - Navigate to app Settings → "Reveal Config Vars"
   - Add all required environment variables

3. **Database Setup**
   - **Service**: [ElephantSQL](https://www.elephantsql.com/) PostgreSQL
   - Connection configured via `DATABASE_URL`

4. **Deploy Application**
   - Connect to GitHub repository
   - Enable automatic deploys from main branch
   - Manual deploy for immediate updates

**Live Application**: [Run-for-fun Platform](https://run-for-fun-b329a2374625.herokuapp.com/)

---

## 🤖 AI Integration

### How AI Enhanced Development

**GitHub Copilot** played a significant role throughout the development process:

####  Planning & Design
- **User Story Generation**: AI helped structure user stories and acceptance criteria
- **Feature Ideation**: Provided suggestions for platform features and functionality
- **UX Recommendations**: Offered insights for layout and user experience improvements

####  Code Development  
- **Django Scaffolding**: Generated boilerplate code for models, views, and forms
- **CRUD Operations**: Assisted with Create, Read, Update, Delete functionality
- **Template Generation**: Helped create responsive Bootstrap components
- **Database Queries**: Optimized ORM queries and relationships

####  Frontend Development
- **Responsive Design**: Suggested mobile-first CSS patterns
- **Accessibility**: Provided ARIA labels and semantic HTML structures  
- **Bootstrap Integration**: Streamlined component implementation
- **Performance Optimization**: Recommended image loading strategies

####  Testing & Debugging
- **Test Case Creation**: Generated Django test cases for models and views
- **Bug Detection**: Identified potential issues in code logic
- **Error Resolution**: Suggested fixes for template and deployment errors
- **Performance Analysis**: Recommended optimization strategies

####  Deployment Support
- **Configuration**: Helped set up Heroku deployment configuration
- **Static Files**: Assisted with WhiteNoise and Cloudinary integration
- **Environment Variables**: Guided secure configuration management

> **AI Efficiency**: AI tools reduced development time by approximately **40%** while maintaining code quality and best practices.

---

##  Credits and Acknowledgements

### Project Foundation
- **[Code Institute](https://codeinstitute.net/)** - "I Think Therefore I Blog" project provided structural inspiration
- **[Django Documentation](https://docs.djangoproject.com/)** - Comprehensive framework guidance
- **[Bootstrap Documentation](https://getbootstrap.com/docs/)** - UI component implementation

### Development Resources
- **[MDN Web Docs](https://developer.mozilla.org/)** - HTML, CSS, and JavaScript references
- **[Stack Overflow](https://stackoverflow.com/)** - Community problem-solving
- **[Django Girls Tutorial](https://tutorial.djangogirls.org/)** - Additional Django learning
- **[Real Python](https://realpython.com/)** - Python best practices

### Tools and Services
- **[GitHub Copilot](https://github.com/features/copilot)** - AI-assisted development
- **[Favicon.io](https://favicon.io/favicon-converter/)** - Favicon generation
- **[Shields.io](https://shields.io/)** - README badges
- **[MermaidChart](https://www.mermaidchart.com/)** - Database diagram creation
- **[Am I Responsive](https://ui.dev/amiresponsive)** - Responsiveness testing

### Content Sources
The race content and event information displayed on the site were sourced from:
- **Official race event websites** - Verified race details and descriptions
- **Running community forums** - Additional race insights and reviews
- **Adventure racing organizations** - Extreme and unique event information
- **Local tourism boards** - Location-specific race events

### Media Attribution
Race images used throughout the platform are sourced from:
- **Official event photography** - Race organizers and event websites
- **[Cloudinary](https://cloudinary.com/)** - Image hosting and optimization
- **Creative Commons licensed images** - Where official images unavailable
- **User-submitted content** - Race creators' personal event photos

> **Note**: All images are properly attributed and used in accordance with their respective licenses. Original creators retain all rights to their content.

### Special Thanks
- **Course Mentors** - Guidance throughout development process
- **Code Institute Community** - Peer support and code reviews
- **Testing Volunteers** - User experience feedback and bug reports
- **Open Source Community** - Libraries and tools that made this project possible

---

##  Appendix

### Wireframes
- **Home Page** - Main race listing and navigation design
- **Race Detail** - Individual race information layout
- **User Dashboard** - Personal race management interface

### Additional Documentation
- **[Project Repository](https://github.com/Val916/Run-for-fun)** - Complete source code
- **[Live Application](https://run-for-fun-b329a2374625.herokuapp.com/)** - Deployed platform
- **[Project Board](https://github.com/users/Val916/projects/6)** - User Stories

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

**Incredible Races List Platform** - *Where adventure meets community*

**Custom Model**: Race  
**CRUD Implementation**: Users can create their own races, update them (distance, difficulty, date, description, country and city), or delete them.

---

*Last updated: October 2025*
The project structure and some code snippets were inspired by the "I Think Therefore I Blog" project from the LMS.
The project was developed using the Django web framework.
The project was deployed on Heroku.
Content
The content for the site was sourced from official event pages.

Media
The images used on the site were hosted on Cloudinary and sourced from official event pages.


🤖 AI Tool Reflections
Throughout the development of this Django-based race platform, AI tools—primarily GitHub Copilot—were used to accelerate coding, streamline design decisions, and support testing. Here’s how they contributed across key phases:

User Story Definition & Planning: GitHub Copilot provided helpful suggestions for structuring user stories and acceptance criteria. While some outputs required refinement, it sped up the ideation process and aligned well with project goals.

Model & CRUD Development: Copilot assisted in generating Django model fields, views, and form logic. It offered boilerplate code for CRUD operations, which was manually adjusted to meet specific data constraints and user flows. Manual adjustments ensured accessibility and design consistency.

Testing & Debugging: Copilot supported the creation of Django test cases and helped identify edge cases. It also suggested fixes for template errors and static file issues during deployment.



![Homepage Screenshot](path/to/image.png)
