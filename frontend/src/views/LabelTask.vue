<template>
  <div class="labeltask">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <h3>标注任务界面</h3>
    <h5>增加、查询、删除标注任务</h5>

    <el-tabs
      :tab-position="tabPosition"
      style="height: 200px"
      class="demo-tabs"
    >
      <el-tab-pane label="User">User<el-switch v-model="value1" /></el-tab-pane>
      <el-tab-pane label="Config">Config</el-tab-pane>
      <el-tab-pane label="Role">Role</el-tab-pane>
      <el-tab-pane label="Task">Task</el-tab-pane>
    </el-tabs>

    
    <el-switch
      v-model="value2"
      class="ml-2"
      active-color="#13ce66"
      inactive-color="#ff4949"
    />

    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App" />
    <!-- <Navigation/> -->
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src
// import Navigation from '@/components/Navigation.vue'; // @ is an alias to /src
import { ref } from "vue";

// const value1 = ref(true)
// const value2 = ref(true)

@Options({
  components: {
    HelloWorld,
  },
  data() {
    return {
      value1: true,
      value2: ref(true),
    };
  },
  // props: {
  //   value1: Boolean,
  //   value2: Boolean,
  // }
})
export default class LabelTask extends Vue {}
</script>

<style>
.demo-tabs > .el-tabs__content {
  padding: 32px;
  background-color: #f4f5f7;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

.el-tabs--right .el-tabs__content,
.el-tabs--left .el-tabs__content {
  height: 100%;
}
</style>