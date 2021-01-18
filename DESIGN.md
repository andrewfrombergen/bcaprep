BCA Prep is a web app that has a navbar with essentially five links. BCA Prep is the brand link in the middle that, as customary, directs to the homepage. There
are two links to the left, "About" and "Tips on Applying," as well as two links to the right, "Entrance Test" and "Contact." There are six main HTML templates
that are used to load pages (other than apology, which is used for errors, and layout, which is a layout used for other HTML pages). The discrepancy (five links
versus six templates) is because the "Entrance Test" link has the effect of directing to different pages depending on whether the user is logged in. Because the
"/entrancetest" route is the only one that requires login, if you are not logged in and click "Entrance Test," you are sent to the login page. If you are logged
in, you can proceed to the page loaded with test.html where you can access information and resources on the English and math portions of the entrance test as well
as plan and track your study progress.

Registration is done on the homepage. Once registration goes through, the app takes the user to the login page, which is user-friendly because it allows newly
registered users to log in. Successful logins route to "/entrancetest" and load test.html because it is the only page that requires login and presents differently
based on the identity of the user. The database that keeps track of users through their username and the hash of their password is on Heroku Postgres. The
database also stores a text "entrancetest" for each user, which is initalized to be empty but serves as storage for the user's study plan as explained in the next
paragraph.

test.html is always loaded while passing in the user's username as well as the user's "entrancetest" value. The page starts with some instructions on how to use
the page and the text box used for planning; then it has a Bootstrap accordion with information and resources on the English and math tests. The page has a text
box accompanied by "Save" and "Log Out" buttons, and the text box always automatically loads the user's "entrancetest" value into the box as the page is loaded.
Because users can click the "Save" button to reload the page while updating their entrancetest value in the database, users' planning in the text box can transfer
between sessions. The "Log Out" button clears the session, and because test.html is not accessible when not logged in, the user will be taken to the login screen.
At the very bottom of test.html, it indicates the username of the user who is logged in and displays a warning to save before logging out.

The rest of the app requires less explanation. The "About," "Tips on Applying," and "Contact" links in the navbar direct to pages that do not vary based on user.
about.html has general information about the app and its purpose along with a fun embedded BCA video to make an otherwise text-filled page less boring for users.
tips.html, which "Tips on Applying" links to, uses a Bootstrap accordion to deliver tips and information on essays, teacher recommendations, and the interview as
well as frequently asked questions and their answers. contact.html has my photo and contact information.

Notes:<br>
-The app is secured with Heroku's Automated Certificate Management and Flask's flask-talisman package. A function of the latter is to redirect to and force HTTPS.<br>
-For enhanced security, passwords are required to be at least eight characters in length and contain at least one capital letter as well as one number.<br>
-If logged in, a user will not see the registration form displayed on the homepage but rather a message that indicates that user's username.<br>
-Immediately after a user successfully registers, s/he is directed to the login page that has additional text confirming that registration went through.<br>