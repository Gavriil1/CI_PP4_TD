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



### User Goals
- Create/Update/Delete tasks.
- Be able to see all tasks in one place.
- Have access to the manual of the application.
- Read the list of self-development books.

### Site Owner Goals

- To provide a solution to allow users to organize to-do tasks.
- Create an intuitive and easy-to-use application to attract more customers.
- Develop a fully responsive and accessible website.

## User Experience

### Target Audience

- Students: managing assignments, study schedules.
- People with Busy Lifestyles: Manage multiple responsibilities.
- Project Managers: To coordinate and track tasks.
- Individuals Seeking Personal Productivity: To increase personal productivity.
- Freelancers and Gig Workers: To manage their various freelance projects and deadlines


### User Requirements and Expectations

- Fully responsive website on all devices.
- Ability to use the app on all types of devices.
- Calm and relaxing GUI interface.
- Contact Form to engage with support or leave feedback.
- Easy and intuitive application.
- List of books for self-development.

##### Back to [top](#table-of-contents)<hr>


## User Stories

1. As a user, I would like to log in to my account.
2. As a user, I would like to create a new account.
3. As a user, I would like to be able to move from the Register page to the Log In page.
4. As a user, I would like to create a new task. While creating the task, I may modify the following fields: 'title,' 'description,' 'importance,' 'frequency,' 'deadline.'
5. As a user, I would like to update a task. While updating the task, I may modify the following fields: 'title,' 'description,' 'importance,' 'frequency,' 'deadline.'
6. As a user, while on the "Create/Update Task" page, I need to go back without modifying or creating a task.
7. As a user, I would like to delete a task.
8. As a user, while on the "Delete" page, I would like to return to the homepage without deleting the task.
9. As a user, I would like to read the manual to understand how to use the application.
10. As a user, I would like to be able to send an email to the admin to contact him or share feedback.
11. As a user, I would like to see the list of books the admin proposes for self-development and visit the Amazon website where I can buy them.



### Admin / Authorised User

12. In my role as an Admin or Authorized User, I have the capability to log in to the admin console for backend access.
13. As an Admin, I can create users, delete users.
14. As an Admin, I want to modify user's settings: First Name, Permissions.
15. As an Admin, I want to filter users by staff, superuser, or active status.
16. As an Admin, I am able to manually include, remove, or update books in the list of favorite books.
17. As an Admin, I can view messages that have been sent by users through the contact form.
18. As an Admin, I can view, update, delete users' tasks.
19. As an Admin, I can filter tasks by: importance, frequency, user.
20. As an Admin, I would like a user to find all company's social links and navigate to them by clicking footer's icons.

## Design

### Colours

I chose bright colors for the footer and navbar to make the application more positive.
I added a picture with a starry sky to make the application relaxing.

### Structure

#### Website pages

The site was designed for the user to be familiar with the layout, such as a navigation bar along the top of the pages and a hamburger menu button for smaller screens.

The footer contains all relevant social media links that the business has, so the user can visit any social media site and follow the business there to expand the business's followers, likes, and shares.

The site consists of the following pages:

- Login page where the user can log in to his account.
- Register page where the user can register.
- Homepage where the user can see all his tasks.
- Create/Update task page, where the user can create or update the task.
- Delete page, where the user can delete the task.
- Manual page, where the user can read how to use the application.
- Contact/Feedback page, where the user can complete a form to share his feedback or just send an email to the admin/owner.
- Books page, where the user can see the admin's favorite books on sales development.
- 404 error page to display if a 404 error is raised.

#### Database

- Built with Python and the Django framework with a database of ElephantSQL for the deployed Heroku version (production).


<details><summary>Show diagram</summary>
<img src="docs/databases/databases.png">
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

##### Contact Model
The Contact Model contains the following:
- id
- name
- email
- subject
- message


##### Books Model
The Books Model contains the following:
- id
- title
- details
- stars
- numberreviews
- price
- productpic
- amazon


##### Tasks Model
The Tasks Model contains the following:
- id
- user
- title
- description
- complete
- created
- frequency
- importance
- completed
- due


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
- Home page includes navbar, main body, and a footer.


<details><summary>See feature images</summary>

![Home page](docs/features/feature-homepage.png)
</details>


### Logo & Navigation
- Shows logo designed for a to-do list.
- Responsive across various screen sizes.
- Transforms into hamburger menu on smaller screens.
- Shows active user.
- Provides access to all available pages directly from the current page.

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

### Social Media Links and CopyRight
- A logo and link is used for each social media displayed
- All links open in a new tab to ensure user is not directed away from the business
- Displayed on all pages
  
<details><summary>See feature images</summary>

![Social Media Links](docs/features/media-links.png)
</details>


### Pagination
- Pagination is used on the bookings list and the blog page
- Ensures the page is kept tidy as only 2 items are displayed per page
  
