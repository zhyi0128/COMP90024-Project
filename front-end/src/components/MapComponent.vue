<template>
  <div>
    <div id="map"></div>
    <BarComponent class="bar"/>
    <div id="clickables">
      <div id="topicButtons" style="position: absolute; left: 20px;">

        <button class="btn btn-dark dropdown-toggle" id="topicDropdown" type="button" data-toggle="dropdown"
                aria-haspopup="true" aria-expanded="false">Topics
        </button>
        <div class="dropdown-menu" aria-labelledby="topicDropdown">
          <a class="dropdown-item" @click="changeTopic('cn')">China Related
            <a v-if="curTopic==='cn'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
          <a class="dropdown-item" @click="changeTopic('virus')">COVID-19
            <a v-if="curTopic==='virus'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
          <a class="dropdown-item" @click="changeTopic('happiness')">Happiness
            <a v-if="curTopic==='happiness'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
        </div>

        <button v-if="curTopic != null" class="btn btn-dark dropdown-toggle" id="areaDropdown" type="button"
                data-toggle="dropdown" data-target="#areaMenu" aria-haspopup="true" aria-expanded="false">Areas
        </button>

        <button class="btn btn-dark" id="analysisButton" type="button"
                data-toggle="modal" data-target="#analysisInfoModal">Analysis</button>

        <div id="areaMenu">
          <div class="dropdown-menu" aria-labelledby="areaDropdown">
            <a class="dropdown-item" @click="switchTo('states')">States
              <a v-if="curArea==='states'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
            <a class="dropdown-item" v-if="curTopic==='happiness'" @click="switchTo('mel')">Melbourne
              <a v-if="curArea==='mel'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
          </div>
        </div>
      </div>

      <div id="labelButton" class="btn-group dropleft" style="position: absolute; right: 20px">
        <button class="btn btn-dark dropdown-toggle" id="labelDropdown" type="button"
                data-toggle="dropdown" data-target="#labelMenu" aria-haspopup="true" aria-expanded="false">Labels
        </button>
        <div id="labelMenu">
          <div class="dropdown-menu" aria-labelledby="labelDropdown">
            <a class="separator">--Tweets--</a>
            <a class="dropdown-item" style="font-size: 15px;" @click="curLabel='sentiment', switchTo(curArea)">Sentiment
              <a v-if="curLabel==='sentiment'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
            <a class="dropdown-item" style="font-size: 15px;" @click="curLabel='attention', switchTo(curArea)">Attention
              <a v-if="curLabel==='attention'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
            <a class="separator">--Population--</a>
            <a class="dropdown-item" style="font-size: 15px;" @click="curLabel='size', switchTo(curArea)">Size
              <a v-if="curLabel==='size'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
            <a class="dropdown-item" style="font-size: 15px;" @click="curLabel='age', switchTo(curArea)">Age
              <a v-if="curLabel==='age'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
            <a class="separator">--Income--</a>
            <a class="dropdown-item" style="font-size: 15px;" @click="curLabel='income', switchTo(curArea)">Income
              <a v-if="curLabel==='income'" style="color: #007bff; font-weight: 900;"> &checkmark;</a></a>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="detailInfoModal" tabindex="-1" role="dialog"
               aria-labelledby="detailInfoModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <p style="font-size: 13px" class="modal-title">
              <a v-if="curModal==='tweets'">Tweets Info</a>
              <a v-else href="#" @click="changeTag('tweets')">Tweets Info</a> |
              <a v-if="curModal==='population'">Population</a>
              <a v-else href="#" @click="changeTag('population')">Population</a> |
              <a v-if="curModal==='income'">Income</a>
              <a v-else href="#" @click="changeTag('income')">Income</a></p>
            <button class="close" style="font-size: 13px" data-dismiss="modal" aria-hidden="true">&times;</button>
          </div>
          <div id="detailModalBody" class="modal-body">
            <div v-if="curModal==='tweets'">
              <el-row v-if="showPieData.showTweetsData != null">
                <el-col class="centerCol" :span="12">
                  <div class="pieChart"><PieChart :data="showPieData.showTweetsData"
                                                  title="Sentiment Proportion"/></div>
                </el-col>
                <el-col class="centerCol" :span="12">
                  <div style="font-size: 12px; line-height: 22px">
                    <div>Sentiment Score: {{tweetsData[curTopic][curArea][curLocation].abstract.sentimentScore}}</div>
                    <div>Sentiment Level: Level {{tweetsData[curTopic][curArea][curLocation].abstract.sentimentLevel}}</div><br>
                    <div>Total Topic-related Tweets: {{tweetsData[curTopic][curArea][curLocation].abstract.relatedTotal}}</div>
                    <div>Total Tweets: {{tweetsData[curTopic][curArea][curLocation].abstract.total}}</div>
                    <div>Attention Score: {{tweetsData[curTopic][curArea][curLocation].abstract.attentionScore}}</div>
                    <div>Attention Level: {{tweetsData[curTopic][curArea][curLocation].abstract.attentionLevel}}</div>
                  </div>
                </el-col>
              </el-row>
              <div style="text-align: center; line-height: 30px" v-else>
                <div style="font-weight: bold">NO DATA</div>
                <div style="font-size: 12px">Please refer to its neighbours</div>
              </div>
            </div>
            <div v-if="curModal==='population'">
              <el-row v-if="showPieData.showGenderProportion != null">
                <el-col class="centerCol" :span="12" >
                  <div class="pieChart"><PieChart :data="showPieData.showGenderProportion"
                                                  title="Gender Proportion"/></div>
                </el-col>
                <el-col class="centerCol" :span="12">
                  <div class="pieChart"><PieChart :data="showPieData.showAgeProportion"
                                                  title="Age Proportion"/></div>
                </el-col>
              </el-row>
              <el-row v-if="showPieData.showGenderProportion != null">
                <el-col class="centerCol" :span="12">
                  <div style="font-size: 12px; line-height: 22px">
                    <div>Male Total: {{populationData[curArea][curLocation].maleTotal}}</div>
                    <div>Female Total: {{populationData[curArea][curLocation].femaleTotal}}</div>
                    <div>Total: {{populationData[curArea][curLocation].total}}</div>
                    <div>Population Size Level: Level {{populationData[curArea][curLocation].sizeLevel}}</div>
                  </div>
                </el-col>
                <el-col class="centerCol" :span="12">
                  <div style="font-size: 12px; line-height: 22px">
                    <div>Median Age: {{populationData[curArea][curLocation].medianAge}}</div>
                    <div>Population Age Level: Level {{populationData[curArea][curLocation].ageLevel}}</div>
                  </div>
                </el-col>
              </el-row>
              <div style="text-align: center; line-height: 30px" v-else>
                <div style="font-weight: bold">NO DATA</div>
                <div style="font-size: 12px">Please refer to its neighbours</div>
              </div>
            </div>
            <div v-if="curModal==='income'">
              <el-row v-if="showPieData.showIncomeProportion != null">
                <el-col class="centerCol" :span="12">
                  <div class="pieChart"><PieChart :data="showPieData.showIncomeProportion"
                                                  title="Income Proportion" /></div>
                </el-col>
                <el-col class="centerCol" :span="12">
                  <div class="pieChart"><PieChart :data="showPieData.showSourceProportion"
                                                  title="Source Proportion"/></div>
                </el-col>
              </el-row>
              <el-row v-if="showPieData.showIncomeProportion != null" type="flex" justify="center">
                  <div style="font-size: 12px; line-height: 22px">
                    <div>Mean total income: {{incomeData[curArea][curLocation].mean}}</div>
                    <div>Median total income: {{incomeData[curArea][curLocation].median}}</div>
                    <div>Income Level: Level {{incomeData[curArea][curLocation].incomeLevel}}</div></div>
              </el-row>
              <div style="text-align: center; line-height: 30px" v-else>
                <div style="font-weight: bold">NO DATA</div>
                <div style="font-size: 12px">Please refer to its neighbours</div>
              </div>
            </div>

          </div>
            <div class="modal-footer">
              <button class="btn btn-secondary btn-sm" data-dismiss="modal">Close</button>
            </div>
          </div>
      </div>
    </div>


    <div class="modal fade" id="analysisInfoModal" tabindex="-1" role="dialog"
         aria-labelledby="analysisInfoModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <p style="font-size: 14px;" class="modal-title">
              <a v-if="curAnalysis==='descriptive'">Descriptive Statistics</a>
              <a v-else href="#" @click="curAnalysis='descriptive', analyzer.barChart.cascaderValue=null">
                Descriptive Statistics</a> |
              <a v-if="curAnalysis==='regression'">Regression</a>
              <a v-else href="#" @click="curAnalysis='regression', analyzer.scatterChart.cascaderValue=null, analyzer.scatterChart.xAxis=null">
                Regression</a></p>
            <button class="close" style="font-size: 13px" data-dismiss="modal" aria-hidden="true">&times;</button>
          </div>
          <div id="analysisModalBody" class="modal-body">
            <div v-if="curAnalysis==='descriptive'">
              <el-select v-model="analyzer.barChart.xAxis" placeholder="States" disabled/>
              <el-cascader v-model="analyzer.barChart.cascaderValue" :options="analyzer.barChart.cascaderList"
                           placeholder="Y Axis" @change="renderBarCharts"/>
              <el-row style="height: 350px">
                <BarChart :data="analyzer.barChart.data" :title="analyzer.barChart.title"
                              :xName="analyzer.barChart.axis.xName" :yName="analyzer.barChart.axis.yName"/>
              </el-row>
            </div>

            <div v-if="curAnalysis==='regression'">
              <el-select v-model="analyzer.scatterChart.xAxis" placeholder="X Axis" @change="analyzer.scatterChart.cascaderValue = null">
                <el-option label="Population-Size" value="population-size"/>
                <el-option label="Population-Age" value="population-age"/>
                <el-option label="Income" value="income"/>
              </el-select>
              <el-cascader v-model="analyzer.scatterChart.cascaderValue" :options="analyzer.scatterChart.cascaderList"
                           placeholder="Y Axis" @change="renderScatterCharts"/>
              <el-row style="height: 350px">
                <ScatterChart :data="analyzer.scatterChart.data"
                              :xName="analyzer.scatterChart.axis.xName" :yName="analyzer.scatterChart.axis.yName" />
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
  import { create, all } from 'mathjs'
  import Common from './Common'
  import { Notification } from 'element-ui';
  import { Message } from 'element-ui';
  import BarComponent from './BarComponent'
  import PieChart from './PieChartComponent'
  import CascaderComponent from './CascaderComponent'
  import ScatterChart from './ScatterChartComponent'
  import BarChart from './BarChartComponent'
  import populationJsonAU from '../../static/population_au.json'
  import populationJsonMEL from '../../static/population_mel.json'
  import incomeJsonAU from '../../static/income_au.json'
  import incomeJsonMEL from '../../static/income_mel.json'
  import neighborJsonMEL from '../../static/suburb_neighbors.json'
  import $ from 'jquery'

  export default {

    name: 'MapComponent',
    components:{
      PieChart,
      BarComponent,
      BarChart,
      ScatterChart,
      CascaderComponent
    },
    data(){
      return{
        curTopic: null,
        curArea: null,
        curLocation: null,
        curLabel: 'size',
        curModal: null,
        curAnalysis: 'descriptive',
        analyzer: {
          scatterChart: {
            cascaderValue: null,
            cascaderList: CascaderComponent.data().options1,
            data: null,
            xAxis: null,
            title: '',
            axis: {
              xName: null,
              yName: 'Score'
            }},
          barChart: {
            cascaderValue: null,
            cascaderList: CascaderComponent.data().options2,
            data: null,
            xAxis: null,
            title: '',
            axis: {
              xName: 'States',
              yName: 'Score'
            }
          }
        },
        notifications: {
          labelHints: false,
          tryAreaHints: false,
          auHints: false,
          melHints: false
        },
        showPieData: {
          showTweetsData: null,
          showIncomeProportion: null,
          showSourceProportion: null,
          showGenderProportion: null,
          showAgeProportion: null,
        },
        showLineData: {

        },
        tweetsData: {
          cn: {
            states: {},
            mel: {}
          },
          virus: {
            states: {},
            mel: {}
          },
          happiness: {
            states: {},
            mel: {}
          }
        },
        incomeData: {
          states: {},
          mel: {}
        },
        populationData: {
          states: {},
          mel: {}
        },
        neighborList: {}
      }
    },
    mounted () {
      this.initMap()
      this.getAurinData()
      this.listenToResize()
    },
    methods: {

      initMap (){
        let map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -26.1666, lng: 133.9575},
          zoom: 4.3,
          mapTypeId: 'hybrid',
          disableDefaultUI: true
        })

        if(this.curTopic == null){
          setTimeout(() => {
            Notification.info({
              title: 'Hints',
              message: 'Try selecting a topic at first.',
              offset: 150
            })
          }, 1000)
        }
        // var marker = new google.maps.Marker({
        //   position: {lat: -37.8001, lng: 144.9575},
        //   map: map,
        //   title: 'melb'
        // });
      },

      // use async & await to sync
      async requestTweetsData(topic){
        const axios = require('axios')
        switch(topic){
          case 'happiness':
            let res = await axios.get('api/generalsenti_mel')
            processTweetsData(res.data, this.tweetsData.happiness.mel, this.getColorRank)
            res = await axios.get('api/generalsenti_all')
            processTweetsData(res.data, this.tweetsData.happiness.states, this.getColorRank)
            break
          case 'cn':
            res = await axios.get('api/cn_all')
            processTweetsData(res.data, this.tweetsData.cn.states, this.getColorRank)
            break
          case 'virus':
            res = await axios.get('api/covid19_all')
            processTweetsData(res.data, this.tweetsData.virus.states, this.getColorRank)
            break
        }

        function processTweetsData (data, tweetsTopicArea, getColorRank) {
          let name
          let sentimentList = [], attentionList = []
          const math = create(all, {})
          for(name in data){
            if(tweetsTopicArea[name] != null) continue // can be removed if want to further update data; e.g. streaming
            tweetsTopicArea[name] = {
              abstract:{
                sentiment:{
                  positive: null,
                  negative: null,
                  neutral : null,
                },
                sentimentScore: null,
                attentionScore: null,
                sentimentLevel: null,
                attentionLevel: null,
                relatedTotal: null,
                total: null
              },
              charts: {
                sentiment: [],
              },
            }
            let dataFields = data[name]['data']
            let obj = tweetsTopicArea[name]
            obj.abstract.relatedTotal = dataFields['related_tweets']
            obj.abstract.total = dataFields['total_tweets']
            obj.abstract.sentiment.positive = dataFields['sentiment']['positive']
            obj.abstract.sentiment.negative = dataFields['sentiment']['negative']
            obj.abstract.sentiment.neutral = dataFields['sentiment']['neutral']
            // format the number with 6 decimal places
            obj.abstract.sentimentScore =
              Math.floor((1 - obj.abstract.sentiment.negative / obj.abstract.relatedTotal) * 100000) / 100000
            sentimentList.push(obj.abstract.sentimentScore)
            obj.abstract.attentionScore =
              Math.floor((obj.abstract.relatedTotal / obj.abstract.total) * 100000) / 100000
            attentionList.push(obj.abstract.attentionScore)
            for(const label in dataFields['sentiment']){
              obj.charts.sentiment.push({name: label, value: dataFields['sentiment'][label]})
            }
          }
          if(sentimentList.length === 0 || attentionList.length === 0) return
          let sentimentMean = math.mean(sentimentList), sentimentStd = math.std(sentimentList)
          let sentiLeftQuantile = sentimentMean - sentimentStd
          let sentiRightQuantile = sentimentMean + sentimentStd
          let attentionMean = math.mean(attentionList), attentionStd = math.std(attentionList)
          let attentLeftQuantile = attentionMean - attentionStd
          let attentRightQuantile = attentionMean + attentionStd
          for(name in data){
            tweetsTopicArea[name].abstract.sentimentLevel =
              getColorRank(tweetsTopicArea[name].abstract.sentimentScore, sentiLeftQuantile, sentiRightQuantile)
            tweetsTopicArea[name].abstract.attentionLevel =
              getColorRank(tweetsTopicArea[name].abstract.attentionScore, attentLeftQuantile, attentRightQuantile)
          }
        }
      },

      getColorRank(value, lQuantile, rQuantile){
        let interval = (rQuantile - lQuantile) / 4
        if (value <= lQuantile) return 0
        else if(value > lQuantile && value <= lQuantile + interval) return 1
        else if(value > lQuantile + interval && value <= lQuantile + 2*interval) return 2
        else if(value > lQuantile + 2*interval && value <= lQuantile + 3*interval) return 3
        else if(value > lQuantile + 3*interval && value <= rQuantile) return 4
        else return 5
      },

      getAurinData() {
        const math = create(all, {})
        processPopulation(populationJsonAU, this.populationData.states, this.getColorRank)
        processPopulation(populationJsonMEL, this.populationData.mel, this.getColorRank)
        processIncome(incomeJsonAU, this.incomeData.states, this.getColorRank)
        processIncome(incomeJsonMEL, this.incomeData.mel, this.getColorRank)

        // get neighbors for each suburb, used for further color simulation
        for(const key in neighborJsonMEL){
          let record = neighborJsonMEL[key]
          this.neighborList[record['name']] = record['neighbors']
        }

        function processPopulation (json, populationArea, getColorRank) {
          let sizeList = [], ageList = []
          for (const key in json) {
            let label
            let record = json[key]
            if (populationArea[record['Name']] != null) continue
            populationArea[record['Name']] = {
              maleTotal: null,
              femaleTotal: null,
              total: null,
              medianAge: null,
              ageLevel: null,
              sizeLevel: null,
              charts: {
                ageProportion: [],
                genderProportion: []
              }
            }
            let obj = populationArea[record['Name']]
            obj.maleTotal = record['Gender proportion']['Total male population']
            obj.femaleTotal = record['Gender proportion']['Total Female population']
            obj.total = obj.maleTotal + obj.femaleTotal
            sizeList.push(obj.total)
            obj.medianAge = record['Median age']
            ageList.push(obj.medianAge)
            for (label in record['Age proportion']) {
              obj.charts.ageProportion.push({name: label, value: record['Age proportion'][label]})
            }
            for (label in record['Gender proportion']) {
              obj.charts.genderProportion.push({name: label, value: record['Gender proportion'][label]})
            }
          }
          let sizeMean = math.mean(sizeList), sizeStd = math.std(sizeList)
          let lSizeQuantile = sizeMean - 2 * sizeStd, rSizeQuantile = sizeMean + 2 * sizeStd

          let ageMean = math.mean(ageList), ageStd = math.std(ageList)
          let lAgeQuantile = ageMean - 2 * ageStd, rAgeQuantile = ageMean + 2 * ageStd
          for (const key in json) {
            populationArea[json[key]['Name']].sizeLevel =
              getColorRank(populationArea[json[key]['Name']].total, lSizeQuantile, rSizeQuantile)
            populationArea[json[key]['Name']].ageLevel =
              getColorRank(populationArea[json[key]['Name']].medianAge, lAgeQuantile, rAgeQuantile)
          }
        }

        function processIncome (json, incomeArea, getColorRank) {
          let list = []
          for (const key in json) {
            let label
            let record = json[key]
            if (incomeArea[record['Name']] != null) continue
            incomeArea[record['Name']] = {
              median: null,
              mean: null,
              incomeLevel: null,
              charts: {
                incomeProportion: [],
                sourceProportion: []
              }
            }
            let obj = incomeArea[record['Name']]
            obj.median = record['Personal median total income']
            obj.mean = record['Personal mean total income']
            list.push(obj.mean)
            for (label in record['Income proportion']) {
              obj.charts.incomeProportion.push({name: label, value: record['Income proportion'][label]})
            }
            for (label in record['Main source proportion']) {
              obj.charts.sourceProportion.push({name: label, value: record['Main source proportion'][label]})
            }
          }
          let mean = math.mean(list), std = math.std(list)
          let lQuantile = mean - 2*std, rQuantile = mean + 3*std
          for (const key in json) {
            incomeArea[json[key]['Name']].incomeLevel =
              getColorRank(incomeArea[json[key]['Name']].mean, lQuantile, rQuantile)
          }
        }
      },

      changeTopic(topic){
        if(this.curTopic !== topic){
          this.curTopic = topic
          this.curArea = null
          this.requestTweetsData(topic)
          Common.loading("Requesting Tweets Data From Database...", 1000)
          this.initMap()
          this.notifications.auHints = false // re-notify after switching topics
          this.notifications.melHints = false
          if(!this.notifications.tryAreaHints){
            setTimeout(() => {
              Notification.info({
                title: 'Hints',
                message: 'Then choose areas.',
                offset: 150
              })
            }, 1500)
            setTimeout(() => {
              Notification.info({
                title: 'Hints',
                message: 'Area options can be different due to the different amount of data of the topics.',
                offset: 150
              })
            }, 2500)
            this.notifications.tryAreaHints = true // do not hint choosing areas
          }

        }
      },

      switchTo(area) {
        Common.loading("Loading...", 2000)
        this.curArea = area
        let thisObj = this
        let infoWindow = new google.maps.InfoWindow({});
        if(area === 'states'){
          let colors = ["#ffffff","#ffd6cc","#ffad99","#ff8566","#ff5c33","#ff3300"]
          let map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: -28.8001, lng: 133.9575},
            zoom: 4.3,
            mapTypeId: 'hybrid',
            disableDefaultUI: true
          })
          map.data.loadGeoJson(
            '../../static/nation_city.json');
          map.data.setStyle(function(feature){
            return getColor(thisObj, colors, feature.getProperty('GCC_NAME16'))
          })

          google.maps.event.addListener(infoWindow, 'closeclick', function() {
            map.data.revertStyle();
          });

          map.data.addListener('click', function (event) {
            map.data.revertStyle();
            map.data.overrideStyle(event.feature, { strokeWeight: 1, fillColor: '#007bff', fillOpacity: 0.8});
            let name = event.feature.getProperty('GCC_NAME16')
            thisObj.showData(thisObj, name)
            thisObj.curLocation = name
            let info = '<h6> Abstract: ' + name + '</h6>';
            info += thisObj.createInfo(thisObj, name)
            infoWindow.setContent(info)
            infoWindow.setPosition(event.latLng);
            infoWindow.open(map)
          })

        }
        else if(area === 'mel'){
          let colors = ["#ffffff","#ffd6cc","#ffad99","#ff8566","#ff5c33","#ff3300"]
          let map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: -37.8001, lng: 144.9575},
            zoom: 11.6,
            mapTypeId: 'hybrid',
            disableDefaultUI: true
          })

          map.data.loadGeoJson(
            '../../static/greater_melb_sub.json');

          map.data.setStyle(function(feature){
            return getColor(thisObj, colors, feature.getProperty('name'))
          })

          google.maps.event.addListener(infoWindow, 'closeclick', function() {
            map.data.revertStyle();
          });

          map.data.addListener('click', function (event) {
            map.data.revertStyle();
            map.data.overrideStyle(event.feature, { strokeWeight: 1, fillColor: '#007bff', fillOpacity: 0.8});
            let name = event.feature.getProperty('name')
            thisObj.showData(thisObj, name)
            thisObj.curLocation = name
            // event.feature.toGeoJson(function (obj) {
            //   name = JSON.stringify(obj)
            // })
            let info = '<h6> Abstract: ' + name + '</h6>';
            info += thisObj.createInfo(thisObj, name)
            infoWindow.setContent(info)
            infoWindow.setPosition(event.latLng);
            infoWindow.open(map);
          })
        }

        // show switch-label hints to user
        if(!this.notifications.labelHints){
          setTimeout(() => {
            Notification.info({
              title: 'Hints',
              message: 'You can change labels to switch scopes.',
              offset: 150
            })
          }, 3500)
          this.notifications.labelHints = true // only hint once within one topic
        }

        // welcome after the first time routing to the place
        let place = ''
        if(this.curArea === 'states' && !this.notifications.auHints) {
          place = 'Australia'
          this.notifications.auHints = true
        }
        else if(this.curArea === 'mel' && !this.notifications.melHints) {
          place = 'Melbourne'
          this.notifications.melHints = true
        }
        else return
        setTimeout(() => {
          Message.info({
            message: 'Welcome to ' + place + '!',
            center: true,
            showClose: true
          })
        }, 2000)


        function getColor (thisObj, colors, name) {
          let index = -1
          let neighbors = thisObj.neighborList[name]
          let levelMap = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}, max = 0

          // only used to simplify duplicated codes
          function shuffling(level){
            levelMap[level] += 1
            max = (levelMap[level] > max) ?
              levelMap[level] : max
          }

          // only used to simplify duplicated codes
          function reducing(){
            const math = create(all, {})
            let result = []
            for(const key in levelMap){
              if(levelMap[key] === max){
                result.push(key)
              }
            }
            return Math.ceil(math.mean(result))
          }

          switch(thisObj.curLabel){
            case 'sentiment':
              if(thisObj.tweetsData[thisObj.curTopic][thisObj.curArea][name] == null) {
                if(neighbors == null) break
                for(const n of neighbors){
                  let neighborData = thisObj.tweetsData[thisObj.curTopic][thisObj.curArea][n]
                  if(neighborData == null) continue
                  shuffling(neighborData.abstract.sentimentLevel)
                }
                index = (max === 0) ? -1 : reducing()
                break
              }
              index = thisObj.tweetsData[thisObj.curTopic][thisObj.curArea][name].abstract.sentimentLevel
              break
            case 'attention':
              if(thisObj.tweetsData[thisObj.curTopic][thisObj.curArea][name] == null) {
                if(neighbors == null) break
                for(const n of neighbors){
                  let neighborData = thisObj.tweetsData[thisObj.curTopic][thisObj.curArea][n]
                  if(neighborData == null) continue
                  shuffling(neighborData.abstract.attentionLevel)
                }
                index = (max === 0) ? -1 : reducing()
                break
              }
              index = thisObj.tweetsData[thisObj.curTopic][thisObj.curArea][name].abstract.attentionLevel
              break
            case 'size':
              if(thisObj.populationData[thisObj.curArea][name] == null) {
                if(neighbors == null) break
                for(const n of neighbors){
                  let neighborData = thisObj.populationData[thisObj.curArea][n]
                  if(neighborData == null) continue
                  shuffling(neighborData.sizeLevel)
                }
                index = (max === 0) ? -1 : reducing()
                break
              }
              index = thisObj.populationData[thisObj.curArea][name].sizeLevel
              break
            case 'age':
              if(thisObj.populationData[thisObj.curArea][name] == null) {
                if(neighbors == null) break
                for(const n of neighbors){
                  let neighborData = thisObj.populationData[thisObj.curArea][n]
                  if(neighborData == null) continue
                  shuffling(neighborData.ageLevel)
                }
                index = (max === 0) ? -1 : reducing()
                break
              }
              index = thisObj.populationData[thisObj.curArea][name].ageLevel
              break
            case 'income':
              if(thisObj.incomeData[thisObj.curArea][name] == null) {
                for(const n of neighbors){
                  let neighborData = thisObj.incomeData[thisObj.curArea][n]
                  if(neighborData == null) continue
                  shuffling(neighborData.incomeLevel)
                }
                index = (max === 0) ? -1 : reducing()
                break
              }
              index = thisObj.incomeData[thisObj.curArea][name].incomeLevel
              break
          }
          if(index === -1) return {
            fillColor: 'grey',
            fillOpacity: 0.6,
            strokeWeight: 1
          }
          else return{
            fillColor: colors[index],
            fillOpacity: 0.8,
            strokeWeight: 1
          }
        }
      },

      showData(thisObj, name){
        switch(thisObj.curTopic){
          case 'cn':
            thisObj.showPieData.showTweetsData = (thisObj.tweetsData.cn[thisObj.curArea][name] != null) ?
              thisObj.tweetsData.cn[thisObj.curArea][name].charts.sentiment : null
            break
          case 'virus':
            thisObj.showPieData.showTweetsData = (thisObj.tweetsData.virus[thisObj.curArea][name] != null) ?
              thisObj.tweetsData.virus[thisObj.curArea][name].charts.sentiment : null
            break
          case 'happiness':
            thisObj.showPieData.showTweetsData = (thisObj.tweetsData.happiness[thisObj.curArea][name] != null) ?
              thisObj.tweetsData.happiness[thisObj.curArea][name].charts.sentiment : null
            break
        }
        thisObj.showPieData.showGenderProportion = (thisObj.populationData[thisObj.curArea][name] != null) ?
          thisObj.populationData[thisObj.curArea][name].charts.genderProportion : null
        thisObj.showPieData.showAgeProportion = (thisObj.populationData[thisObj.curArea][name] != null) ?
          thisObj.populationData[thisObj.curArea][name].charts.ageProportion : null
        thisObj.showPieData.showIncomeProportion = (thisObj.incomeData[thisObj.curArea][name] != null) ?
          thisObj.incomeData[thisObj.curArea][name].charts.incomeProportion : null
        thisObj.showPieData.showSourceProportion = (thisObj.incomeData[thisObj.curArea][name] != null) ?
          thisObj.incomeData[thisObj.curArea][name].charts.sourceProportion : null
      },

      createInfo(thisObj, name){
        let topicData = null
        let info = ''
        let topicName = ''
        switch(thisObj.curTopic){
          case 'cn':
            topicData = thisObj.tweetsData.cn[thisObj.curArea]
            topicName = 'China'
            break
          case 'virus':
            topicData = thisObj.tweetsData.virus[thisObj.curArea]
            topicName = 'COVID-19'
            break
          case 'happiness':
            topicData = thisObj.tweetsData.happiness[thisObj.curArea]
            topicName = 'Happiness'
            break
        }
        let err = '<div style="font-size: 12px; line-height: 22px"><div style="font-weight: bold"> NO DATA </div>' +
          '<div>Color simulated by its neighbours</div></div>'
        switch (thisObj.curLabel){
          case 'sentiment':
            if(topicData[name] == null) return err
            info += '<div style="font-size: 12px; line-height: 22px">' +
              '<div> Positive: ' + topicData[name].abstract.sentiment.positive + '</div>' +
              '<div> Neutral: ' + topicData[name].abstract.sentiment.neutral + '</div>' +
              '<div> Negative: ' + topicData[name].abstract.sentiment.negative + '</div>' +
              '<div> Sentiment Score: ' + topicData[name].abstract.sentimentScore + '</div>' +
              '<div> Sentiment Level: Level ' + topicData[name].abstract.sentimentLevel + '</div>' +
              '<a href="#" data-toggle="modal" data-target="#detailInfoModal"> details </a></div>'
            break
          case 'attention':
            if(topicData[name] == null) return err
            info += '<div style="font-size: 12px; line-height: 22px"> ' +
              '<div> Tweets related to ' + topicName + ': ' + topicData[name].abstract.relatedTotal + '</div>' +
              '<div> Total: ' + topicData[name].abstract.total + '</div>' +
              '<div> Attention Level: Level ' + topicData[name].abstract.attentionLevel + '</div>' +
              '<a href="#" data-toggle="modal" data-target="#detailInfoModal"> details </a></div>'
            break
          case 'size':
            if(thisObj.populationData[thisObj.curArea][name] == null) return err
            info += '<div style="font-size: 12px; line-height: 22px"> ' +
              '<div> Total: ' + thisObj.populationData[thisObj.curArea][name].total + '</div>' +
              '<div> Population Size Level: Level ' + thisObj.populationData[thisObj.curArea][name].sizeLevel + '</div>' +
              '<a href="#" data-toggle="modal" data-target="#detailInfoModal"> details </a></div>'
            break
          case 'age':
            if(thisObj.populationData[thisObj.curArea][name] == null) return err
            info += '<div style="font-size: 12px; line-height: 22px"> ' +
              '<div> Median Age: ' + thisObj.populationData[thisObj.curArea][name].medianAge + '</div>' +
              '<div> Population Age Level: Level ' + thisObj.populationData[thisObj.curArea][name].ageLevel + '</div>' +
              '<a href="#" data-toggle="modal" data-target="#detailInfoModal"> details </a></div>'
            break
          case 'income':
            if(thisObj.incomeData[thisObj.curArea][name] == null) return err
            info += '<div style="font-size: 12px; line-height: 22px"> ' +
              '<div> Mean: ' + thisObj.incomeData[thisObj.curArea][name].mean + '</div>' +
              '<div> Median: ' + thisObj.incomeData[thisObj.curArea][name].median + '</div>' +
              '<div> Income Level: Level ' + thisObj.incomeData[thisObj.curArea][name].incomeLevel + '</div>' +
              '<a href="#" data-toggle="modal" data-target="#detailInfoModal"> details </a></div>'
            break
        }
        return info
      },

      async renderScatterCharts(value){
        Common.loading("Processing...", 2000, document.getElementById('analysisModalBody'))
        let params = value.toString().split(',')
        let area = params[0], yAxisTopic = params[1], yAxis = params[2]
        await this.requestTweetsData(yAxisTopic) // request data again, in case the tweets data isn't loaded
        let xData, xScoreLabel
        let yData = this.tweetsData[yAxisTopic][area], yScoreLabel = yAxis + 'Score'
        let scale = 1
        switch (this.analyzer.scatterChart.xAxis) {
          case 'population-size':
            xScoreLabel = 'total'
            xData = this.populationData[area]
            scale = 100000
            this.analyzer.scatterChart.axis.xName = '* 10^5 persons'
            break
          case 'population-age':
            xScoreLabel = 'medianAge'
            xData = this.populationData[area]
            scale = 10
            this.analyzer.scatterChart.axis.xName = '* 10 years'
            break
          case 'income':
            xScoreLabel = 'mean'
            xData = this.incomeData[area]
            scale = 100000
            this.analyzer.scatterChart.axis.xName = '* 10^5 AUD'
            break
        }
        let result = []
        for (const name in xData) {
          if (yData[name] == null) continue
          let sample = []
          if(yData[name].abstract['total'] < 50) continue
          sample.push(xData[name][xScoreLabel] / scale)
          sample.push(yData[name].abstract[yScoreLabel])
          result.push(sample)
        }
        this.analyzer.scatterChart.data = result
      },

      async renderBarCharts(value){
        Common.loading("Processing...", 2000, document.getElementById('analysisModalBody'))
        let params = value.toString().split(','), yAxisTopic = params[0], yAxis = params[1]
        await this.requestTweetsData(yAxisTopic) // request data again, in case the tweets data isn't loaded
        switch (yAxisTopic) {
          case 'cn':
            this.analyzer.barChart.title = 'China related tweets ' + yAxis
            break
          case 'virus':
            this.analyzer.barChart.title = 'COVID-19 related tweets ' + yAxis
            break
          case 'happiness':
            this.analyzer.barChart.title = '"Happiness"'
            break
        }
        let yData = this.tweetsData[yAxisTopic].states, yScoreLabel = yAxis + 'Score'
        let result = [[],[]]
        for (const name in yData) {
          result[0].push(name)
          result[1].push(yData[name].abstract[yScoreLabel])
        }
        this.analyzer.barChart.data = result
      },

      changeTag(tag, noWait){
        this.curModal = tag
        if(noWait == null)
          Common.loading("Initializing Charts...", 1000, document.getElementById('detailModalBody'))
      },

      // Poor compatibility caused by bootstrap & echarts; have to use jquery to handle the resizing of the charts
      // Basically, the above two are not commonly used in Vue framework, which is data-driven
      listenToResize(){
        let changeTag = this.changeTag
        let loading = Common.loading
        $('#detailInfoModal').on('show.bs.modal', function () {
          loading('Initializing Charts...', 1000, document.getElementById('detailModalBody'))
          changeTag('tweets', true)
        });
        $('#detailInfoModal').on('hide.bs.modal', function () {
          changeTag(null, true)
        });
      }
    }
  }

</script>

<style>
  #map {
    height: 100vh;
    width: 100%
  }

  #clickables {
    position: absolute;
    width: 100%;
    top: 90px;
  }

  #detailInfoModal {
    position: absolute;
    top: 50%; left: 50%;
    width: 30%;
    transform: translate(-50%,-50%);
  }

  .separator {
    padding: 0.25rem 1.5rem;
    font-weight: 500;
  }

  .dropdown-menu{
    background-color: #1d2124;
    color: white;
  }

  .dropdown-item{
    cursor: pointer;
    background-color: #1d2124;
  }

  .dropdown-item:hover{
    background-color:#007bff
  }

  .pieChart {
    height: 150px;
    width: 150px;
  }

  .centerCol {
    display:flex;
    justify-content:center;
    align-items:center;
  }

  #detailModalBody .el-loading-spinner {
    transform: translate(-50%, 0);
  }

  #detailModalBody .el-loading-spinner .el-loading-text {
    font-size: 12px;
  }

</style>
