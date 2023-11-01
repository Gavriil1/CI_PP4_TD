# ABCDE Todo List

![Am I Responsive](docs/amiresponsive/am_i_responsive.png)

**Developer: Arron Beale**

💻 [Visit live website](https://ci-pp4-td-014f88cd1918.herokuapp.com/)  
(Ctrl + click to open in new tab)












## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)




### About
"ABCDE Todo List" is an application that helps a user organize their time according to Brian Tracy's method, as described in his book "Eat That Frog." Additionally, the website has additional features: 
- Feedback form 
- Admin favorite books.

<hr>

### User Goals
- Create/Update/Delete tasks.
- Be able to see all tasks in one place.
- Have access to the manual of the application.
- Read the list of self-development books.

### Site Owner Goals

- To provide a solution to allow users to organize to-do tasks.
- Create an intuitive and easy-to-use application to attract more customers.
- Develop a fully responsive and accessible website.

<hr>


## User Experience

### Target Audience
- Students: managing assignments, study schedules.
- People with Busy Lifestyles: Manage multiple responsibilities.
- Project Managers:  To coordinate and track tasks.
- Individuals Seeking Personal Productivity: To increase personal productivity.
- Freelancers and Gig Workers: To manage their various freelance projects and deadlines.


### User Requirements and Expectations

- Fully responsive website on all devices.
- Ability to use the app on all types of devices.
- Calm and relaxing GUI interface.
- Contact Form to engage with support or leave feedback.
- Easy and intuitive application.
- List of books for self-development.

##### Back to [top](#table-of-contents)<hr>


## User Stories




### Admin / Authorised User

16. In my role as an Admin or Authorized User, I have the capability to log in to the admin console for backend access.
17. As an Admin or Authorized User, I am able to manually include, remove, or update books in the list of favorite books.
18. As an Admin or Authorized User, I can view messages that have been sent by users through the contact form.
19. As an Admin, I have the ability to view, update, or delete user tasks from the backend.
20. As an Admin, I can create user, delete user , block and unblock useer.

### Site Owner  
23. As a Site Owner I want site to be responsive (Must have)
24. As a Site Owner  I want to add validation to the contact form, to make sure that all required fields are completed.

### Kanban, Epics & User Stories
- GitHub Kanban was used to track all open user stories
- Epics were created using the milestones feature
- Backlog, In Progress, Done headings were used in the kanban

<details><summary>Epics</summary>

![Epics](https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/features/kanban-epics.PNG)
![Epic 1](https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/features/kanban-epic-1.PNG)
![Epic 2](https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/features/kanban-epic-2.PNG)
![Epic 3](https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/features/kanban-epic-3.PNG)
![Epic 4](https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/features/kanban-epic-4.PNG)
</details>

<details><summary>User Stories</summary>

![User stories](https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/features/user-stories.PNG)

</details>

<details><summary>Kanban</summary>

![Kanban mid](https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/features/kanban-mid.PNG)
![Kanban finish](https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/features/kanban-finish.PNG)

</details>


##### Back to [top](#table-of-contents)<hr>


## Design

### Colours

I chose bright colours for footer and navbar to make application more positive.
I added a pcture with star sky to make application relaxing.

### Structure

#### Website pages

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

The footer contains all relevant social media links that the business has so the user can visit any social media site and follow the business there to expand the businesses followers, likes and shares.

- The site consists of the following pages:
  - Homepage with cards for the user to choose to book a table, view the food or drinks menu.
  - Food menu has the current list of all available foods from the database sorted by starters, mains and desserts
  - Drinks menu has the current list of all available drinks from the databse sorted by type
  - Blog page has a paginated list of blogs posted by an admin or authorised user, 4 per page
  - Blog expanded displays a blog the user has selected so they can read the blog, if they are logged in they can also leave a comment which will then need to be approved before it is displayed
  - Book page allows registered users to book a table , guest count, date requested, time requested and table location
  - My bookings displays all bookings for the user that they have made, bookings in the past are automatically expired
  - Edit booking allows the user to change their date, time, table and guest count
  - Cancel booking allows the user to cancel the booking which will then delete it from the database
  - Contact us allows the user to send us a DM if the are registered, or they can contact us from the displayed email and phone number or visit the address listed.
  - Login / Logout allows users to login to make bookings, view, edit, and delete bookings
  - Register allows the user to regiser so they can use the booking system
  - 404 error page to display if a 404 error is raised

#### Database

- Built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)
- Two database model shows all the fields stored in the database