<details><summary>See feature images</summary>

![Pagination](docs/features/pagination.png)
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

<details><summary>python/base/test_forms.py</summary>
<img src="docs/validation/python/base/test_forms_validation_base.png">
</details>

<details><summary>python/base/test_models.py</summary>
<img src="docs/validation/python/base/test_models_validation_base.png">
</details>

<details><summary>python/base/test_views.py</summary>
<img src="docs/validation/python/base/test_views_validation_base.png">
</details>

<details><summary>python/base/test_urls.py</summary>
<img src="docs/validation/python/base/test_url_validation_base.png">
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

<details><summary>python/books/test_models.py</summary>
<img src="docs/validation/python/books/test_models_book.png">
</details>

<details><summary>python/books/test_views.py</summary>
<img src="docs/validation/python/books/test_views_books.png">
</details>

<details><summary>python/books/test_urls.py</summary>
<img src="docs/validation/python/books/test_url_book.png">
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

<details><summary>python/contactform/test_models.py</summary>
<img src="docs/validation/python/contactform/test_models_contactform.png">
</details>

<details><summary>python/contactform/test_views.py</summary>
<img src="docs/validation/python/contactform/test_views_contactform.png">
</details>

<details><summary>python/contactform/test_urls.py</summary>
<img src="docs/validation/python/contactform/test_urls_contactform.png">
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



### Manual testing

## User Stories

1.  As a User I would like to login to my account.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 | Open application URL. See login page. User credentials to log in | User logs in | Works as expected |


<details><summary></summary>
<img src="docs/userstories/log-in-to-user-account.png">


</details>

2. As a User I would like to create a new account.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| On login page click "Sign Up". On register page register your username and password | New account is created and user logged in | Works as expected |

<details><summary></summary>
<img src="docs/userstories/register-an-account-user-account.png">

</details>

3.  As a User I would like to be able to move from Register page to Log In Page.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| On Register page, click on  link "Login". | User is redirected to Log In Page | Works as expected |

<details><summary></summary>
<img src="docs/userstories/redirect-register-login.png">

</details>

4. As a user, I would like to create a new task. While creating the task, I may modify the following fields: 'title', 'description',  'importance','frequency', 'deadline'.

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| On homepage, click "Add New". On Create/Update page. Complete fields: 'title,' 'task description,' select the 'deadline,' 'severity,' 'importance,' 'frequency' and click Submit| New Task is created with required fields. | Works as expected |

<details><summary></summary>
<img src="docs/userstories/create-new-task.png">

</details>

5. As a user, I would like to update a new task. While updating the task, I may modify the following fields: 'title', 'description',  'importance','frequency', 'deadline'.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on a penscil in edit colon. On "Create/Update Task" you may6 modify one of the following fields: 'title', 'description',  'importance','frequency', 'deadline' | Task Modified | Works as expected |

<details><summary></summary>
<img src="docs/userstories/update-a-task.png">

</details>

6. As a user, while I am on "Create/Update Task" I need to go back, without modifying or creating task.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| While on "Create/Update" page click on an arrow on left top corner.| User is redirected to Homepage  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/create-update-homepage.png">

</details>

7. As a user I would like to delete the task.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on x in Edit colon. On Delete page click "Delete" | The task is deleted  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/delete-task.png">
</details>

8. As a user, while on "Delete" page I would like to return to homepage without deleting the task.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| While on a "Delete" page, click on the arrow on the top left corner| The user redirected back to homepage, task is not deleted  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/delete-homepage.png">

</details>


9. As a user,  I would like to read manual, to understand how to use the application.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| While on homepage, click "Manual" in navigation bar | The user redirected to manual page where he can read instructions.  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/read-manual.png">

</details>

10. As a user I would like to be able to send an email to admin, to contact him or share feedback.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| While on homepage, click "Feedback", complete all fields and click send feedback. | User redirected to homepage, and see the message that the email was received  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/feedback-1.png">
<img src="docs/userstories/feedback-2.png">
</details>

11. As a user I would like to see the list of book the admin propose for self development, and visit Amazon website where I can buy it.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| While on homepage, click "Books". See books' cover, description, rating. Click on button "Buy on Amazon" to navigate to Amazon page, where you may buy a book | User redirected to 'Books' page and after to Amazon's website  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/login-administration-panel.png">

</details>

## Testing Admin user stories:

12. In my role as an Admin or Authorized User, I have the capability to log in to the admin console for backend access.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| navigate to https://ci-pp4-td-014f88cd1918.herokuapp.com/admin/ Complete username and Password and click next to login | User redirected to admin console.  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/books.png">

</details>


## Admin/Site owner user stories.

