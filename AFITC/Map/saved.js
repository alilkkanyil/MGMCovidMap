import React from "react";
import {
  GoogleMap,
  withScriptjs,
  withGoogleMap,
  useLoadScript,
  Marker,
  InfoWindow,
} from "@react-google-maps/api";

import { formatRelative } from "date-fns";


import usePlacesAutoComplete, {
  getGeocode,
  getLatLng,
} from "use-places-autocomplete";
import {
  Combobox,
  ComboboxInput,
  ComboboxPopover,
  ComboboxList,
  ComboboxOption,
} from "@reach/combobox";
import "@reach/combobox/styles.css";

import mapStyles from "./mapStyles";

const libraries = ["places"]
const mapContainerStyle = {
  width:"100vw",
  height: "100vh",
};
const mapCenter = {
  lat: 32.376541,
  lng: -86.299660,
};
const options = {
  styles: mapStyles,
  disableDefaultUI: true,
};

export default function App(){
  const { isLoaded, loadError } = useLoadScript({
    googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
    libraries,
  });

  if (loadError) return "Error loading maps";
  if (!isLoaded) return "Loading Maps";

  return <div>
    <GoogleMap 
    mapContainerStyle = {mapContainerStyle} 
    zoom = {13} 
    center = {mapCenter}
    options = {options}
    ></GoogleMap>
  </div>
}
