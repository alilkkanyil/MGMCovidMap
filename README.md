# MGMCovidMap
This project is a web app designed to allow Montgomery, AL government to communicate the availability of supplies during emergency times online. The web-app displays the availability of essential supplies for a crisis scenario, these supplies being food, water, toilet paper, hand sanitizer and paper towels. The web-app is being designed with the intention of caching its data to be accessed offline if necessary. Python scripts provided and the database schema provided is intended to work in conjunction to update these values periodically.

This project is intended to be a proof of concept and is being made for the innovate AFITC hackathon. 

# Dependencies

Note: Dependencies only necessary if you build the program yourself.

* Python 3.x
* Node.js
* NPM
* MongoDB
* React.js
* @react-google-maps
* combobox
* google-maps-infobox
* react-google-maps
* Mongodb

# Instructions

To run the program, you can unzip the "Map.rar" file to MGMCovidMap/AFITC/Map and cd into "build" directory. In the build directory, you can start the web app with "npm start".

Alternatively, you can use the "npm start" to start the development version or "npm run build" to build the deployment build. 

Mongodb is used to store the data for each store.  This data consists of availabilities of each item, store locations, etc.

It can be be quried via the availabilities.  The responses are then converted to a format that is applied to google maps.

Presentation video included above.
