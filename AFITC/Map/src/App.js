import React from "react";
import {GoogleMap, withScriptjs, withGoogleMap, Marker } from "react-google-maps";

import * as storeData from "./data/outfile.json";

/*
var test = Object.values(storeData.default);
var item;
let lat = [];
let lng = [];
let keys = [];

var test2 = Object.values(test[1]);

for(item in test){
  keys.push(item);
  lat.push(test[item]["lat"]);
  lng.push(test[item]["lng"]);
}

var mylatlng = {lat: lat[1], lng: lng[1]};

*/

function Map(){
  return(
    <GoogleMap 
      defaultZoom = {12} 
      defaultCenter={{ lat:32.376541, lng: -86.299660}} 
    >    
    });
    </GoogleMap>

  )
}



const WrappedMap = withScriptjs(withGoogleMap(Map));


export default function App(){
  return(
  <div style = {{width: "100vw", height: "100vh"}}>
    <WrappedMap 
      googleMapURL = {'https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key='}
      loadingElement = {<div style = {{height:"100%"}} />}
      containerElement = {<div style = {{height:"100%"}} />}
      mapElement = {<div style = {{height:"100%"}} />}
    />
   </div>
   ); 
}