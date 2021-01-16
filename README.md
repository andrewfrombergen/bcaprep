The public magnet high school I went to, Bergen County Academies, has a crazy admissions process with a 15% acceptance rate that mirrors the college admissions
process: essays, transcripts, recommendations, interviews, and more. For-profit companies* offering expensive preparation courses have stepped in to prepare
students that can afford it, but a fair shot is out of reach for lower-income students. This might help explain why BCA's student body is disproportionately
white and Asian (38% white, 51% Asian) as well as wealthy (only 5% free or reduced lunch).**

My CS50 final project, BCA Prep, is a web app that serves as a free and comprehensive resource for all students applying to BCA. It has resources to prepare for
the English and math portions of the entrance test. For each section of the test, there is advice and a list of resources that I recommend for preparation, and
there is login functionality which allows applicants to plan and track their progress with a study plan that saves between sessions. There is another page "Tips
for Applying" that contains my tips for the other parts of the application: essays, teacher recommendations, and the interview. The page also contains frequently
asked questions and answers to those questions, as well as directions for contacting me if there are questions that are not yet covered. There is also an "About"
page that describes the website along with a fun embedded BCA video as well as a "Contact" page with my contact information.

The app was built with a Flask framework incorporating Python, SQL, and HTML/CSS/JavaScript. The files for the app are contained in an "implementation" folder,
which itself contains two folders (static, templates) and six files (application.py, bcaprep.db, DESIGN.md, helpers.py, README.md, requirements.txt). The folder
static contains three files: favicon.ico, photo.jpg, styles.css. The folder templates contains eight files: about.html, apology.html, contact.html, index.html,
layout.html, login.html, test.html, tips.html. All files other than the DESIGN.md and README.md documentation files are necessary for the proper functioning of
the app.

My hope is that this app would help equalize the resources that disadvantaged BCA applicants have compared to their wealthier peers and (ultimately) help make BCA
a more racially and socioeconomically diverse place.

*list of for-profit companies<br>
-Accel Learning (https://www.accellearning.com/test-prep/bca-test-prep-classes/)<br>
-Masters Prep (https://www.mastersprep.org/bergen-county-academies-prep)<br>
-MEK Review (https://mekreview.com/programs/bergen-county-academies-prep/)<br>
-EMI Academy (http://www.emiacademy.com/emi-program/test-prep/)<br>
-Gouda BCA (https://www.goudabca.com/bcaprepcourse)

**https://www.niche.com/k12/bergen-county-academies-hackensack-nj/

Acknowledgements: Steven DiSilvio, my friend and fellow BCA graduate, gave me the idea for this project. I credit CS50 instructors David Malan, Brian Yu, and Yoel
Hawa for teaching me the skills to make this app, Helen Cho for being a very supportive friend in the publication process, and the finance problem set for being a
starting point in many aspects. I used favicon.io (https://favicon.io/favicon-generator/) to make the favicon.ico file.