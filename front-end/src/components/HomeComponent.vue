<template>
  <div>
    <BarComponent class="bar"/>
    <div class="background"></div>
    <div class="center">
      <p style="text-align: center; color: white; font-size: 50px; font-family: -apple-system"></p>
      <p style="text-align: center">
        <el-button onclick="window.location.href='/map'" type="primary" style="font-size: 23px; font-weight: 500" round>
          Explore Now</el-button>
      </p>
      <!-- button class="btn btn-secondary btn-sm" data-toggle="modal" data-target="#detailInfoModal">open</button -->
    </div>




    <div class="modal fade" id="detailInfoModal" tabindex="-1" role="dialog"
         aria-labelledby="detailInfoModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            Fuck you
            <button class="close" style="font-size: 13px" data-dismiss="modal" aria-hidden="true">&times;</button>
          </div>
          <div class="modal-body">
            <div>
              <el-row>
                <el-select v-model="xAxis" placeholder="X Axis">
                  <el-option key="population" label="Population" value="population"/>
                  <el-option key="income" label="Income" value="income"/>
                </el-select>
                <el-cascader
                  :options="options" placeholder="Y Axis"
                  @change="renderScatterCharts"/>
              </el-row>
              <el-row style="height: 350px">
                <BarChart :data="test"/>
              </el-row>

            </div>

          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary btn-sm" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  import Common from './Common'
  import BarComponent from './BarComponent'
  import CascaderComponent from './CascaderComponent'
  import ScatterChart from './ScatterChartComponent'
  import BarChart from './BarChartComponent'

  export default{
    components: {BarChart, ScatterChart, BarComponent},
    data(){
      return {
        test: null,
        xAxis: null,
        options: CascaderComponent.data().options1
      }
    },
    methods:{
      renderScatterCharts(value){
        alert(value)
        Common.loading("Loading Data From Database...", 1000)
        let params = value.toString().split(',')
        this.test = [["au",'sdf','sd','qwew','zxc'], [10,23,24,15,8]]
        //this.getScatterData(this.value, params[0], params[1], params[2])
      },

    },
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
    background-position: center 0;
  }

  .center{
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%,-50%);
  }

</style>
