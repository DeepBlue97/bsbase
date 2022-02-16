<template>
  <!-- <div class="common-layout">
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px">Aside</el-aside>
        <el-main>Main</el-main>
      </el-container>
    </el-container>
  </div> -->
  <!-- <el-container>

    <el-header>Header</el-header>
    <el-aside width="200px">Aside</el-aside>


  </el-container> -->

      <!-- <el-main> -->
      <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
      <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App" /> -->
      <Navigation/>
      <!-- <SideBar/> -->
      <!-- <button @click="getJson">get json</button> -->
    <!-- </el-main> -->
</template>

<script lang="ts">
import { defineComponent } from "vue";
// import HelloWorld from "./components/HelloWorld.vue";
// import SideBar from "./components/SideBar.vue";
import Navigation from "./components/Navigation.vue";

import axios from "axios";

export default defineComponent({
  name: "App",
  components: {
    Navigation,
  },
  methods: {
    getJson() {
      axios.get("http://localhost:9000/api/").then(
        (response) => {
          console.log("请求成功!", response.data);
        },
        (error) => {
          console.log("请求失败！", error.message);
        }
      );
    },
  },
});
</script>

<style scoped>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
.common-layout .el-header,
.common-layout .el-footer {
  background-color: #b3c0d1;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 60px;
}
.common-layout .el-footer {
  line-height: 60px;
}

.common-layout .el-aside {
  background-color: #d3dce6;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 200px;
}

.common-layout .el-main {
  background-color: #e9eef3;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 160px;
}

.common-layout > .el-container {
  margin-bottom: 40px;
}

.common-layout .el-container:nth-child(5) .el-aside,
.common-layout .el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.common-layout .el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
