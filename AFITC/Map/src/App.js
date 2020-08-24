import React, { useState } from "react";
import {
  GoogleMap, 
  withScriptjs, 
  withGoogleMap, 
  Marker,
  InfoWindow
 } from "react-google-maps";

import * as storeData from "./data/outfile.json";
import mapStyles from "./mapStyles";
function Map(){
  const [selectedStore, setSelectedStore] = useState(null);


  return(
    <GoogleMap 
      defaultZoom = {12} 
      defaultCenter={{ lat:32.376541, lng: -86.299660}} 
      defaultOptions = {{styles : mapStyles}}
    >    
     {storeData.features.map((store) => (
       <Marker 
        key={store.properties.STORE_ID} 
        position ={{
          lat: store.properties.lat,
          lng: store.properties.lng
        }}
        onClick = {() => {
          setSelectedStore(store);
        }}
        icon = {{
          url: '/store.png',
          scaledSize: new window.google.maps.Size(25, 25)
        }}
       />

     ))}
      {selectedStore && (
        <InfoWindow
          position ={{
            lat: selectedStore.properties.lat,
            lng: selectedStore.properties.lng
          }}
          onCloseClick = {() => {
            setSelectedStore(null);
          }}
        >
          <div>
            <h2>{selectedStore.properties.BRAND}</h2>
            <h2>Address: {selectedStore.properties.ADDRESS}</h2>
            <p>Canned Food: {selectedStore.properties.cannedFood}</p>
            <p>Toilet Paper: {selectedStore.properties.toiletPaper}</p>
            <p>Paper Towels: {selectedStore.properties.paperTowels}</p>
            <p>Sanitizer: {selectedStore.properties.sanitizer}</p>
          </div>
        </InfoWindow>
      )}
    </GoogleMap>

  )
}

const WrappedMap = withScriptjs(withGoogleMap(Map));


export default function App(){
  return(
  <div style = {{width: "100vw", height: "100vh"}}>
    <WrappedMap 
      googleMapURL = {'https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyBXQY3TfYUy08e5FSch7nz21vJpMYqxBnQ'}
      loadingElement = {<div style = {{height:"100%"}} />}
      containerElement = {<div style = {{height:"100%"}} />}
      mapElement = {<div style = {{height:"100%"}} />}
    />
   </div>
   ); 
}