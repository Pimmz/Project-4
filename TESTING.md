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
| Register | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing_images/html/htmlcheck3.png) |  Pass: No Errors  |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing_images/html/htmlcheck4.png) | Pass: No Errors |
| Adoption/Rehome| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fadoption%2F) | ![screenshot](documentation/testing_images/html/htmlcheck5.png) | Pass: No Errors |
| Adoption/rehome details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fadoption%2F29%2F) | ![screenshot](documentation/testing_images/html/htmlcheck9.png) | Pass: No Errors |
| Update adoption/rehome details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fupdate_adoption%2F125%2F) | ![screenshot](documentation/testing_images/html/htmlcheck11.png) | Pass: No Errors |
| Delete adoption/rehome details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fdelete_adoption%2F98%2F) | ![screenshot](documentation/testing_images/html/htmlcheck12.png) | Pass: No Errors |
| No adoption Details | [W3C](https://pimmz-project-4-9cc2ab59cc64.herokuapp.com/adoption/29/) | ![screenshot](documentation/testing_images/html/htmlcheck10.png) | Pass: No Errors |
| Post Room | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpimmz-project-4-9cc2ab59cc64.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2Fblog.html) | ![screenshot](documentation/testing_images/html/html.check7.png) |  Pass: No Errors |

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

For lines that have been too long I have shortened everything where possible however there was one section in settings.py that couldn't be shortened due to it affecting the functionality of the code so I have used `# noqa` at the end of those lines so it will ignore linting validation.

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
| manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/Project-4/main/manage.py) | ![screenshot](documentation/testing_images/python/pycheckmanage.png) | Pass: No Errors |


## Browser Compatibility

I have tested The Fox Terriers Owners Club on four different browsers using [Browserling](https://www.browserling.com/). I used this site because you can test multiple browsers in one place for free. The first was Chrome, the second was Firefox, the third was Edge and the fourth was Opera.

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://brave.com/download)
- [Opera](https://www.opera.com/download)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/testing_images/browser/chrometest.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing_images/browser/firefoxtest.png) | Works as expected |
| Edge | ![screenshot](documentation/testing_images/browser/edgetest.png) | Works as expected |
| Opera | ![screenshot](documentation/testing_images/browser/operatest.png) | Works as expected |


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
| Register | Desktop | ![screenshot](documentation/testing_images/lighthouse/registerlight.png) | Worked as expected |
| Login | Desktop | ![screenshot](documentation/testing_images/lighthouse/loginlight.png) | Worked as expected |
| Adoption/Rehome | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptlight.png) | Worked as expected |
| Adoption/Rehome Detail Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptdetaillight.png) | Worked as expected |
| Adoption/Rehome Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/updateadoptlight.png) | Worked as expected |
| Adoption/Rehome Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/deleteadoptlight.png) | Worked as expected |
| Post Room Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postroomlight.png) | Average performance due to number of images and size |
| Post Room Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postroomupdate.png) | Good overall though average accessibility |
| Post Room Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postdelete.png) | Worked as expected  |
| Comment Room Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/commentroomlight.png) | Good overall although accessibility knocked out slightly by gif |

Mobile
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/testing_images/lighthouse/homemoblight.png) | Slow response time due to gif and images. Compressed and using cloudinary to be more effective. |
| About | Mobile | ![screenshot](documentation/testing_images/lighthouse/aboutmoblight.png) | Average performance score due to gif and images|
| Register | Desktop | ![screenshot](documentation/testing_images/lighthouse/regestermoblight.png) | Average performance score due to gif. loaded to cloudinary to be more effective |
| Login | Desktop | ![screenshot](documentation/testing_images/lighthouse/loginmoblight.png) | Average performance score due to gif and images |
| Adoption/Rehome | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptmoblight.png) |  Average performance score due to gif |
| Adoption/Rehome Detail Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptdetailmob.png) | All good except Average performance score due to large gif |
| Adoption/Rehome Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/adoptupdatemob.png) | All good except Average performance score due to large gif. |
| Adoption/Rehome Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/deletemoblight.png) | All good except Average performance score due to large gif |
| Post Room Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postroommob.png) | Average performance due to number of images and size |
| Post Room Update Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postroommob.png) | Average performance and accessability score due to gif |
| Post Room Delete Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/postdeletemob.png) | All good except Average performance score due to  gif |
| Comment Room Page | Desktop | ![screenshot](documentation/testing_images/lighthouse/commentlight.png) | Average performance and accessability score due to gif |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo Name | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Brute forcing the URL to get to the page for loggin users only |  User redirected to sign up page | Pass |  |
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
| Adoption/Rehome Page | | | | |
| | Click on Adoption link in navbar | Redirection to Adoption page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Select terrier type or sex from drop down menu | User can only choose from the two available choices| Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | No message in textareas | error message appears stating this field is required | Pass | |
| | Click the Submit button | Redirects user to the adoption detail page where they have the opportunity to update/delete or cancel which returns to the adoption page | Pass |  |
| Adoption/Rehome Detail Page | | | | |
| | Click on Update button | User will be redirected to the Update adoption page | Pass | |
| | Click on the Delete button | User will be redirected to the Delete adoption page | Pass | |
| | Click on the Cancel button | User will be redirected to the Home page | Pass | |
| | Brute forcing the URL to get to another user's profile | User will not be allowed access | Pass | Redirects user back to own profile |
| Update Adoption/Rehome Page | | | | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Select terrier type or sex from drop-down menu | User can only choose from the two available choices| Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | No message in textareas | error message appears stating this field is required | Pass | |
| | Click the Submit button | Redirects user to the adoption detail page where they have the opportunity to update/delete or cancel which returns to the Update adoption page | Pass |  |
| | Click on the Cancel button | User will be redirected to the Home page  | Pass | |
| | Brute forcing the URL to get to another user's profile | User will not be allowed access | Pass | Redirects user back to own profile |
| Delete Adoption/Rehome Page | | | | |
| | Click on the Delete Button | Redirection to Adoption page | Pass | Confirms delete first|
| | Click the Delete button | Redirects user to Adoption page  | Pass |  |
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

