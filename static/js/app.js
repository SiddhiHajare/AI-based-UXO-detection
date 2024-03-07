import React, { useEffect, useState } from 'react';
import Webcam from 'webcam-easy'; // Assuming you have the webcam-easy library installed
import L from 'leaflet';

import 'leaflet/dist/leaflet.css';

const App = () => {
  const [position, setPosition] = useState({ lat: 14.0860746, long: 100.608406, accuracy: 0 });

  useEffect(() => {
    const map = L.map('map').setView([position.lat, position.long], 6);

    const osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    osm.addTo(map);

    if (!navigator.geolocation) {
      console.log("Your browser doesn't support geolocation feature!");
    } else {
      updatePosition();
      // Update position every 10000 milliseconds (10 seconds)
      setInterval(updatePosition, 10000);
    }

    let marker, circle;

    function updatePosition() {
      navigator.geolocation.getCurrentPosition(getPosition);
    }

    function getPosition(position) {
      const lat = position.coords.latitude;
      const long = position.coords.longitude;
      const accuracy = position.coords.accuracy;

      if (marker) {
        map.removeLayer(marker);
      }

      if (circle) {
        map.removeLayer(circle);
      }

      marker = L.marker([lat, long]);
      circle = L.circle([lat, long], { radius: accuracy });

      const featureGroup = L.featureGroup([marker, circle]).addTo(map);

      map.fitBounds(featureGroup.getBounds());

      console.log(`Your coordinate is: Lat: ${lat} Long: ${long} Accuracy: ${accuracy}`);

      setPosition({ lat, long, accuracy });
    }
  }, []); // empty dependency array to run useEffect only once

  return (
    <div>
      {/* Navbar */}
      {/* Your existing Navbar code */}
      
      {/* Map and Webcam */}
      <div id="parent-container">
        <div id="map"></div>

        <video id="Webcam" autoPlay playsInline width="800" height="600"></video>
        <canvas id="canvas"></canvas>
      </div>

      {/* Table */}
      <table id="table">
        <thead>
          <tr>
            <th>Latitude</th>
            <th>Longitude</th>
            <th>Accuracy</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{position.lat}</td>
            <td>{position.long}</td>
            <td>{position.accuracy}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default App;
