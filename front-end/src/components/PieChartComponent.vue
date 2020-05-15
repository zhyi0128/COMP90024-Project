<template>
  <div id="pie" ref="curPie" style="position:relative; height: 100%; width: 100%"></div>
</template>

<script>

  export default {
    name: 'PieChart',

    mounted () {
      this.initCharts()
      setTimeout(()=>{
        this.initCharts(this.data, this.title)
      }, 1000)
    },

    props: [
      'data',
      'title'
    ],
    watch: {
      data: function(data){
        setTimeout(()=>{
          this.initCharts(this.data, this.title)
        }, 1000)
      }
    },
    methods:{
      initCharts(data, title){
        this.pieChart = this.$echarts.init(this.$refs.curPie);
        let pieOption = {
          title: {
            text: this.title,
            textStyle: {
              fontSize: 12,
              fontWeight: 'normal',
            },
            left: 'center'
          },
          tooltip: {
            confine: true,
            textStyle: {
              fontSize: 11
            }
          },
          series: [{
            type: 'pie',
            radius: '80%',
            top: '20%',
            bottom: '5%',
            selectedMode: 'single',
            selectedOffset: 10,
            clockwise: true,
            data: data,
            label: {
              show: false
            }
          }]
        };
        this.pieChart.setOption(pieOption)
        window.addEventListener("resize", this.pieChart.resize);
        this.resize()
      },
      resize(){
        this.pieChart.resize()
      }
    }
  }

</script>
