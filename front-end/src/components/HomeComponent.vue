<template>
  <div>
    <BarComponent class="bar"/>
    <div class="background"></div>
    <div class="center">
      <p style="text-align: center">
        <el-button onclick="window.location.href='/map'" type="primary" style="font-size: 22px; font-weight: 500" round>
          Explore Now</el-button>
      </p>
    </div>
  </div>

</template>

<script>
  import BarComponent from './BarComponent'

  export default {
    components: {BarComponent},
  }

</script>


<style>
  .background{
    position:fixed;
    top: 0;
    left: 0;
    width:100%;
    height:100%;
    z-index:-10;
    background-image: url(../assets/background.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;
    background-position: center;
  }

  .center{
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%,-50%);
  }

</style>
