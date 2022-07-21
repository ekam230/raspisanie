<script>
import RealTime from './components/RealTime.vue'
import Tablo from './components/Tablo.vue'
import CarouselVue from './components/Carousel.vue'

export default {
  components: {
    Tablo,
    RealTime,
    CarouselVue
},
data() {
          return {
              connection: null,
              myObject: {},
              arrayList: [[0,1,2,3,4],
                          [5,6,7,8,9]
              ]
          }
        },
        created: function() {
            console.log("Starting connection to WebSocket Server")
            this.connection = new WebSocket("ws://localhost:6789/")
            var vm = this;
            this.connection.onmessage = function(event) {
              console.log(event);
              let result = JSON.parse(event.data);
              console.log(result)
              
              if (result.type == "list_data") {
                delete result.type;
                vm.myObject = result;
              }                      
            }
        
            this.connection.onopen = function(event) {
              console.log(event)
              console.log("Successfully connected to websocket server...")
            }
        
          },
          methods: {
            sendMessage: function(message) {
              console.log(this.connection);
              this.connection.send(JSON.stringify(message));
            }
          },
}
            
</script>

<template>
  <div>
    <div id="time" class="columns">
      <div class="column is-2 is-offset-10 is-size-2">
      <div class="is-size-4">Текущее время</div>
        <RealTime></RealTime>
      </div>            
    </div>
          
    <div class="columns has-text-centered is-size-4">
      <div class="column is-2">Оператор</div>
      <div class="column is-1">Время</div>
      <div class="column is-2">Направление</div>
      <div class="column is-3">Название</div>
      <div class="column is-2">Причал</div>
      <div class="column is-2">Примечания</div>
    </div>
    
    <carousel-vue :arrayList="arrayList" :myObject="myObject"></carousel-vue>
        <!-- <Tablo
          v-for="(item,i) in myObject"
          :key="i"
          :name="item.name"
          :operator="item.operator"
          :time="item.time"
          :path="item.path"
          :terminal="item.terminal" class="has-text-centered is-size-3"
          :remarks="item.remarks"
        ></Tablo> -->
  </div>
</template>

<style>
/* @import './assets/base.css'; */
/* import './node_modules/bulma/CSS/bulma.css'; */
@import '../node_modules/bulma/css/bulma.min.css';
@import '../../css/style.css'


</style>