13. As an Admin, I can create user, delete user .

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| In admin console, click Users. Click "Add User" in the right top corner to create a user, complete Username and passwords fields and click Save. Select a user, from "Action" select "Delete selected user" click go | One user is created, one user is deleted  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/create-user-admin.png">
<img src="docs/userstories/delete-user-admin.png">

</details>

14. As an Admin, I want to modify user's settings: Firs Name, Perissions.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| In admin console click on "Users", click on user, modify user's settings and click "Save" | User's settings are updated.  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/update-users-settings.png">


</details>

15. As an Admin, I want to filter user by staff , superuser or active status.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| In admin console click "Users", "Filter", select required filter settings. | Users are filtered according to filter settings.  | Works as expected |

<details><summary></summary>
<img src="docs/userstories/filter-users-admin.png">


</details>


16. As an Admin  I am able to manually include, remove, or update books in the list of favorite books.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| In admin console click "Products". On the top right corner select "Add Product, complete all the fields, and click Save. To update click on a book text, update all required fields and click Save. To delete a book, select a book, "Action", "Delete selected products", "Go"| Book added, updated deleted sucesfully | Works as expected |

<details><summary></summary>
Add a new book.
<img src="docs/userstories/add-book-admin.png">
Update a book.
<img src="docs/userstories/update-book-admin.png">
Delete a book.
<img src="docs/userstories/delete-book-admin.png">


</details>




17. As an Admin , I can view messages that have been sent by users through the contact form.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| In admin console, click on Contacts, and click on the text of a message.  | A new window opens, and I can see full   message which was sent by user. | Works as expected |

<details><summary></summary>
<img src="docs/userstories/view-feedback-admin.png">



</details>

18. As an Admin , I can view, update, delete user's tasks

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Navigate to "Tasks", Click on task.  | A new window opens,where I can see, update or delete the task | Works as expected |

<details><summary></summary>
<img src="docs/userstories/view-udpate-delete-task.png">

</details>

19. As an Admin , I can filter tasks by: importance, frequency, user

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Navigate to "Tasks". Find Filter, set desired filters.  | Tasks are filterd according to filter settings. | Works as expected |

<details><summary></summary>
<img src="docs/userstories/filter-tasks-admin.png">

</details>

20. As an Admin , I would like a user to find all company's social links, and navigate to them be clicking footer's icons/

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| On homepage find footer. Click on one of the icons  | User is redirected to social media | Works as expected |

<details><summary></summary>
<img src="docs/userstories/social-media-admin.png">

</details>

### Automated testing

- Testing was done using the built in Django module, unittest.
- Coverage was also usesd to generate a report

<br>

<details><summary>base, test_models.py</summary>
<img src="docs/automatic_testing/base/base_test_models.png">
</details>

<details><summary>base, test_views.py</summary>
<img src="docs/automatic_testing/base/base_test_views.png">
</details>

<details><summary>base, test_urls.py</summary>
<img src="docs/automatic_testing/base/base_test_url.png">
</details>

<details><summary>base, test_form.py</summary>
<img src="docs/automatic_testing/base/base_test_form.png">
</details>

<br>

<details><summary>books, test_models.py</summary>
<img src="docs/automatic_testing/books/books_test_models.png">
</details>

<details><summary>books, test_views.py</summary>
<img src="docs/automatic_testing/books/books_test_views.png">
</details>

<details><summary>books, test_urls.py</summary>
<img src="docs/automatic_testing/books/books_test_urls.png">
</details>

<br>

<details><summary>contactform, test_models.py</summary>
<img src="docs/automatic_testing/contactform/test_models_contactform.png">
</details>

<details><summary>contactform, test_views.py</summary>
<img src="docs/automatic_testing/contactform/test_views_contactform.png">
</details>

<details><summary>contactform, test_urls.py</summary>
<img src="docs/automatic_testing/contactform/test_url_contactform.png">
</details>



<br>

<details><summary>Coverage Report For All Applications</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/coverage-bookings.PNG">
</details>


### Device Testing & Browser compatibility

###  Performing tests on various devices

Testing of the website was conducted on the following devices:

- Latitude 5520

- Redmi Note 10

- Samsung Tablet A10.1

Furthermore, the website underwent testing using the Device Toggling feature of Google Chrome Developer Tools, which includes all available device options.

###  Browser compatability

The following browsers were used to test the website:

- Google Chrome

- Mozilla Firefox

- Microsoft Egde



