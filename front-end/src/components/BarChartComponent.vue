<!--
Referenced & modified according to:
https://echarts.apache.org/examples/en/editor.html?c=bar-gradient
-->

<template>
  <div id="bar" ref="curBar" style="position:relative; height: 100%; width: 100%"></div>
</template>

<script>
  export default {
    name: 'BarChart',
    props: [
      'data',
      'xName',
      'yName',
      'title'
    ],
    watch: {
      data: function(data){
        this.initCharts(data, this.title)
      }
    },
    methods:{
      initCharts(data, title){
        const barChart = this.$echarts.init(this.$refs.curBar);
        const max = (title.indexOf('attention') > -1) ? 0.1 : 1
          let barOption = {
          title:{
            text: 'Australian States ' + title + ' analysis',
            textStyle: {
              fontSize: 13,
              fontWeight: '600',
            },
            left: 'center',
            top: '5%',
            bottom: '5%'
          },
          xAxis: {
            name: this.xName,
            nameLocation: 'center',
            nameGap: 20,
            data: data[0],
            axisLabel: {
              show: false,
            },
            axisTick: {
              show: false
            },
            axisLine: {
              show: false
            }
          },
          yAxis: {
            name: this.yName,
            axisLine: {
              show: false
            },
            axisTick: {
              show: false
            },
            max: max
          },
          tooltip:{
            show: true,
            confine: true,
            textStyle: {
              fontSize: 11
            }
          },
          series: [{
            type: 'bar',
            data: data[1],
            barCategoryGap: '50%',
            showBackground: true,
            backgroundStyle: {
              color: 'rgba(0, 0, 0, 0.06)'
            },
            itemStyle: {
              color: new this.$echarts.graphic.LinearGradient(
                0, 0, 0, 1,
                [{offset: 0, color: '#ff8566'},
                  {offset: 0.5, color: '#ff5c33'},
                  {offset: 1, color: '#ff3300'}
                ])
            },
            emphasis: {
              itemStyle: {
                color: new this.$echarts.graphic.LinearGradient(
                  0, 0, 0, 1,
                  [{offset: 0, color: '#ff3300'},
                    {offset: 0.5, color: '#ff5c33'},
                    {offset: 1, color: '#ff8566'}
                  ])
              }
            }
          }]
        }
        barChart.setOption(barOption)
      }
    }
  }

</script>
