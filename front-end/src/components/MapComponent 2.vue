<template>
  <div>
    <div id="map"></div>
  </div>


</template>


<script>
export default {
  name: 'MapComponent',
  mounted () {
    this.initMap()
  },
  methods: {
    initMap (){
      var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 8
      })
    }
  }
}
</script>

<style>
  #map {
    height: 100vh;
    width: 100%
  }
</style>
