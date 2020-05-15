<!--
  The linear regression section of the scatter chart is referenced according to an example provide by the e-charts
  official website. See https://echarts.apache.org/examples/en/editor.html?c=scatter-linear-regression
-->

<template>
  <div id="scatter" ref="curScatter" style="position:relative; height: 100%; width: 100%"></div>
</template>


<script>
  import ecStat from 'echarts-stat'
  export default {
    name: 'ScatterChart',
    props: [
      'data',
      'xName',
      'yName'
    ],
    watch: {
      data: function(data){
        this.initCharts(data)
      }
    },
    methods:{
      initCharts(data){
        const scatterChart = this.$echarts.init(this.$refs.curScatter)
        const myRegression = ecStat.regression('linear', data)
        myRegression.points.sort(function(a, b) {
          return a[0] - b[0];
        });
        let scatterOption = {
          title:{
            text: 'Linear regression',
            textStyle: {
              fontSize: 13,
              fontWeight: '600',
            },
            left: 'center',
            top: '5%',
            bottom: '5%'
          },
          xAxis: {
            type: 'value',
            name: this.xName,
            nameLocation: 'center',
            nameGap: 25,
            min: 'dataMin',
            splitLine: {
              lineStyle: {
                type: 'dashed'
              },
            },
          },
          yAxis: {
            type: 'value',
            name: this.yName,
            min: 'dataMin',
            splitLine: {
              lineStyle: {
                type: 'dashed'
              },
            },
          },
          tooltip: {
            trigger: 'axis',
            confine: true,
            axisPointer: {
              type: 'cross'
            },
            textStyle: {
              fontSize: 11
            }
          },
          series: [{
            name: 'True value',
            type: 'scatter',
            symbol: 'pin',
            symbolSize: 6,
            data: data,
            label:{
              show: false
            },
            itemStyle: {
              color: '#ff3300'
            },
          },{
            name: 'line',
            type: 'line',
            showSymbol: false,
            data: myRegression.points,

            lineStyle: {
              color: '#007bff',
              width: 1,
            },
            markPoint: {
              itemStyle: {
                color: 'transparent'
              },
              label: {
                show: true,
                position: 'left',
                formatter: myRegression.expression,
                color: '#1d2124',
                fontSize: 12
              },
              data: [{
                coord: myRegression.points[myRegression.points.length - 1]
              }]
            }
          }]
        };
        scatterChart.setOption(scatterOption)
      },
    }
  }

</script>
