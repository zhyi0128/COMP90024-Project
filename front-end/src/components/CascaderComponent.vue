<script>
  export default {
    name: 'CascaderComponent',
    data() {
      return {
        options1: [{
          value: 'states',
          label: 'States',
          children: [{
            value: 'cn',
            label: 'China Related',
            children: [{ value: 'sentiment', label: 'Sentiment'}, { value: 'attention', label: 'Attention'}]
          }, {
            value: 'virus',
            label: 'COVID-19',
            children: [{ value: 'sentiment', label: 'Sentiment'}, { value: 'attention', label: 'Attention'}]
          },{
            value: 'happiness',
            label: 'Happiness',
            children: [{ value: 'sentiment', label: 'Sentiment'}]
          }]
        }, {
          value: 'mel',
          label: 'Melbourne',
          children: [{
            value: 'happiness',
            label: 'Happiness',
            children: [{ value: 'sentiment', label: 'Sentiment'}]
          }]
        }],

        options2: [{
          value: 'cn',
          label: 'China Related',
          children: [{ value: 'sentiment', label: 'Sentiment'}, { value: 'attention', label: 'Attention'}]
        }, {
          value: 'virus',
          label: 'COVID-19',
          children: [{ value: 'sentiment', label: 'Sentiment'}, { value: 'attention', label: 'Attention'}]
        },{
          value: 'happiness',
          label: 'Happiness',
          children: [{ value: 'sentiment', label: 'Sentiment'}]
        }]
      };
    }
  };
</script>
