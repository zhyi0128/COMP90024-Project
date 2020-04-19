<template>
  <div>
    <BarComponent/>
    <router-view/>
  </div>

</template>

<script>
  import BarComponent from './components/BarComponent'

  export default {
  name: 'App',
  components: {BarComponent}
}
</script>