<details><summary>Show diagram</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/database-schema.PNG">
</details>


##### User Model
The User Model contains the following:
- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

##### FoodItem Model
The FoodItem Model contains the following:
- food_id
- food_name
- description
- price
- available

##### DrinkItem Model
The DrinkItem Model contains the following:
- drink_id
- drink_name
- description
- price
- available

##### Table Model
The Table Model contains the following:
- table_id (PrimaryKey)
- table_name
- max_seats
- available


##### Booking Model
The Booking Model contains the following:
- booking_id (PrimaryKey)
- created_date
- requested_date
- requested_time
- table (ForeignKey)
- guest (ForeignKey)
- seats
- guest_count

##### Post Model
The Post Model contains the following:
- title
- post_id (PrimaryKey)
- author (ForeignKey)
- created_date
- updated_date
- content
- featured_image
- excerpt
- slug
- status

##### Comment Model
The Comment Model contains the following:
- post (ForeignKey)
- name
- email
- body
- created_date
- approved
- Meta: created_on

##### ContactUs Model
The ContactUs Model contains the following:
- contact_id (PrimaryKey)
- name (ForeignKey)
- email (ForeignKey)
- phone (ForeignKey)
- body


### Wireframes
The wireframes were created using Balsamiq
###  Wireframes

<details><summary>Login</summary>

<img src="docs/wireframes/login.png">

</details>

<details><summary>Register</summary>

<img src="docs/wireframes/register.png">

</details>

<details><summary>Home</summary>

<img src="docs/wireframes/homepage.png">

</details>

<details><summary>Manual</summary>

<img src="docs/wireframes/manual.png">

</details>

<details><summary>Books</summary>

<img src="docs/wireframes/bookshop.png">

</details>

<details><summary>ContactForm</summary>

<img src="docs/wireframes/contactform.png">

</details>

<details><summary>DeleteTask</summary>

<img src="docs/wireframes/delete.png">

</details>

<details><summary>CreateUpdateTask</summary>

<img src="docs/wireframes/createupdate.png">

</details>

<details><summary>404 Page</summary>

<img src="docs/wireframes/404.png">
</details>


## Features

### Home page
- Home page includes nav bar, main body and a footer


<details><summary>See feature images</summary>

![Home page](docs/features/feature-homepage.png)
</details>


### Logo & Navigation
- Shows logo designed for a to-do list
- Responsive across various screen sizes
- Transforms into hamburger menu on smaller screens
- Shows active user
- Provides access to all available pages directly from the current page

<details><summary>See feature images</summary>

![Footer](docs/features/feature-homepage.png)
![Footer](docs/features/navbar-overview-logout.png)
![Footer](docs/features/navbar-overview-hamburger.png)
</details>


### Footer
- Contains social media links and copyright
- displayed across all pages

<details><summary>See feature images</summary>

![Footer](docs/features/footer.png)
</details>

### Sign up / Register
- Allow users to register an acoount
- Username and password is required.

<details><summary>See feature images</summary>

![Register](docs/features/register.png)
</details>


### Login
-  User can login to create/update/delete a task, view list of tasks, send feedback message, see list of favourite books.

<details><summary>See feature images</summary>

![Login](docs/features/login.png)
</details>


### Logout
- Allows the user to securely log out

<details><summary>See feature images</summary>

![Logout](docs/features/navbar-overview-logout.png)
</details>


