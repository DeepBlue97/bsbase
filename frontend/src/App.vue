<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>
  <button @click="getJson">get json</button>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import HelloWorld from './components/HelloWorld.vue';

import axios from "axios"


export default defineComponent({
  name: 'App',
  components: {
    HelloWorld
  },
  methods: {
    getJson(){
      axios.get('http://localhost:9000/api/').then(
        response => {
          console.log("请求成功!", response.data)
        },
        error => {
          console.log("请求失败！", error.message)
        }
      )
    }
  }
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
