# Testing

Return back to the [README.md](README.md) file.

To ensure that The Fox Terriers Owners Club works effectively over several sites and devices, I have prepared details and screenshots for you to see the testing I have done to ensure it is very reliable.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. Which I have put into a tanle below so you can easily check them.


| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2F) | ![screenshot](documentation/testing_images/html/htmlcheck1.png) | Pass: No Errors  |
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/testing_images/html/htmlcheck2.png) | Forbidden code point U+009d. Fixed by removing invalid syntax |
| Register | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing_images/html/htmlcheck3.png) | There was an Error: Duplicate ID signup-form. Server 500. trailing slash. These wouldnt remedy by changing the duplicate Id or removing the slash and were traced back to a google authentication issue which the Tutors dont advise on. So I have had to delete the google and facebook button to resolve the error due to spending to much time on it which I simply dont have. |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing_images/html/htmlcheck4.png) | Pass: No Errors |
| Adoption/Rehome| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fadoption%2F) | ![screenshot](documentation/testing_images/html/htmlcheck5.png) | Pass: No Errors |
| Adoption/rehome details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fadoption%2F29%2F) | ![screenshot](documentation/testing_images/html/htmlcheck9.png) | Pass: No Errors |
| Update adoption/rehome details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fupdate_adoption%2F125%2F) | ![screenshot](documentation/testing_images/html/htmlcheck11.png) | Pass: No Errors |
| Delete adoption/rehome details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fdelete_adoption%2F98%2F) | ![screenshot](documentation/testing_images/html/htmlcheck12.png) | Pass: No Errors |
| No adoption Details | [W3C](https://pimmz-project-4-9cc2ab59cc64.herokuapp.com/adoption/29/) | ![screenshot](documentation/testing_images/html/htmlcheck10.png) | Pass: No Errors |
| Post Room | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fblog.html) | ![screenshot](documentation/testing_images/html/htmlcheck7.png) |  Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](<https://jigsaw.w3.org/css-validator/#validate_by_uri>) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/testing_images/css/csscheck.png) | Pass: No Errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

I have used /* jshint esversion: 11, jquery: true */ at the top of the file so Jshint is allowed to recognize modern ES6 methods, such as:
`let`.

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/testing_images/javascript/javacheck.png) | Unused variables from external file|

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

For lines that have been to long I have shortened everything where possible however there was one section in settings.py that couldnt be shortened due to it affecting the functionality of the code so I have used `# noqa` at the end of those lines so it will ignore linting validation.

![screenshot](documentation/testing_images/python/pychecknoqa.png)


| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/Project-4/main/blog/admin.py) | ![screenshot](documentation/testing_images/python/pycheckadmin.png) | Pass: No Errors  |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/Project-4/main/blog/forms.py) | ![screenshot](documentation/testing_images/python/pycheckforms.png) | Pass: No Errors |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/Project-4/main/blog/models.py) | ![screenshot](documentation/testing_images/python/pycheckmodels.png) | Pass: No Errors |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/project-4/main/blog/urls.py) | ![screenshot](documentation/testing_images/python/pycheckurls.png) | Pass: No Errors |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/Project-4/main/blog/views.py) | ![screenshot](documentation/testing_images/python/pycheckviews.png) | Pass: No Errors |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/Project-4/main/main/settings.py) | ![screenshot](documentation/testing_images/python/pycheckset.png) | Pass: No Errors |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/Project-4/main/main/urls.py) | ![screenshot](documentation/testing_images/python/pycheckurl2.png) | Pass: No Errors |
| wsgi.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/Project-4/main/main/wsgi.py) | ![screenshot](documentation/testing_images/python/pycheckwsgi.png) | Pass: No Errors |
| manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/Project-4/main/manage.py) | ![screenshot](documentation/testing_images/python/py.checkmanage.png) | Pass: No Errors |


## Browser Compatibility