### Contact Form
- Allows the user to contact admin/site owner to share feedback

<details><summary>See feature images</summary>

![ContactForm](docs/features/contact-form.png)
</details>


### Books
- Allows the user to see the list of favorite books.
- User may see the book title, book cover, book description, book's star rating, number of reviews.
- User may click on "Buy on Amazon" to purchase the book from Amazon.
- User may utilize pagination to view the complete list of books.

<details><summary>See feature images</summary>

![Book](docs/features/books.png)
</details>


### Task List 
- Allows the user to see all their their tasks for Dayly, Weekly, Montlhy, Yearly goals
- User can see, Severity of the task, deadline of the task, complete status
- Allows a user an option to create a task, update/view the task, delete the task

<details><summary>See feature images</summary>

![Task List](docs/features/task-list.png)
</details>


### View/Edit Task page
- Allows the user to edit/view task. 
<details><summary>See feature images</summary>

![Edit/View Task](docs/features/update-view.png)
</details>

### Delete Task page
- Allows user to delete task. 
<details><summary>See feature images</summary>

![Delete Task](docs/features/delete-task.png)
</details>

### 404  page
- Page is displayed when user enters incorrect URL. 
<details><summary>See feature images</summary>

![Delete Task](docs/features/404.png)
</details>


## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