## User Story Testing

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
| EPIC User Story | Adoption/Rehome Interaction |
| As a Site User, I can see my request so that I can find it easily at a later date. | ![screenshot](documentation/readme_images/updateadoptdetails.png) |
| As a Site User, I can update and delete adoption/rehome requests that I have created so that I can easily make changes if I have made a mistake. | ![screenshot](documentation/readme_images/adoptdetail.png) |
| EPIC User Story | Site Administration |
| As a Site Administrator, I can create, read, update and delete adoption, rehome requests, posts and comments so that I can manage the app content. | ![screenshot](documentation/readme_images/admin.png) |
| As a Site Administrator, I can view comments on an individual post so that I can read the conversation | ![screenshot](documentation/readme_images/admin1.png) |
| As a Site Admin I can create draft posts so that I can finish writing the content later | ![screenshot](documentation/readme_images/admin2.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)



### Python (Unit Testing)

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
| Blog | test___init__.py | 100% | ![screenshot](documentation/testing_images/pythontesting/coverage.png) |
| Blog | test_admin.py | 92% | ![screenshot](documentation/testing_images/pythontesting/coverage.png) |
| Blog | test_apps.py | 79% | ![screenshot](documentation/testing_images/pythontesting/coverage.png) |
| Blog | test_forms.py | 99% | ![screenshot](documentation/testing_images/pythontesting/coverage.png) |
| Blog | test_models.py | 87% | ![screenshot](documentation/testing_images/pythontesting/coverage1.png) |
| Blog | test_test.py | 99% | ![screenshot](documentation/testing_images/pythontesting/coverage1.png) |
| Blog | test_urls.py | 89% | ![screenshot](documentation/testing_images/pythontesting/coverage1.png) |
| Blog | test_views.py | 43% | ![screenshot](documentation/testing_images/pythontesting/coverage1.png) |
| Main | test___init__.py | 100% | ![screenshot](documentation/testing_images/pythontesting/coverage2.png) |
| Main | test_asgi.py | 0% | ![screenshot](documentation/testing_images/pythontesting/coverage2.png) |
| Main | test_settings.py   | 100% | ![screenshot](documentation/testing_images/pythontesting/coverage2.png) |
| Main | test_urls.py| 100% | ![screenshot](documentation/testing_images/pythontesting/coverage2.png) |
| Main | test_wsgi.py | 0% | ![screenshot](documentation/testing_images/pythontesting/coverage2.png) |

![screenshot](documentation/testing_images/pythontesting/coveragereport.png) |

#### Unit Test Issues


Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

## Bugs

- Page not found, error 404

    ![screenshot](documentation/testing_images/bug/bug01.png)

  - I fixed this, by ensuring the path was correct in the url.

- Invalid cloudinary url scheme

    ![screenshot](documentation/testing_images/bug/bug02.png)

  - To fix this, I corrected the url to 'cloudinary://'

- Rehome not defined

    ![screenshot](documentation/testing_images/bug/bug03.png)

  - To fix this, I imported rehome in the views as I had forgotten to put it in.


- Python `E501 line too long` (90 > 79 characters)

    ![screenshot](documentation/testing_images/bug/bug04.png)

  - To fix this, I split the line onto two lines ensuring it was split so it would nt cause any errors  


## Unfixed Bugs

There are no remaining bugs that I am aware of.
