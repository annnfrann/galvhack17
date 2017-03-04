var mymap = L.map('mapid').setView([35.505, -0.09], 2);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
<<<<<<< HEAD
  maxZoom: 18,
=======
  maxZoom: 4,
  center: L.latLng(-100.89, 40.22),
  minZoom: 4,
  dragging: false,
>>>>>>> d4a5a8b854e78d36d28c8967c60ee48bd80497e4
  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
    '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
    'Imagery © <a href="http://mapbox.com">Mapbox</a>',
  id: 'mapbox.streets'
}).addTo(mymap);


  var popup = L.popup();


  function onMapClick(e) {
<<<<<<< HEAD
    popup
      .setLatLng(e.latlng)
      .setContent("You placed your windfarm at " + e.latlng.toString().replace(/LatLng/i, ""))
      .openOn(mymap);
    $.ajax({url: "/score/" + e.latlng.toString().replace(/LatLng/i, ""), success: function(result){
      alert(result)
=======
    $.ajax({url: "/score/" + e.latlng.toString().replace(/LatLng/i, ""), success: function(result){
     popup
      .setLatLng(e.latlng)
      .setContent("You placed your windfarm at " + e.latlng.toString().replace(/LatLng/i, "")
                 +"\nWindspeed at this location is: " + result["user_speed"])
      .openOn(mymap);     
      console.log(result);
     popup
      .setLatLng(e.latlng)
      .setContent("Best Location is: " + result["best_lat"] + ", " + result["best_lon"]
                 +"\nWindspeed at best location is: " + result["best_speed"])
      .openOn(mymap);
>>>>>>> d4a5a8b854e78d36d28c8967c60ee48bd80497e4
    }})
  }

mymap.on('click', onMapClick);


// $("mymap").click(function(){
//   alert("yay")
//     $.ajax({url: "demo_test.txt", success: function(result){
//         $("#div1").html(result);
//     }});
// });