- [Am I Responsive](https://ui.dev/amiresponsive)
- [Cloudinary](https://cloudinary.com/)
- [Balsamiq](https://balsamiq.com/)
- [Favicon.io](https://favicon.io)
- [Google Fonts](https://fonts.google.com/)
- [jQuery](https://jquery.com)
- [ElePhantSQL](https://www.elephantsql.com/)
- [Chrome dev tools](https://developer.chrome.com/docs/devtools/)
- [Font Awesome](https://fontawesome.com/)
- [GitHub](https://github.com/)
- [gitpod](https://www.gitpod.io/)
- [Bootstrap v.4.6.2](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Heroku](https://dashboard.heroku.com/apps)


- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents)







### Food Menu
- The food menu displays all available foods on the menu
- Menu is seperated by starters, mains and desserts
- Items can be added via the admin panel in the backend by staff
- Staff can create, update and delete foods via the admin panel
  
<details><summary>See feature images</summary>

![Food Menu](docs/features/feature-food-menu.PNG)
</details>


### Drinks Menu
- The drinks menu displays all available foods on the menu
- Menu is seperated by wines, beers and cocktails
- Items can be added via the admin panel in the backend by staff
- Staff can create, update and delete foods via the admin panel 
  
<details><summary>See feature images</summary>

![Drinks Menu](docs/features/feature-drinks-menu.PNG)
</details>


### Blog
- The blog displays each post made by a staff member
- Paginations is used to display 4 posts per page
  
<details><summary>See feature images</summary>

![Blog](docs/features/feature-blog.PNG)
</details>


### Blog Expanded
- Expands into the selected blog the user wishes to read
- Displays a featured image uploaded by the poster
- If no image is uploaded a default image is then used
- Registerd user can comment on the blog
  
<details><summary>See feature images</summary>

![Blog Expanded](docs/features/feature-blog2.PNG)
</details>


### Comments
- Comments made are set to pending approval status to ensure nothing bad is displayed
- Only registered users can comment on a blog post
- Staff can approve comments via the admin panel on the backend
  
<details><summary>See feature images</summary>

![Comments](docs/features/feature-comments.PNG)
</details>


### Contact Us
- Registered users can DM staff via the message box
- Contact info such as, phone, email, and address is displayed
- A Google Map is embedded with the address for users to use
  
<details><summary>See feature images</summary>

![Contact Us](docs/features/feature-contact-us.PNG)
![Contact Us](docs/features/feature-contact-us2.PNG)
</details>


### Social Media Links
- A logo and link is used for each social media displayed
- All links open in a new tab to ensure user is not directed away from the business
- Displayed on all pages
  
<details><summary>See feature images</summary>

![Social Media Links](docs/features/feature-social-links.PNG)
</details>


### Pagination
- Pagination is used on the bookings list and the blog page
- Ensures the page is kept tidy as only 4 items are displayed per page
  
<details><summary>See feature images</summary>

![Pagination](docs/features/feature-pagination.PNG)
</details>


##### Back to [top](#table-of-contents)<hr>


## Validation

The W3C Markup Validation Service

<details><summary>Login</summary>
<img src="docs/validation/html-validation/login-html-validation.png">
</details>

<details><summary>Register</summary>
<img src="docs/validation/html-validation/register-html-validation.png">
</details>


<details><summary>Home</summary>
<img src="docs/validation/html-validation/homepage-html-validation.png">
</details>

<details><summary>Task Create Update</summary>
<img src="docs/validation/html-validation/create-update-html-validation.png">
</details>

<details><summary>Task Delete</summary>
<img src="docs/validation/html-validation/taskdelete-html-validation.png">
</details>

<details><summary>Manual</summary>
<img src="docs/validation/html-validation/manual-html-validation.png">
</details>

<details><summary>Contact Form</summary>
<img src="docs/validation/html-validation/contactform-html-validation.png">
</details>

<details><summary>Books</summary>
<img src="docs/validation/html-validation/books-html-validation.png">
</details>

<details><summary>404</summary>
<img src="docs/validation/html-validation/404-html-validation.png">
</details><hr>


### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>Style.css</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/validation-css.PNG">
</details><hr>


### PEP8 Validation
[PEP8 Validation Service](https://pep8ci.herokuapp.com/) The code underwent verification for PEP8 compliance and successfully passed without any errors or warnings.


<hr><summary>TODO(base) Aplication. </summary><hr>


<details><summary>base/admin.py</summary>
<img src="docs/validation/python/base/base.admin.png">
</details>

<details><summary>base/apps.py</summary>
<img src="docs/validation/python/base/base.apps.png">
</details>

<details><summary>base/forms.py</summary>
<img src="docs/validation/python/base/base.forms.png">
</details>

<details><summary>base/models.py</summary>
<img src="docs/validation/python/base/base.models.png">
</details>

<details><summary>base/url.py</summary>
<img src="docs/validation/python/base/base.urls.png">
</details>

<details><summary>base/views.py</summary>
<img src="docs/validation/python/base/base.views.png">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-test-models.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-test-views.PNG">
</details>

<details><summary>test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-test-urls.PNG">
</details>



<hr><summary>Books</summary><hr>

<details><summary>books/admin.py</summary>
<img src="docs/validation/python/books/books.admin.png">
</details>

<details><summary>books/apps.py</summary>
<img src="docs/validation/python/books/books.apps.png">
</details>

<details><summary>books/models.py</summary>
<img src="docs/validation/python/books/books.models.png">
</details>

<details><summary>books/urls.py</summary>
<img src="docs/validation/python/books/books.urls.png">
</details>

<details><summary>books/views.py</summary>
<img src="docs/validation/python/books/books.views.png">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-test-models.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-test-views.PNG">
</details>

<details><summary>test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-test-urls.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-forms.PNG">
</details>


<hr><summary>Contact Form</summary><hr>

<details><summary>contactform/admin.py</summary>
<img src="docs/validation/python/contactform/contactform.admin.png">
</details>

<details><summary>contactform/apps.py</summary>
<img src="docs/validation/python/contactform/contactform.apps.png">
</details>

<details><summary>contactform/models.py</summary>
<img src="docs/validation/python/contactform/contactform.models.png">
</details>

<details><summary>contactform/urls.py</summary>
<img src="docs/validation/python/contactform/contactforms.urls.png">
</details>

<details><summary>contactform/views.py</summary>
<img src="docs/validation/python/contactform/contactform.views.png">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-test-models.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-test-views.PNG">
</details>

<details><summary>test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-test-urls.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-forms.PNG">
</details>





### Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

#### Desktop
<details><summary>Login</summary>
<img src="docs/lighthouse/desktop/login-desktop.png">
</details>

<details><summary>Register</summary>
<img src="docs/lighthouse/desktop/register-desktop.png">
</details>

<details><summary>Homepage</summary>
<img src="docs/lighthouse/desktop/homepage-desktop.png">
</details>

<details><summary>Create/Update Task</summary>
<img src="docs/lighthouse/desktop/create-update-task-desktop.png">
</details>

<details><summary>Delete Task</summary>
<img src="docs/lighthouse/desktop/delete-task-desktop.png">
</details>

<details><summary>Manual</summary>
<img src="docs/lighthouse/desktop/manual-desktop.png">
</details>

<details><summary>Feedback</summary>
<img src="docs/lighthouse/desktop/feedback-desktop.png">
</details>

<details><summary>Books</summary>
<img src="docs/lighthouse/desktop/books-desktop.png">
</details>



#### Mobile
<details><summary>Login</summary>
<img src="docs/lighthouse/mobile/login-mobile.png">
</details>

<details><summary>Register</summary>
<img src="docs/lighthouse/mobile/register-mobile.png">
</details>

<details><summary>Homepage</summary>
<img src="docs/lighthouse/mobile/homepage-mobile.png">
</details>

<details><summary>Create Update Task</summary>
<img src="docs/lighthouse/mobile/create-update-task-mobile.png">
</details>

<details><summary>Delete Task</summary>
<img src="docs/lighthouse/mobile/delte-task-mobile.png">
</details>

<details><summary>Manual</summary>
<img src="docs/lighthouse/mobile/manual-mobile.png">
</details>

<details><summary>Feedback</summary>
<img src="docs/lighthouse/mobile/feedback-mobile.png">
</details>

<details><summary>Books</summary>
<img src="docs/lighthouse/mobile/books-desktop.png">
</details>



### Wave
WAVE was used to test the websites accessibility.

<details><summary>Login</summary>
We have two false positive errors.
Waive check says that labels are empty, but in reality the 
the labels have icons instead of text.
<img src="docs/validation/accessibility/login-waive-1.png">
<img src="docs/validation/accessibility/login-waive-2.png">
</details>

<details><summary>Register</summary>
We have 3 false positive errors, like before.
Waive check says that labels are empty, but in reality the 
the labels have icons instead of text.

<img src="docs/validation/accessibility/register-waive-1.png">
<img src="docs/validation/accessibility/register-waive-2.png">
</details>


<details><summary>HomePage</summary>
We see 2-8 false positive errors: "A link contains no text."
This happens because I used icons instead of text to create links 
<img src="docs/validation/accessibility/homepage-waive-1.png">
<img src="docs/validation/accessibility/homepage-waive-2.png">
</details>

<details><summary>Create/Update Task</summary>
<img src="docs/validation/accessibility/create-update-task-1.png">
<img src="docs/validation/accessibility/create-update-task-2.png">
</details>

<details><summary>Delete Tasks</summary>
<img src="docs/validation/accessibility/delete-waive-1.png">
<img src="docs/validation/accessibility/delete-waive-2.png">
</details>

<details><summary>Manual</summary>
<img src="docs/validation/accessibility/manual-waive-1.png">
<img src="docs/validation/accessibility/manual-waive-2.png">
</details>

<details><summary>Feedback</summary>
<img src="docs/validation/accessibility/feedback-waive-1.png">
<img src="docs/validation/accessibility/feedback-waive-2.png">
</details>

<details><summary>Books</summary>
We have false positive contrast error. Pagination background and page number
have very good contrast
<img src="docs/validation/accessibility/books-waive-1.png">
<img src="docs/validation/accessibility/books-waive-2.png">
</details>

<details><summary>404</summary>
We have one alert "Suspicious link text" which means that purpose  of the 
link is not described well, but the link is part of sentence "Otherwise, Click here to redirect to homepage.  Sentence expains the purpose of the link.
For this reason the alert is false positive.
<img src="docs/validation/accessibility/404-waive-1.png">
<img src="docs/validation/accessibility/404-waive-2.png">
</details>


##### Back to [top](#table-of-contents)<hr>


## Testing

1. Manual testing
2. Automated testing
### Users

0.  As a User I would like to login to my account.
00.  As a User I would like to create a new account.
000. As a User I would like to be able to move from Register page to Log In Page.
1. As a user, I would like to create a new task. While creating the task, I may modify the following fieldsL 'title', 'description',  'importance','frequency', 'deadline'.
2. As a user, I would like to update a new task. While updating the task, I may modify the following fields: 'title', 'description',  'importance','frequency', 'deadline'.
3. As a user, while I am on "Create/Update Task" I need to go back, without modifying or creating task.
4. As a user I would like to delete the task.
5. As a user, while on "Delete" page I would like to return to homepage without deleting the task.
6. As

### Manual testing



0.  As a User I would like to login to my account.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 | Open application URL. See login page. User credentials to log in | User logs in | Works as expected |


<details><summary></summary>
<img src="docs/userstories/log-in-to-user-account.png">


</details>

00 As a User I would like to create a new account.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| On login page click "Sign Up". On register page register your username and password | New account is created and user logged in | Works as expected |

<details><summary></summary>
<img src="docs/userstories/register-an-account-user-account.png">

</details>

000.  As a User I would like to be able to move from Register page to Log In Page.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| On Register page, click on  link "Login". | User is redirected to Log In Page | Works as expected |

<details><summary></summary>
<img src="docs/userstories/redirect-register-login.png">

</details>

1. As a user, I would like to create a new task. While creating the task, I may modify the following fields: 'title', 'description',  'importance','frequency', 'deadline'.

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| On homepage, click "Add New". On Create/Update page. Complete fields: 'title,' 'task description,' select the 'deadline,' 'severity,' 'importance,' 'frequency' and click Submit| New Task is created with required fields. | Works as expected |

<details><summary></summary>
<img src="docs/userstories/create-new-task.png">

</details>

2. As a user, I would like to update a new task. While updating the task, I may modify the following fields: 'title', 'description',  'importance','frequency', 'deadline'.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on a penscil in edit colon. On "Create/Update Task" you may6 modify one of the following fields: 'title', 'description',  'importance','frequency', 'deadline' | Task Modified | Works as expected |

<details><summary></summary>
<img src="docs/userstories/update-a-task.png">

</details>

3. As a user, while I am on "Create/Update Task" I need to go back, without modifying or creating task.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| While on "Create/Update" page click on an arrow on left top corner.| User is redirected to Homepage  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/create-update-homepage.png">

</details>

4. As a user I would like to delete the task.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on x in Edit colon. On Delete page click "Delete" | The task is deleted  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/delete-task.png">
</details>

5. As a user, while on "Delete" page I would like to return to homepage without deleting the task.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| While on a "Delete" page, click on the arrow on the top left corner| The user redirected back to homepage, task is not deleted  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/delete-homepage.png">

</details>




### Automated testing

- Testing was done using the built in Django module, unittest.
- Coverage was also usesd to generate a report


<details><summary>Bar & Grill App, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bar-and-grill-test-models.PNG">
</details>

<details><summary>Bar & Grill App, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bar-and-grill-test-views.PNG">
</details>

<details><summary>Bar & Grill App, test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bar-and-grill-test-urls.PNG">
</details>

<details><summary>Bar & Grill App, Coverage</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/coverage-bar-and-grill.PNG">
</details>

<details><summary>Bookings App, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bookings-test-models.PNG">
</details>

<details><summary>Bookings App, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bookings-test-views.PNG">
</details>

<details><summary>Bookings App, test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bookings-test-urls.PNG">
</details>

<details><summary>Bookings App, Coverage</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/coverage-bookings.PNG">
</details>


### Device Testing & Browser compatibility

The site uses to test on various real world devices was [BrowserStack](https://ci-pp4-the-diplomat.herokuapp.com/)  

This allowed me to test on real devices and not just device emulators.

The following devices were used to test my site:

<details><summary>Samsung Galaxy S22 Ultra</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-samsung-s22-ultra.PNG">
</details>

<details><summary>Apple iPhone 13</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-iphone-13.PNG">
</details>

<details><summary>Google Pixel 5</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-google-pixel-5.PNG">
</details>

<details><summary>Mozilla Firefox (v105 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-firefox.PNG">
</details>

<details><summary>Google Chrome (v106 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-chrome.PNG">
</details>

<details><summary>Safari (Monteray v15.3 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-safari-monteray-15.3.PNG">
</details>


##### Back to [top](#table-of-contents)<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| css not loading| the css folder was created in uppercase as CSS, renamed and fixed |
| While logged in as a user, on edit bookings page, if you changed the url booking number and if the number was a valid booking for another user it would access the booking | Defensive programming to make sure that only bookings made by the user would be visible |
| Double bookings | Adjusted code to check that the date, time and table were unique together and to give an error to indicate to the user that the booking was unavailable for that date, time and table combination |
| Food item description not showing on menu | A "p" element was used to encase the jinja code, once removed the food item description was then visible |
| Foods not listing by type, starters, manins and desserts | I needed to fix the database loop for the food items to specify the food type had to be a starter to display in the starter section of the menu, and the same for mains and desserts |
| Drinks not listing by type, wines, beers and cocktails | I needed to fix the database loop for the drinks item to specify the drink type had to be a wine to display in the wine section of the menu, and the same for beers and cocktails |
| Card links not working on home page for book a table, food menu and drinks menu | The links were not set within urls.py so just needed to be wired up to load each relevant page |
| Booking form accepting phone number that are too short | I used Django PhoneNumberField to ensure only valid phone formats were accepted |

##### Back to [top](#table-of-contents)<hr>


### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-01.PNG">
</details>

2. Create an app, give it a name for such as ci-pp4-the-diplomat, and select a region
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-02.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-03.PNG">
</details>

3. Under resources search for postgres, and add a Postgres database to the app
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-04.PNG">
</details>

Heroku Postgres

1. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-18.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-17.PNG">
</details>

2. Install the plugins dj-database-url and psycopg2-binary.

3. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-05.PNG">
</details>

4. Create a Procfile with the text: web: gunicorn the_diplomat.wsgi
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-06.PNG">
</details>

5. In the settings.py ensure the connection is to the Heroku postgres database, no indentation if you are not using a seperate test database.
I store mine in env.py
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-07.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-08.PNG">
</details>

6. Ensure debug is set to false in the settings.py file
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-09.PNG">
</details>

7. Add localhost, and ci-pp4-the-diplomat.herokuapp.com to the ALLOWED_HOSTS variable in settings.py

8. Run "python3 manage.py showmigrations" to check the status of the migrations

9. Run "python3 manage.py migrate" to migrate the database

10. Run "python3 manage.py createsuperuser" to create a super/admin user

11. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories

12. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products

13. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt

14. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ci-pp4-the-diplomat
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-19.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-10.PNG">
</details>


15. Ensure the following environment variables are set in Heroku
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-11.PNG">
</details>

16. Connect the app to GitHub, and enable automatic deploys from main if you wish
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-13.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-14.PNG">
</details>

17. Click deploy to deploy your application to Heroku for the first time

18. Click on the link provided to access the application

19. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue
<hr>

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

##### Back to [top](#table-of-contents)<hr>


## Credits

### Images

Images used were sourced from Pexels.com and an AI image generator (Dalle2) was used for an image with the permission from OpenAI

### Code

Bootstrap dark navigation theme was used alongside boostrap classes and carousel

##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- Code Institute
- My Mentor Mo Shami