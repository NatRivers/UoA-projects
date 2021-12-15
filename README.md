# University of Auckland projects

### Throughout my studies in University of Auckland since 2019 until now that im currently in 3rd year of my degree in Computer Science, I have made several interesting project assignments that I would like to share:


**YEAR 1 PROJECTS**
* ConnectFourGame *<Python>* (CS130 - Introduction to Software Fundamentals)  
We created a game of Connect Four where we played with the computer bot as our opponent. It's a normal Connect Four game but this time, we are playing in a console style format instead of graphics. We are using "X" and "O", where user is "O" and computer is "X". Our initial given color was suppose to be console default color, however for user to be able to easily identify which nodes are theirs, I allow user to choose their own colors, in order to differentiate the color to the computer's I use different color which is in contrast of user's color. I also added a "need help?" if user got stuck on where to put, the program will try to give a guide where user can achieve a score and I also added a bit of creativity in this "need help with the "Time" system. I tried to make the program as realistic as possible to how a board game in computers usually works so I added other features to the original template. Further details regarding the program can be found in  the description file located in  the ConnectFourGame directory.


**YEAR 2 PROJECTS**
* BounceAppBasic *<Java>* (CS230 - Object Oriented Software Development)  
In this project, we created a DVD loading style bouncing program using Eclipse. First we implemented the "screen" for the shapes to bounce around within that screen border in the AnimationPanel.java before constructing the shapes: Rectangle, Square, Ellipse, Pyramid and OverlappedSquare which extends the MovingShape class. After constructing the shapes, we also added an extra "movement" which is the fall movement, where once the shape reaches the very bottom of the screen, it will go back up and starts falling in a loop. It's a really simple bouncing program, a more advanced bounce program is in [BounceApp](https://github.com/NatRivers/assignment/tree/main/bounceApp) project.
* BounceApp *<Java>* (CS230 - Object Oriented Software Development)  
This bounce program has more advanced implementations in constructing different shapes(not just simple shapes Rectangle, Square, Ellipse, Pyramid and OverlappedSquare), note that BounceAppBasic and BounceApp is not related to each other however some implementations such as the AnimationViewer is similar. In this project, we added GraphicsPainter, Painter, FormHandler, Viewer, Listener and Adapters to support the shapes drawn into the "screen". The shapes that we used here are Rectangle, Oval, DynamicRectangle, ImageRectangleShape and NestingShape. Rectangle and Oval shape works similarly like BounceAppBasic's shapes, DynamicRectangle and ImageRectangleShape move like Rectangle shape but DynamicRectangle changes color everytime it hits an edge and ImageRectangleShape is a rectangle which contains an image in it, Lastly NestingShape as what it is called as "nesting" it has multiple shapes bouncing around the parent, the child shapes uses the parent shape as its screen instead of the main screen. FormHandler, Viewer, Listener and Adapters files are used for implementing the image of the ImageRectangle and the NestedShapes shapes such as inserting a chosen image into the ImageRectangle, listing the children of the NestedShape and the children's children as well.
* Movie Making Web *<Python, HTML, CSS>* (CS235 - Software Development Methodologies)  
The biggest project I did in year 2 is the movie making website, where we did an end-to-end testing (not fully functional) in PyCharm. We used different resources to do this assignment such as Flask blueprints, Jinja templating, WTForms, etc. Just like a typical movie website, we are supposed to display the movie titles as a "recommendation" in the homepage. We are not given any images to implement the 1000 movies so we can only display its title. We can browse movies according to genre and actors where I used the hover style where the drop down list will appear upon the cursor above it. Users are also allowed to log in and sign up into the website. Furthermore, logged in users will be able to post comments and add movies to their watchlist where these buttons will appear once the user are logged in, those who are not can only view comments and will not have an option to add to watchlist, the watchlist button will not be there to select from too. Since we only use cookies instead and did not use any database, so log in and sign up records will be lost once the program was restarted, so as the comments made by the users previously. (side note: We were suppose to implement the assignment with database in the upcoming assignments, however due to covid we were forced to extend the previous assignment and this assignment was done in a rush, and we can not proceed with the other remaining assignments.)

**YEAR 3 PROJECTS**
* Concert Booking Web *<Java, Javascript, HTML, CSS>* (CS331 - Large-Scale Software Development)  
This project is a group project where we team up in a group of 3 and we each contributed our work to the final project. We only have to implement the domainmodel and mapper classes in concert-service and also the files in concert-common directory. I implemented some of the ConcertResource, dto, domainmodel and mapper files. Our task distribution was further stated in the directory's organisation.md file.
* Book Program Discussion *<JavaScript, HTML, CSS>* (CS345 - Human-computer Interaction)  
A simple high level prototype was the task given to us where we should design our own template only for the homepage section and also the sign up section. I used a similar template to the [Movie Making Web](https://github.com/NatRivers/UoA-projects/tree/main/MovieMakingWeb). This project aims to follow as much of the principles of having a good user experience (UX) design such as common fate, proximity, similarity, etc. We are assigned with a color and should be able to create a good design out of our respected color.
  
  
### There will be more upcoming projects in my remaining year of my studies in University of Auckland which will be uploaded once the project is complete.
