<template>
  <div class="container">
    <div class="background"></div>
    <div class="center">
      <p style="text-align: center; color: white; font-size: 35px; font-family: -apple-system; font-weight: bold">
      COMP90024 Cluster & Cloud Computing Project</p>
      <p style="text-align: center"><button type="button" class="btn btn-light" style="font-weight: bold">Explore</button></p>
    </div>
  </div>

</template>

<style>
  .background{
    position:fixed;
    top: 0;
    left: 0;
    width:100%;
    height:100%;
    z-index:-10;
    background-image: url(../assets/background.png);
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;
    background-position: center 0;
  }
  .center{
    position: relative;
    margin-top: 25%;
  }

</style>