I have tested The Fox Terriers Owners Club on four different browsers using [Browserling](https://www.browserling.com/). I used this site because you can test multiple browsers in one place for free. The first was Chrome, the second was Firefox, the third was Edge and the fourth was Opera.

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://brave.com/download)
- [Opera](https://www.opera.com/download)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/testing_images/Browser/chrometest.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing_images/Browser/firefoxtest.png) | Works as expected |
| Edge | ![screenshot](documentation/testing_images/Browser/edgetest.png) | Works as expected |
| Opera | ![screenshot](documentation/testing_images/Browser/operatest.png) | Works as expected |


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| ipad mini | ![screenshot](documentation/testing_images/responsiveness/ipdadmini.png) | Works as expected |
| ipad air | ![screenshot](documentation/testing_images/responsiveness/ipadair.png) | Works as expected |
| iphonese | ![screenshot](documentation/testing_images/responsiveness/iphonese.png)| Works as expected |
| iphone 12 pro | ![screenshot](documentation/testing_images/responsiveness/iphone12pro.png) | Works as expected |
| iphone xr | ![screenshot](documentation/testing_images/responsiveness/iphonexr.png) | Works as expected |
| Nest hub| ![screenshot](documentation/testing_images/responsiveness/nesthub.png) | Works as expected |
| Nest hub Max| ![screenshot](documentation/testing_images/responsiveness/nesthubmax.png) | Works as expected |
| Pixel 5 | ![screenshot](documentation/testing_images/responsiveness/pixel5.png) | Works as expected |
| Surface duo | ![screenshot](documentation/testing_images/responsiveness/surfaceduo.png) | Works as expected |
| Galaxy A51 / 71 | ![screenshot](documentation/testing_images/responsiveness/a51.png) | Works as expected |
| Galaxy S8 | ![screenshot](documentation/testing_images/responsiveness/galaxys8.png) | Works as expected |
| Galaxy S20 Ultra | ![screenshot](documentation/testing_images/responsiveness/s20ultra.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. 

Desktop
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](documentation/testing_images/lighthouse/homelight.png) | Few warnings |
| About | Desktop | ![screenshot](documentation/testing_images/lighthouse/aboutlight.png) | Few warnings |
| Register | Desktop | ![screenshot](documentation/testing_images/lighthouse/registerlight.png) | Some minor warnings |
| Login | Desktop | ![screenshot](documentation/testing_images/lighthouse/loginlight.png) | Worked as expected |
| Adoption | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptlight.png) | Good overall though average accessibility due to form labels |
| Adoption Detail Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptdetaillight.png) | Worked as expected |
| Adoption Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/updateadoptlight%20.png) | Good overall although accessibilty knocked out slightly by large giph |
| Adoption Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/deleteadoptlight.png) | Worked as expected |
| Rehome Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/rehomelight.png) | good over all with one warning |
| Rehome Detail Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/rehomedetaillight.png) | Worked as expected  |
| Rehome Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/rehomeupdatelight.png) | Good overall although accessibilty knocked out slightly by giph |
| Rehome Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/rehomedetaillight.png) | Worked as expected |
| Post Room Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postroomlight.png) | Average performance due to number of images and size |
| Post Room Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postroomupdate.png) | Good overall though average accessibility |
| Post Room Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postdelete.png) | Worked as expected  |
| Comment Room Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/commentroomlight.png) | Good overall although accessibilty knocked out slightly by giph |


Mobile
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/testing_images/lighthouse/homemoblight.png) | Slow response time due to giph and images. Compressed and using cloudinary to be more effective. |
| About | Mobile | ![screenshot](documentation/testing_images/lighthouse/aboutmoblight.png) | Average performance score due to giph and images|
| Register | Desktop | ![screenshot](documentation/testing_images/lighthouse/regestermoblight.png) | Average performance score due to giph. loaded to cloudinary to be more effective |
| Login | Desktop | ![screenshot](documentation/testing_images/lighthouse/loginmoblight.png) | Average performance score due to giph and images |
| Adoption | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptmoblight.png) |  Average performance score due to giph and accessibility due to form labels|
| Adoption Detail Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptdetailmob.png) | All good except Average performance score due to large giph |
| Adoption Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptupdatemob.png) | Few warning about the giph size and the form elements not having a label. |
| Adoption Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/deletemoblight.png) | All good except Average performance score due to large giph |
| Rehome Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/rehomelight.png) | Average performance score due to giph and accessibility due to form labels |
| Rehome Detail Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/rehomedetailmob.png) | All good except Average performance score due to large giph |
| Rehome Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/rehomeupdatemob.png) | Few warnings on performance and accessibility |
| Rehome Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/rehomedeletemob.png) | All good except Average performance score due to giph |
| Post Room Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postroommob.png) | Average performance due to number of images and size |
| Post Room Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postroommob.png) | Average performance and accessability score due to giph |
| Post Room Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postdeletemob.png) | All good except Average performance score due to  giph |
| Comment Room Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/commentlight.png) | Average performance and accessability score due to giph |


## Defensive Programming

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:

- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):

- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

Flask/Django:

- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo Name | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Brute forcing the URL to get to page for loggin users only |  User redirected to sign up page | Pass |  |
| About Page | | | | |
| | Click on About link in navbar | Redirection to About page | Pass | |
| | Click on Wikipedia links | Wikipedia loaded as expected | Pass | |
| | Brute forcing the URL to get to another user's profile | Redirects user back to own profile | Pass | |
| Register | | | | |
| | Click on Register link in navbar | Redirection to Register page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Submit without filling in all required boxes | Error message appears highlighting area | Pass | |
| Log In | | | | |
| | Click Login link in the navbar | Redirection to Login page | Pass | |
| | Enter valid username | Field will only accept a registered username | Pass | |
| | Enter valid password | Field will only accept a registered password | Pass | |
| Adoption Page | | | | |
| | Click on Adoption link in navbar | Redirection to Adoption page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Select terrier type or sex from drop down menu | User can only choose from the two available choices| Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | No message in textareas | error message appears stating this field is required | Pass | |
| | Click the Submit button | Redirects user to the adoption detail page where they have the opportunity to update / delete or cancel which returns to the adoption page | Pass |  |
| Rehome Page | | | | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Select which terrier or sex from drop down menu | User can only choose from the two available choices | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | No message in textareas | error message appears stating this field is required | Pass | |
| | Click the Submit button | Redirects user to the rehome detail page where they have the opportunity to update / delete or cancel which returns to the adoption page | Pass |  |
| Adoption Detail Page | | | | |
| | Click on Update button | User will be redirected to the Update adoption page | Pass | |
| | Click on the Delete button | User will be redirected to the Delete adoption page | Pass | |
| | Click on the Cancel button | User will be redirected to the Home page | Pass | |
<!--| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |-->
| Rehome Detail Page | | | | |
| | Click on Update button | User will be redirected to the Update adoption page | Pass | |
| | Click on the Delete button | User will be redirected to the Delete adoption page | Pass | |
| | Click on the Cancel button | User will be redirected to the Home page | Pass | |
<!--| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |-->
| Update Adoption Page | | | | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Select terrier type or sex from drop down menu | User can only choose from the two available choices| Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | No message in textareas | error message appears stating this field is required | Pass | |
| | Click the Submit button | Redirects user to the adoption detail page where they have the opportunity to update / delete or cancel which returns to the Update adoption page | Pass |  |
| | Click on the Cancel button | User will be redirected to the Home page  | Pass | |
<!--| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |-->
| Update Rehome Page | | | | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Select terrier type or sex from drop down menu | User can only choose from the two available choices| Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | No message in textareas | error message appears stating this field is required | Pass | |
| | Click the Submit button | Redirects user to the rehome detail page where they have the opportunity to update / delete or cancel which returns to the Update adoption page | Pass |  |
| | Click on the Cancel button | User will be redirected to the Home page  | Pass | |
<!--| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |-->
| Delete Adoption Page | | | | |
| | Click on the Delete Button | Redirection to Adoption page | Pass | Confirms delete first|
| | Click the Delete button | Redirects user to Adoption page  | Pass |  |
| | Click on the Cancel button | User will be redirected to the Home page  | Pass | |
| Delete Rehome Page | | | | |
| | Click on the Delete Button | Redirection to Rehome page | Pass | Confirms delete first|
| | Click the Delete button | Redirects user to the Rehome Page page  | Pass |  |
| | Click on the Cancel button | User will be redirected to the Home page  | Pass | |
| Post Room Page | | | | |
| | Click on Post Room link in navbar | Redirection to Post Room page | Pass | |
| | Enter Title | Field will accept freeform text | Pass | |
| | Enter Content | Field will accept freeform text | Pass | |
| | No message in textareas | error message appears stating this field is required | Pass | |
| | Click on Choose Image button |  Choose your image you want to upload| Pass | |
| | Click on Add Your Post button  | Redirection to Post Room page with message to confirm the post was successful | Pass | |
| | Click post title  | Redirected to the comment room page | Pass | |
| | Click on Update button | User will be redirected to the Update adoption page | Pass | |
| | Click on the Delete button | User will be redirected to the Delete adoption page | Pass | |
| | Click on Update button | Only available to registered user that made the post | Pass | |
| | Click on the Delete button | Only available to registered user that made the post | Pass | |
| Update Post Page | | | | |
| | Click on the Update Button | Redirection to Update post page | Pass | |
| | Enter Title | Field will accept freeform text | Pass | |
| | Enter Content | Field will accept freeform text | Pass | |
| | Choose Image | Change your image you have uploaded| Pass | |
| | Click the Submit button | Redirects user to the comment page  | Pass |  |
| | Click on the Cancel button | User will be redirected to the Post Room page  | Pass | |
| Delete Post Page | | | | |
| | Click on the Delete Button | Redirection to Delete post page | Pass | Confirms delete first|
| | Click the Delete button | Redirects user to the Post Room page  | Pass |  |
| | Click on the Cancel button | User will be redirected to the Post Room page  | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to sign out page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |


⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## User Story Testing

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| User Story | Screenshot |
| --- | --- |
| EPIC User Story | User Profile |
| As a Site User I can register an account so that I can add/edit/delete my adoption plus rehoming requests and comment on the posts of other people's post. | ![screenshot](documentation/readme_images/admin3.png) |
| As a Site User, I can log in or log out of my account so that I can keep my account secure. | ![screenshot](documentation/readme_images/admin4.png) |
| As a Site User I can see my login status so that I know if I'm logged in or out. | ![screenshot](documentation/readme_images/admin5.png) |
|EPIC User Story | User Navigation |
| As a Site User I can immediately understand the purpose of the site so that I can decide if it meets my needs.| ![screenshot](documentation/readme_images/homepage1.png) |
| As a Site User, I can intuitively navigate around the site so that I can find content and understand where I am on the site. | ![screenshot](documentation/readme_images/admin6.png) |
| As a Site User, I can view a paginated list of posts so that I can easily select a post to view. | ![screenshot](documentation/readme_images/postroom.png) |
| As a Site User, I can click on a post so that I can read the full text | ![screenshot](documentation/readme_images/comment.png) |
| As a Site User I can register an account so that I can comment, like, add an adoption and rehome request | ![screenshot](documentation/readme_images/admin3.png) |
| As a Site User, I can view a list of posts so that I can select one to read | ![screenshot](documentation/readme_images/postroom.png) |
|EPIC User Story | Post Management |
| As a Site User, I can update and delete posts that I have created so that I can easily make changes without having to start over. | ![screenshot](documentation/readme_images/postroom.png) |
| As a Site User I can leave comments on a post so that I can be involved in the conversation | ![screenshot](documentation/readme_images/comment.png) |
| As a Site User I can view my posts so that I can see and manage all my own posts, but not be able to change other peoples. | ![screenshot](documentation/readme_images/postroom.png) |
| As a Site User I can view my posts so I can find them easily in one location. | ![screenshot](documentation/readme_images/postroom.png) |
| As a Site user I can like or unlike a post so that I can interact with the content | ![screenshot](documentation/readme_images/comment.png) |
| EPIC User Story | Adoption Interaction |
| As a Site User, I can see my request so that I can find it easily at a later date. | ![screenshot](documentation/readme_images/adoptdetail.png) |
| As a Site User, I can update and delete adoption requests that I have created so that I can easily make changes if I have made a mistake. | ![screenshot](documentation/readme_images/adoptdetail.png) |
| EPIC User Story | Rehome Interaction |
| As a Site User, I can see my request so that I can find it easily at a later date. | ![screenshot](documentation/readme_images/rehomedetail.png) |
| As a Site User, I can update and delete rehome requests that I have created so that I can easily make changes if I have made a mistake. | ![screenshot](documentation/readme_images/rehomedetail.png) |
| EPIC User Story | Site Administration |
| As a Site Administrator, I can create, read, update and delete adoption, rehome requests, posts and comments so that I can manage the app content. | ![screenshot](documentation/readme_images/admin.png) |
| As a Site Administrator, I can view comments on an individual post so that I can read the conversation | ![screenshot](documentation/readme_images/admin1.png) |
| As a Site Admin I can create draft posts so that I can finish writing the content later | ![screenshot](documentation/readme_images/admin2.png) |




## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality.

In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `enter` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work.

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```

Remember to adjust the `fs.readFileSync()` to the specific file you'd like you test.
The example above is testing the `index.html` file.

Finally, at the bottom of the script file where your primary scripts are written, include the following at the bottom of the file.
Make sure to include the name of all of your functions that are being tested in the `.test.js` file.

```js
if (typeof module !== "undefined") module.exports = {
    function1, function2, function3, etc.
};
```

Now that these steps have been undertaken, further tests can be written, and be expected to fail initially.
Write JS code that can get the tests to pass as part of the Red-Green refactor process.

Once ready, to run the tests, use this command:

- `npm test`

**NOTE**: To obtain a coverage report, use the following command:

- `npm test --coverage`

Below are the results from the tests that I've written for this application:

| Test Suites | Tests | Coverage | Screenshot |
| --- | --- | --- | --- |
| 1 passed | 16 passed | 55% | ![screenshot](documentation/js-test-coverage.png) |
| x | x | x | repeat for all remaining tests |

#### Jest Test Issues

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Use this section to list any known issues you ran into while writing your Jest tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Python (Unit Testing)

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Bugs

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

For JavaScript and Python applications, it's best to screenshot the errors to include them as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

  - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

  - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

  - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

  - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

  - To fix this, I _____________________.

### GitHub **Issues**

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: <https://github.com/Pimmz/Project-4/issues>

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/Pimmz/Project-4/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/Pimmz/Project-4/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/Pimmz/Project-4/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/Pimmz/Project-4/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/Pimmz/Project-4/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/Pimmz/Project-4/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/Pimmz/Project-4/issues/5) | Open |

## Unfixed Bugs

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

  - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

  - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

  - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

There are no remaining bugs that I am aware of.
