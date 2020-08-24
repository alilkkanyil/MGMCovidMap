import React from "react";
import { GoogleMap } from "react-google-maps";

function Map(){
    return (<GoogleMap defaultZoom = {10} defaultCenter = {{ lat:32.376541, lng:-86.299660}}/>);
}