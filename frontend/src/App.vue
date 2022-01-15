<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <h1 class="name">gait.fun</h1>
  <HelloWorld msg="Hello Vue 3.0 + Vite" />
</template>

<script lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import './assets/app.css'
import data from './assets/peter.json'
// 添加ts代码
const peter:string = 'gati.fun'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  // 验证ts是否work
  mounted(){
    console.log(peter)
    console.log(data.name + '|' + data.website)
  },
}
</script>

<style lang="scss">
.name{
  color: green;
}
</style>