##### Back to [top](#table-of-contents)<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| css not loading| static files confiugration in settings.py was not correct, after fixing it the issue resolved. |
| User could see the tasks of other users| Denesive programming. Configured user's to see only their tasks by adding mydata = Task.objects.filter(user=request.user) to the equation|
|  Users could update and delete other users' tasks |  Adjusted cosde which check if task belongs to the user, and it is not it show 404 page |
| Footer was not on the button of the page, when the content was big. | Changed footer class to class="text-center text-white fixed-bottom" . After that the issue fixed on all pages. |
| The contact form was not saving subject of a message in admin | modified views.py script for feedback page to link correct subject to correct variable. |
| Homepage, was not showing correct display when tasks of the user were 0| I found that it was counting tasks in other, users. Added additional filter which made application to count tasks only of logged user and not all users by adding   user=request.user|
| Update page did not open, when I pressed on update button | The links were not set within urls.py so just needed to be wired up to load each relevant page |

##### Back to [top](#table-of-contents)<hr>


### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

### Heroku Deployment

Before deploying to Heroku, environment variables must be defined in the django project so that local development functions correctly. Once these environment variables are set up in the workspace, the project can be deployed and the environment variables can be copied into heroku as config vars (to ensure the deployed app works correctly with 3rd party dependecies.)

1. Create a file called env.py in the root directory of your workspace and ensure that the file is included in .gitignore. These variables should NOT be committed and pushed to GitHub.
2. import os to the file.
3. os.environ['DATABASE_URL'] = URL copied from ElephantSQL
4. os.environ['SECRET_KEY'] = A randomly generated key of your choosing. This keeps django from serving data to/from an unauthorised source.
5. os.environ['CLOUDINARY_URL'] = The URL from a cloudinary account. This can be found on the following page on the cloudinary website: www.cloudinary.com
<details><summary>Cloudinary</summary>
<img src="docs/heroku-deployment/cloudinari-key.png">
</details>
These environment variables can now be accessed and configured in the settings.py file of the django project.

The website was deployed to Heroku using the following process:

1. Login to  [Heroku](https://dashboard.heroku.com/) 

<details><summary>Heroku Login</summary>
<img src="docs/heroku-deployment/login-heroku.png">
</details>

2. Click on New > Create new app in the top right of the screen.
<details><summary>Create New App</summary>
<img src="docs/heroku-deployment/create-new-app.png">
</details>

3. Add an app name and select location, then click 'create app'.

<details><summary>Create New App</summary>
<img src="docs/heroku-deployment/select-app-region.png">
</details>

4. Under the deploy tab of the next page, select connect to GitHub.
5. Log in to your GitHub account when prompted.
<details><summary>Github Deploy</summary>
<img src="docs/heroku-deployment/deploy-app.png">
</details>

6. Select the repository that you want to be connected to the Heroku app.
<details><summary>Select Repository</summary>
<img src="docs/heroku-deployment/connect-to-github-project.png">
</details>
7. Click on the settings and in "Config Vars" click on "Reveal Config Vars".
<details><summary>Select Repository</summary>
<img src="docs/heroku-deployment/reveal-vars.png">
</details>
8. Scroll down to the config vars section, and add config vars specified at the start of this section of the README. Also, include a var with the key 'PORT' and value '8000' to avoid build errors. The end result should look something like this:
KEY: DATABASE_URL
VALUE: postgresurlexample123.com
<details><summary>Configure Vars</summary>
<img src="docs/heroku-deployment/var-configuration.png">
</details>
9. Navigate back to the 'deploy' tab.
10.  Select automatic deploys to allow Heroku to build the site with new changes each time changes are pushed to GitHub.
<details><summary>Automatic Deploy</summary>
<img src="docs/heroku-deployment/automatic-deploy.png">
</details>
11.  In the 'manual deploy' section beneath this, make sure the branch selected is 'main' and click deploy branch.
<details><summary>Automatic Deploy</summary>
<img src="docs/heroku-deployment/manual-deploy.png">
</details>
12.  The site should now be built and Heroku should provide a url for the built site.
<hr>

### Clone Repository
Follow these steps to clone the repository:
1. Go to the GitHub repository 
2. Find the "Code" button located above the file list and click on it.
3. Choose whether you prefer to clone via HTTPS, SSH, or Github CLI, and then click on the copy button to copy the URL to your clipboard.
4. Open Git Bash
5. Navigate to the directory where you would like to clone the directory and set it as the current working directory.
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Hit the Enter key to create your local clone.

Please check the following link for more information: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

##### Back to [top](#table-of-contents)<hr>


## Credits

### Images

Backgroun image was taken from https://getwallpapers.com/

### Code

1. First version of the App was built from Django Tutorial of Dennis Ivy: https://www.youtube.com/watch?v=llbtoQTt4qw
2. Code which is locatd on Bootstrap 4.6 page https://getbootstrap.com/docs/4.6/getting-started/introduction/  was used to deploy NavBar and Footer
3. Pagination was taken from this video: https://www.youtube.com/watch?v=wY_BNsxCEi4&t=61s
4. Login, Register, Feedback pages are inspired from: https://bootsnipp.com/snippets/vl4R7
5. Automatic testing: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2


##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- Code Institute
- My Mentor Mo Shami