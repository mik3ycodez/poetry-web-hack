## The Idea
Poetr (poet - er) is a space for the exploration and creation of poetry along a so called "non-euclidian poem highway." Readers are presented with a poem that may seem random... or perhaps it's a step on their unique path through the collection. They may continue their journey via one of two buttons: one to dive deeper down the path they're on, and one to shift to a new perspective. If the inspiration strikes them, a reader may submit their own piece, saved in its unique spot in the collection yet tied to poems with a similar vibe. 

## How We Made It
Poetr is built on the Django python framework with a mysql database and hosted on Google's App Engine cloud platform. The Poetr team divided and conquered with the team splitting in half to work independently on both the back and front ends at the same time. This was possible because the Django backend and the HTML/CSS frontend are minimally connected allowing for rapid iterations and prototyping on both ends. Google App Engine proved to be the perfect hosting solution because of its robust support for Django and mysql

**Team Testimonials**

Alice: Django has copious amounts of documentation but much of it assumes you already know how to use Django. There was a real shortage of low level tutorials or resources to help us get off the ground. But once Jett and I got past the initial confusion it proved to be a very powerful and effective tool.

Jett: I worked on the back-end with Alice. Together, we wrote the python code that manages and presents our data. I also worked a bit with the front end team; I created our logo graphic in Adobe Illustrator and revised it with feedback from Nicolas and Mike.

Mike: Contributing to the front end of our project has really helped me hone my responsive layout and best practice skills. Designing quickly while maintaining proper HTML and CSS standards was fun and ensured the project developed smoothly. Working with Nicolas on front end also helped us collaborate together and help each other through the process.

Nicolas: I had a great time working with the Poetr team. I collaborated primarily on the front-end with Mike; for me, this was an opportunity to move past creating static HTML files and onto coding dynamically-generated webpages, powered by Django and Google Cloud. Alice and Jett did a great job on the back-end and throughout the creative process, both front-end and back-end communicated superbly, often getting together to brainstorm ideas, updating each other on progress, and helping the other debug. We hope you enjoy Poetr.


## Challenges We Braved
**Back End:**
- We were working with a completely foreign tech stack
- No previous Django knowledge and it has a learning curve to say the least
- No one had used Google App Engine before either and it can be confusing to interact with
- Google App Engine at one point refused to update the files

**Front End:**
- Understanding and interacting with the dynamic content Django creates
- utilizing a responsive design

**Team Testimonials**

Alice: The backend team spent a good three hours just trying to wrap our heads around how Django is supposed to work and then how it actually works. I also personally fought with App Engine repeatedly while trying to get it to update to newer versions of the code, but in the end I got it all sorted out.

Jett: Learning the syntax and structure of Django was the largest challenge I faced, but now that I'm familiar with it I'm excited to add a powerful tool to my belt. Thankfully I had Alice to dig through the docs with :).

Mike: Personally, I found it a challenge to incorporate a responsive design and making sure the layouts adapted to the most used browsers and devices in a 24 hour period. Another point I wasn't quite sure how to do was connecting the front end to the back. With Alice's and Jett's help, we were able to figure out the Django syntax. 

Nicolas: For me, the most interesting - and therefore, challenging - component of the front-end development was that we were loading both Bootstrap CSS - which already came loaded with certain conventions - and a local static CSS file. Thus figuring out the best practices for styling, like Mike touched on, was crucial to ensuring cross-browser compatibility. No one had used Django prior, so I very much appreciated the team’s initiative early on in exploring how to connect the front and back end. I was able to run Django outside a runtime environment wrapper to test changes to the front-end, and now I never want to go back to local testing.

## Accomplishments We Are Proud Of
We are proud of developing a Django based web application that provides a space for the exploration of poetry. We worked together as a team to brainstorm new ideas, implement new features, and solve problems at every level.

**Team Testimonials**

Alice: The front end team did an incredible job putting together a polished website in such a tight time window. I'm ecstatic with how well the project turned out, it really surpassed my wildest hopes and expectations

Jett: I'm proud of how polished our project is and how well my teammates worked together. As computer science students, it's trivial to write a program that displays a random poem. The Poetr team went above and beyond to developed a clean, fully functional user interface for our poetry landscape, and we had fun and taught each other new things while doing it.

Mike: I am really proud that our team was able to accomplish a fairly beautiful project in a short amount of time. With a first time experience at a hackathon, it was great to see how efficiently our group formed and collaborated. Really proud of the work that we did overall. 

Nicolas: Is it overkill to say that, I too, am very proud of our team? We each met and joined ranks the night before the hackathon began, came up with an idea the morning of, and kept an open line of communication and feedback throughout, despite the three-hour difference for the front-end and back-end. Thank you, Alice, Jett, and Mike, for making my first hackathon ever such a great experience.

## What's next for Poetr
We would like to see our collection of poems grow and for users to continue exploring poetry through our website. There's always room for improvement on our current features, as well as the possibility of new ones.

**Future Features**
- Proper dark/light mode
- Rating system, up/down voting
- User profiles to save posts and follow others
- Poem connections based on something more robust then one genre tag
