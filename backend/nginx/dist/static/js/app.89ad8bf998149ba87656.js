webpackJsonp([1],{I4hv:function(t,e){},NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n("7+uW"),s={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("nav",{staticClass:"navbar navbar-expand-lg navbar-dark bg-dark"},[n("a",{staticClass:"navbar-brand",attrs:{href:"#"}},[t._v("Team 38")]),t._v(" "),n("button",{staticClass:"navbar-toggler",attrs:{type:"button","data-toggle":"collapse","data-target":"#navbarItems","aria-controls":"navbarItems","aria-expanded":"false","aria-label":"Toggle navigation"}},[n("span",{staticClass:"navbar-toggler-icon"})]),t._v(" "),n("div",{staticClass:"collapse navbar-collapse",attrs:{id:"navbarItems"}},[n("div",{staticClass:"navbar-nav"},[n("a",{staticClass:"nav-item nav-link active",attrs:{href:"/"}},[t._v("Home")]),t._v(" "),n("a",{staticClass:"nav-item nav-link active",attrs:{href:"/map"}},[t._v("Map")]),t._v(" "),n("a",{staticClass:"nav-item nav-link active",attrs:{href:"/about"}},[t._v("About us")])])])])}]},i={name:"App",components:{BarComponent:n("VU/8")({name:"BarComponent"},s,!1,null,null,null).exports}},r={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("BarComponent"),this._v(" "),e("router-view")],1)},staticRenderFns:[]},o=n("VU/8")(i,r,!1,null,null,null).exports,l=n("/ocq"),c={name:"MapComponent",mounted:function(){this.initMap()},methods:{initMap:function(){new google.maps.Map(document.getElementById("map"),{center:{lat:-34.397,lng:150.644},zoom:8})}}},p={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("div",{attrs:{id:"map"}})])}]};var v=n("VU/8")(c,p,!1,function(t){n("I4hv")},null,null).exports,u={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"container"},[e("div",{staticClass:"background"}),this._v(" "),e("div",{staticClass:"center"},[e("p",{staticStyle:{"text-align":"center",color:"white","font-size":"35px","font-family":"-apple-system","font-weight":"bold"}},[this._v("\n    COMP90024 Cluster & Cloud Computing Project")]),this._v(" "),e("p",{staticStyle:{"text-align":"center"}},[e("button",{staticClass:"btn btn-light",staticStyle:{"font-weight":"bold"},attrs:{type:"button"}},[this._v("Explore")])])])])}]};var m=n("VU/8")(null,u,!1,function(t){n("tcbg")},null,null).exports;a.a.use(l.a);var d=new l.a({mode:"history",routes:[{path:"/",name:"HomeComponent",component:m},{path:"/map",name:"MapComponent",component:v}]});n("qb6w"),n("4kSj"),n("Bb4J");a.a.config.productionTip=!1,new a.a({el:"#app",router:d,components:{App:o},template:"<App/>"})},qb6w:function(t,e){},tcbg:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.89ad8bf998149ba87656.js.map