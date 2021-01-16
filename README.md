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
the app, and the app should be tested with the command "flask run" in the implementation folder in CS50 IDE.

My hope is that this app would help equalize the resources that disadvantaged BCA applicants have compared to their wealthier peers and (ultimately) help make BCA
a more racially and socioeconomically diverse place. I plan to improve and publish this app during winter break after the semester is over.

YouTube URL: https://youtu.be/_GaJCzKVPA8

*list of for-profit companies
-TestPrepBCA (bcatestprep.com)
-Accel Learning (https://www.accellearning.com/test-prep/bca-test-prep-classes/)
-Masters Prep (https://www.mastersprep.org/bergen-county-academies-prep)
-MEK Review (https://mekreview.com/programs/bergen-county-academies-prep/)
-EMI Academy (http://www.emiacademy.com/emi-program/test-prep/)
-Gouda BCA (https://www.goudabca.com/bcaprepcourse)

**https://www.niche.com/k12/bergen-county-academies-hackensack-nj/

Acknowledgements not included in code: Steven DiSilvio, my friend and another BCA graduate (who now studies math and CS at Columbia), came up with this idea many
months ago, and I got his approval to implement a version of it for my CS50 final project. I used favicon.io (https://favicon.io/favicon-generator/) to make the
favicon.ico file. David Malan, Brian Yu, and Yoel Hawa for teaching me the skills to make this app, and CS50 Finance for being a starting point for many aspects.