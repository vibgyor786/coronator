function updatemap() {
  fetch("https://www.trackcorona.live/api/countries")
    // fetch("https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")
    .then((response) => response.json())
    .then((rsp) => {
      console.log(rsp.data[0]);
      let test = rsp.data[0];
    //   new mapboxgl.Marker({
    //     draggable: false,
    //     color: "rgb(255,0,0)",
    //   })
    //     .setLngLat([test.longitude, test.latitude])
    //     .setPopup(
    //       new mapboxgl.Popup({ offset: 25 }) 
    //         .setHTML(
    //           "<h3>location: " +
    //             test.location +
    //             "</h3><p>Death " +
    //             test.dead +
    //             "</p>"
    //         )
    //     )
    //     .addTo(map);

      rsp.data.forEach((element) => {
    //    let color="rgb(233,0,0)";
        if (element.dead>1157){
            color="rgb(255,0,0)";
        }
       else{
           color="rgb(${element.dead},0,0)"
       }
        new mapboxgl.Marker({
            draggable: false,
            color:color,
          })
            .setLngLat([element.longitude, element.latitude])
            .setPopup(
              new mapboxgl.Popup({ offset: 25 }) 
                .setHTML(
                  "<h3>confirmed cases: " +
                    element.confirmed +
                    "</h3><p>Deaths " +
                    element.dead +
                    "</p>"
                )
            )
            .addTo(map);
      });
    });
}

// let interval=2000000;
// setInterval((updatemap,interval));
updatemap();
