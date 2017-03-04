var mymap = L.map('mapid').setView([35.505, -0.09], 2);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
  maxZoom: 18,
  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
    '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
    'Imagery © <a href="http://mapbox.com">Mapbox</a>',
  id: 'mapbox.streets'
}).addTo(mymap);


  var popup = L.popup();


  function onMapClick(e) {
    popup
      .setLatLng(e.latlng)
      .setContent("You placed your windfarm at " + e.latlng.toString().replace(/LatLng/i, ""))
      .openOn(mymap);
    $.ajax({url: "/score/" + e.latlng.toString().replace(/LatLng/i, ""), success: function(result){
      alert(result)
    }})
  }

mymap.on('click', onMapClick);


// $("mymap").click(function(){
//   alert("yay")
//     $.ajax({url: "demo_test.txt", success: function(result){
//         $("#div1").html(result);
//     }});
// });
