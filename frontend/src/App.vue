<template>

  <Navigation/>

</template>

<script lang="ts">
import { defineComponent } from "vue";
// import HelloWorld from "./components/HelloWorld.vue";
// import SideBar from "./components/SideBar.vue";
import Navigation from "./components/Navigation.vue";

// import axios from "axios";

// import { ref } from 'vue'
// const value1 = ref(true)

export default defineComponent({
  name: "App",
  components: {
    Navigation,
  },
  data() {
    return {
      // value1: true
    }
  },
  // props: {
  //   value1
  // },
  methods: {
  //   getJson() {
  //     axios.get("http://localhost:9001/api/").then(
  //       (response) => {
  //         console.log("请求成功!", response.data);
  //       },
  //       (error) => {
  //         console.log("请求失败！", error.message);
  //       }
  //     );
  //   },
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}
body{
  background-color: #FFFFF0
}

</style>
