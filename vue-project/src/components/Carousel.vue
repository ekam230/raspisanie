<template>
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
  <Carousel :autoplay="10000" :wrap-around="true" pause-autoplay-on-hover>
    <Slide v-for="(slide,i) in arrayList" :key="i">
    <div class="carousel__item">
      <div v-for="item_dfg in slide" :key="item_dfg" > <!-- {{ myObject[item_dfg]}}  -->
      <Tablo :myObject = "myObject[item_dfg]"
      ></Tablo>
      <!-- <Tablo myObject[item_dfg]"
      :key="key.id"
      :name="key.name"
      :operator="key.operator"
      :time="key.time"
      :path="key.path"
      :terminal="key.terminal" class="has-text-centered is-size-3"
      :remarks="key.remarks"
      ></Tablo> -->
      <!-- <span v-for="(value, key) in myObject[item_dfg]">{{ key }}: {{ value }}</span> -->
      </div>
      <!-- <div class="carousel__item">{{slide}} --> 
        
      </div>
    </Slide>

    <template #addons>
      <Pagination />
    </template>
  </Carousel>
  
</template>

<script>
import { defineComponent } from 'vue';
import Tablo from './Tablo.vue';
import { Carousel, Pagination, Slide } from '../../node_modules/vue3-carousel/dist/carousel.es';
import '../../node_modules/vue3-carousel/dist/carousel.css';
export default defineComponent({
  name: 'Autoplay',
  components: {
    Carousel,
    Slide,
    Pagination,
    Tablo,
  },
  props: ['myObject', 'arrayList']
});
</script>