# Fluent City Coding Challenge

### The Anagram Algorithm

This anagram algorithm works in 3 steps. First it confirms that the word exists.
If so, then it determines the length of the word, and pulls all other words of the same length from the db.
This is done so that comparisons are only done against words that are the same length-since other length words can't be anagrams.
After a list of all equal length words has been pulled, a single for loop is run (This keeps overall complexity at O(N)) wherein
the iterated word is broken into an array of its letters and sorted-this array is then compared against the array of the given word.
This comparison is predicated off the fact that anagrams are words that are the same length with the same letters.
Consequently, a sorted array of anagrams will be identical. Therefore once identical arrays are found,
they are added to the anagram list and returned once all equal length words are evaluated.

### The Backend:

**Within this directory there are three folders:**
  The **DockerNGINXFlask** folder contains the Dockerized version of this project
  wherein the app is orchestrated with Docker-Compose, runs on Flask, served with NGINX for
  proxying/load balancing/serving and connects to the Postgres DB. When composed,
  the app will be available http://localhost:8080/.

  The **DjangoHeroku** folder contains the Django implementation of the project
  which is currently deployed to Heroku and is accessible now at https://fluent-city-anagrams.herokuapp.com/

  While the **PandasAndLocal** is totally local, wherein I import the given dictionary
  into a pandas dataframe and run my algorithm against the df.

**The Aims/Goals:**
  This project aims to bring the supplied dictionary to life and to implement an
  efficient algorithm of anagram sorting. The goal was also to build a full-stack web
  app using open source technologies and to deploy into production/Dockerization.
  This was successfully accomplished. User interaction is designed to be minimalistic
  wherein a word is entered checked against the db and returned with all anagrams

**The Database**
  Postgres was employed because its scalable, open-source, works on Heroku/Docker,
  and is overall terrific! In both projects I opt to execute raw SQL over ORMs,
  I do so mainly because I like writing SQL and I find it easier to debug SQL
  statements then ORM models, just a personal preference and I'm far from dogmatic about it.

**Both projects employ a PostgresDB and use the same front-end so the only
variation is within the backend.**

**A Separate README for DjangoHeroku and DockerNGINXFlask implementations are found in their respective folders**

### The Frontend:

**SPA:**
  The frontend is built with React, which handles user input from the html,
  handles API calls, formats incoming data. As the app's complexity was pretty
  simple only one component is created, and redux and webpack were avoided since
  the requirements could be accomplished without them.
  Controller: /CodingSample/DockerNGINXFlask/static/assets/js/MainScript.js

**CSS3/HTML5:**
  I employed previously written CSS code to format the basic design of the app and
  to format for a variety of mobile scenarios. I additionally wrote new css for certain graphing aspects.
  CSS: /CodingSample/DockerNGINXFlask/static/assets/css/main.css
  Html: /CodingSample/DockerNGINXFlask/templates/Homepage.html

**Areas of Expansion/Continuance:**
  If work on this project were to continue, more words could be uploaded and
  other languages could be added. Additionally, other word based applications could be made
  and other features on the client could be added on-like links to wikitionary.
  Additionally Kubernetes could be employed to scale up the number of containers.

# Hope you enjoy!
