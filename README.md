# DCMS - Digital Compliance Management System

The live link for the site can be found here - https://project5-dcms-react.herokuapp.com/

The live link for the API can be found here - https://project5-dcms-drf-api.herokuapp.com/

# Table of Contents
<!-- - [Overview](#overview)
- [UX](#ux)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Languages Used](#languages-used)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [CRUD](#crud)
  - [Other Features](#other-features)
  - [Future Features](#future-features)
- [Testing](#testing)
  - [Automated Testing](#automated-testing)
  - [Manual Test of User Stories](#manual-test-of-user-stories)
  - [Test on Alternative Browsers and Screen Size](#test-on-alternative-browsers-and-screen-size)
  - [Debugging](#debugging)
  - [Validator Testing](#validator-testing)
  - [Unfixed Bugs](#unfixed-bugs)
- [Libraries and Programs Used](#libraries-and-programs-used)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content) -->

# Overview

This site was developed to address a problem which occurred during my previous employment as a Senior Account Manager for a Health and Safety Consultancy. I worked with clients with a large estate of sites throughout the UK. The central health and safety team did not know whether any of the compliance checks were being completed unless they attended site and reviewed the paper checklists used to record the completion of tasks or actions. I have created this site as a way of solving this issue.

# User Stories

As seen above, there will only be two different types of user of this site (Site User and Site Admin). I have broken down my user stories into these two categories:

*Categories*

- View Categories List: As a **site admin** I can **view the categories list** so that **I can ensure that all appropriate categories are available to be allocated to a task or action**.
- Add Categories: As a **site admin** I can **create a category** so that **it can be allocated to a task or action**.
- Edit Categories: As a **site admin** I can **edit a category** so that **the correct category can be allocated to a task or action**.
- Delete Categories: As a **site admin** I can **delete a category** so that **it is no longer available to be allocated to a task or action**.

*Master Tasks*

- View Master Task List: As a **site admin** I can **view the master task list** so that **to ensure all users have been allocated the appropriate tasks**.
- View Master Task Details: As a **site admin** I can **view the master task details** so that **to ensure that the correct information has been set on a master task**.
- Add Master Task: As a **site admin** I can **add a master task** so that **I am able to allocate a master task to a user**.
- Edit Master Task: As a **site admin** I can **edit a master task** so that **I am able to update a master task if any of the requirements change**.
- Delete Master Task: As a **site admin** I can **delete a master task** so that **it is no longer available to be allocated to a user**.
- Search for Master Tasks:	As a **site admin** I can **search for master tasks** so that **so it is easy to find the master task which I am looking for**.

*Assign Tasks*

- Allocate Master Task to User: As a **site admin** I can **allocate a master task to a user** so that **so a user task can be allocated to them to ensure that an activity is being completed**.
- Set Completed By: As a **site admin** I can **set who the task is to be completed by** so that **either the admin or the user is aware that a task requires completing by them**.

*User Tasks*

- Add User Task: As a **site admin** I can **automatically create a user task once a master task has been allocated** so that **I know a user task has been created which requires completion**.
- View User Task List: As a **site user/site admin** I can **view the user tasks which are to be completed by me** so that **I am aware what tasks I need to completed**.
- View Overdue User Task List: As a **site user/site admin** I can **view the overdue user tasks which are to be completed by me** so that **I can prioritise completing tasks which are overdue**.
- Filter User Tasks: As a **site user/site admin** I can **filter user tasks** so that **so it is eay to find the user task which I am looking for**.
- Search for User Tasks: As a **site user/site admin** I can **search for user tasks** so that **so it is eay to find the user task which I am looking for**.
- View User Task Details: As a **site user/site admin** I can **view a user tasks details** so that **I am aware what tasks I need to completed**.
- Update User Task Status: As a **site user/site admin** I can **update a user tasks status** so that **I can record whether a task has been completed or is in progress**.
- Add Image to User Task: As a **site user/site admin** I can **add an image to a user task** so that **I can provide additional evidence that a task has been completed or that an issue was identified**.

*User Tasks: Comments*

- View Task Comments: As a **site user/site admin** I can **view task comments** so that **I can read the log of detailed information recorded about a task**.
- Add Task Comment: As a **site user/site admin** I can **add a comment to a task** so that **I can record whether an issue has been raised or detail information about the completion of a task**.
- Edit Task Comment: As a **site user/site admin** I can **edit a task comment** so that **I can update an error made in a comment**.
- Delete Task Comment: As a **site user/site admin** I can **delete a task comment** so that **I can delete a comment which has been incorrectly submitted**.
- Task Status Update Comment: As a **site user/site admin** I can **automatically add a comment to detail a change in an tasks status** so that **the comments have a log of any changes to the status of the task**.

*Actions*

- View Action List: As a **site user/site admin** I can **view the actions which are to be completed by me** so that **I am aware what actions I need to completed**.
- View Action Details: As a **site user/site admin** I can **view an actions details** so that **I am aware of the details of the action which I need to completed**.
- Add Action: As a **site user/site admin** I can **add an action** so that **I can record any issues identified so they can be addressed at a later date**.
- Add Action related to a Task: As a **site user/site admin** I can **raise an action if an issue was raise when completing a task** so that **I can record any issues identified when completing a task so they can be addressed at a later date**.
- Edit Action: As a **site user/site admin** I can **edit an action** so that **I am able to update an action if any of the requirements change**.
- Delete Action: As a **site user/site admin** I can **delete an action** so that **I can delete an action which has been incorrectly submitted**.

*Actions: Comments*

- View Action Comments: As a **site user/site admin** I can **view action comments** so that **I can read the log of detailed information recorded about an action**.
- Add Action Comment: As a **site user/site admin** I can **add a comment to an action** so that **I can log the progress of the completion of an action**.
- Edit Action Comment: As a **site user/site admin** I can **edit an action comment** so that **I can update an error made in a comment**.
- Delete Action Comment: As a **site user/site admin** I can **delete an action comment** so that **I can delete a comment which has been incorrectly submitted**.
- Action Status Update Comment: As a **site user/site admin** I can **automatically add a comment to detail a change in an actions status** so that **the comments have a log of any changes to the status of the action**.

The user stories where then managed in a Kanban board which was created in [GitHub Projects](https://github.com/users/TuckerFaulk/projects/5/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%2C%22Milestone%22%5D). User stories were then prioritized with the MoSCoW approach and labels where used to manage this. The kanban board was split into five columns to manage the various stages of development:

1. To do: This item hasn't been started
2. In Progress - DRF API: This item is actively being worked on in the DRF API
3. To do - React: This item has tasks related to the React App which have not been started
4. In Progress - React: This item is actively being worked on in the React App
5. Done: All tasks related to the DRF API and the React App have been completed

# Site Navigation Flowchart

![Flowchart](readme_images/flowchart.png)

# Database Schema

Data normalisation to structure each relational model to help reduce data redundancy and improve data integrity was used after initially setting out all of the information required for the site.

![Database Schema](src/assets/README_images/data_model.png)

# Languages Used

- Python
- SQL (Postgres)

# Testing

## Manual Test of User Stories

| User Story Tested |  Passed |
|-------|:--------:|
|View Categories List: As a **site admin** I can **view the categories list** so that **I can ensure that all appropriate categories are available to be allocated to a task or action**.|☑|
|Add Categories: As a **site admin** I can **create a category** so that **it can be allocated to a task or action**.|☑|
|Edit Categories: As a **site admin** I can **edit a category** so that **the correct category can be allocated to a task or action**.|☑|
|Delete Categories: As a **site admin** I can **delete a category** so that **it is no longer available to be allocated to a task or action**.|☑|
|View Master Task List: As a **site admin** I can **view the master task list** so that **to ensure all users have been allocated the appropriate tasks**.|☑|
|View Master Task Details: As a **site admin** I can **view the master task details** so that **to ensure that the correct information has been set on a master task**.|☑|
|Add Master Task: As a **site admin** I can **add a master task** so that **I am able to allocate a master task to a user**.|☑|
|Edit Master Task: As a **site admin** I can **edit a master task** so that **I am able to update a master task if any of the requirements change**.|☑|
|Delete Master Task: As a **site admin** I can **delete a master task** so that **it is no longer available to be allocated to a user**.|☑|
|Search for Master Tasks	As a **site admin** I can **search for master tasks** so that **so it is easy to find the master task which I am looking for**.|☑|
|Allocate Master Task to User: As a **site admin** I can **allocate a master task to a user** so that **so a user task can be allocated to them to ensure that an activity is being completed**.|☑|
|Set Completed By: As a **site admin** I can **set who the task is to be completed by** so that **either the admin or the user is aware that a task requires completing by them**.|☑|
|Add User Task: As a **site admin** I can **automatically create a user task once a master task has been allocated** so that **I know a user task has been created which requires completion**.|☑|
|View User Task List: As a **site user/site admin** I can **view the user tasks which are to be completed by me** so that **I am aware what tasks I need to completed**.|☑|
|View Overdue User Task List: As a **site user/site admin** I can **view the overdue user tasks which are to be completed by me** so that **I can prioritise completing tasks which are overdue**.|☑|
|Filter User Tasks: As a **site user/site admin** I can **filter user tasks** so that **so it is eay to find the user task which I am looking for**.|☑|
|Search for User Tasks: As a **site user/site admin** I can **search for user tasks** so that **so it is eay to find the user task which I am looking for**.|☑|
|View User Task Details: As a **site user/site admin** I can **view a user tasks details** so that **I am aware what tasks I need to completed**.|☑|
|Update User Task Status: As a **site user/site admin** I can **update a user tasks status** so that **I can record whether a task has been completed or is in progress**.|☑|
|Add Image to User Task: As a **site user/site admin** I can **add an image to a user task** so that **I can provide additional evidence that a task has been completed or that an issue was identified**.|☑|
|View Task Comments: As a **site user/site admin** I can **view task comments** so that **I can read the log of detailed information recorded about a task**.|☑|
|Add Task Comment: As a **site user/site admin** I can **add a comment to a task** so that **I can record whether an issue has been raised or detail information about the completion of a task**.|☑|
|Edit Task Comment: As a **site user/site admin** I can **edit a task comment** so that **I can update an error made in a comment**.|☑|
|Delete Task Comment: As a **site user/site admin** I can **delete a task comment** so that **I can delete a comment which has been incorrectly submitted**.|☑|
|Task Status Update Comment: As a **site user/site admin** I can **automatically add a comment to detail a change in an tasks status** so that **the comments have a log of any changes to the status of the task**.|☑|
|View Action List: As a **site user/site admin** I can **view the actions which are to be completed by me** so that **I am aware what actions I need to completed**.|☑|
|View Action Details: As a **site user/site admin** I can **view an actions details** so that **I am aware of the details of the action which I need to completed**.|☑|
|Add Action: As a **site user/site admin** I can **add an action** so that **I can record any issues identified so they can be addressed at a later date**.|☑|
|Add Action related to a Task: As a **site user/site admin** I can **raise an action if an issue was raise when completing a task** so that **I can record any issues identified when completing a task so they can be addressed at a later date**.|☑|
|Edit Action: As a **site user/site admin** I can **edit an action** so that **I am able to update an action if any of the requirements change**.|☑|
|Delete Action: As a **site user/site admin** I can **delete an action** so that **I can delete an action which has been incorrectly submitted**.|☑|
|View Action Comments: As a **site user/site admin** I can **view action comments** so that **I can read the log of detailed information recorded about an action**.|☑|
|Add Action Comment: As a **site user/site admin** I can **add a comment to an action** so that **I can log the progress of the completion of an action**.|☑|
|Edit Action Comment: As a **site user/site admin** I can **edit an action comment** so that **I can update an error made in a comment**.|☑|
|Delete Action Comment: As a **site user/site admin** I can **delete an action comment** so that **I can delete a comment which has been incorrectly submitted**.|☑|
|Action Status Update Comment: As a **site user/site admin** I can **automatically add a comment to detail a change in an actions status** so that **the comments have a log of any changes to the status of the action**.|☑|

## Validator Testing

<!-- - CSS: No errors were found when passing through the official W3C CSS validator.

![CSS W3C Validator](src/assets/README_images/css_validation.png)

- JSHint: The following issues were raised, and have been intentionally ignored as they are in relation later version of ES:

1. Unclosed regular expression.
2. 'async functions' is only available in ES8 (use 'esversion: 8').
3. 'Optional chaining' is only available in ES11 (use 'esversion: 11').
4. 'object spread property' is only available in ES9 (use 'esversion: 9').

- Lighthouse (Accessibility Audit): The page achieved a great accessibility rating.

![Lighthouse Accessibility Audit](src/assets/README_images/lighthouse.png) -->

## Unfixed Bugs

There were no unfixed bugs.

## Libraries and Programs Used

- Github: Store Repository
- Gitpod: IDE
- Heroku: Site Deployment
- Cloudinary: Serving static media files
- ElephantSQL: PostgreSQL database hosting
- Django/Django REST Framework: Backend database and API
- Google Chrome, Microsoft Edge, Mozilla Firefox, Safari: Site testing on alternative browsers
- Chrome Dev Tools: Debugging of the site
- Microsoft OneNote: Planning notes for the project
- Lucid Charts: Planning the site process with a flow diagram

# Deployment

This project was deployed on Heroku using Code Institute's Videos. After creating a GitHub repository, the steps taken to create the Heroku App were:

<!-- 1. Install React.js:
```
npx create-react-app . --use-npm
npm start
```
2. All packages were already installed in the CI React Template.
3. Git add, commit, and push changes to gitpod.
4. Create the project app on Heroku, and link the GitHub repository by navigating to the 'Deploy' tab.

### Connecting to the API:
1. Navigated to the Heroku app of the project DRF-API, and under the Settings tab, added the following configvars:
- Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
- Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io
2. Check that the trailing slash `\` at the end of both links has been removed, and save the configvar pairs.
3. Install the Axios package, and create supporting `axiosDefaults.js` as shown in [Moments Walkthrough](https://github.com/Code-Institute-Solutions/moments/blob/cf955d2f2e6f70f61c92d1f9de85558d8e49f3a8/src/api/axiosDefaults.js). -->

<!-- ### Deploy to Heroku:
1. In the `scripts` section of `package.json` in gitpod, added the following command:
```
"heroku-prebuild": "npm install -g serve",
```
2. Add Procfile to project root & populate with the following:
```
web: serve -s build
```
3. Repeat the steps of git add/commit/push.
4. Deploy the project via the deploy button on Heroku. -->

## Deploy to ElephantSQL:
<!-- (ElephantSQL)[https://www.elephantsql.com/] using the following [instructions](https://code-institute-students.github.io/deployment-docs/41-pp5-adv-fe/pp5-adv-fe-drf-01-create-a-database) -->

## Requirements

-asgiref==3.6.0
-cloudinary==1.32.0
-dj-database-url==0.5.0
-dj-rest-auth==2.1.9
-Django==3.2.18
-django-allauth==0.44.0
-django-cloudinary-storage==0.3.0
-django-cors-headers==3.14.0
-django-filter==22.1
-djangorestframework==3.14.0
-djangorestframework-simplejwt==5.2.2
-gunicorn==20.1.0
-oauthlib==3.2.2
-Pillow==9.4.0
-psycopg2==2.9.5
-PyJWT==2.6.0
-python3-openid==3.2.0
-pytz==2022.7.1
-requests-oauthlib==1.3.1
-sqlparse==0.4.3

# Credits

I have again enjoyed learning with the Code Institute and completing my fifth assignment. I would like to thank my mentor Martina for her support, the CI Student Support Team and the CI Slack Community. Finally a big thank you to my girlfriend for her help with testing and the review of this site.

## Content

**Resources Used:**

- Code Institutes Walkthrough Videos
- Django and Django Rest documentation
- W3C Schools and Stack Overflow for general enquiries relating to Django

[Back to Top](#table-of-contents)