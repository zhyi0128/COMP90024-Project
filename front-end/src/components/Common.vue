<script>
  import {Loading} from 'element-ui'
  function loading(text, time, target) {
    const loading = Loading.service(
      {
        target: target,
        lock: true,
        text: text,
      });
    setTimeout(() => {
      loading.close();
    }, time);
  }

  export default {
    name: 'Common',
    loading
  }


</script>
