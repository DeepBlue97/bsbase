<template>
  <div class="labeltask">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <h3>标注任务界面</h3>
    <h5>增加、查询、删除标注任务</h5>

    <p>
      姓名：{{ name }}, 公司：{{ company }}, 月薪：{{ salary }}, 年薪{{ total }}
    </p>
    <button @click="double">月薪double</button>

    <div class="demo-date-picker">
      <div class="block">
        <span class="demonstration">Default</span>
        <el-date-picker v-model="value1" type="date" placeholder="Pick a day">
        </el-date-picker>
      </div>
      <div class="block">
        <span class="demonstration">Picker with quick options</span>
        <el-date-picker
          v-model="value2"
          type="date"
          placeholder="Pick a day"
          :disabled-date="disabledDate"
          :shortcuts="shortcuts"
        >
        </el-date-picker>
      </div>
    </div>

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
import { defineComponent, reactive, toRefs, ref, computed } from "vue";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src
// import Navigation from '@/components/Navigation.vue'; // @ is an alias to /src

const shortcuts = [
  {
    text: "Today",
    value: new Date(),
  },
  {
    text: "Yesterday",
    value: () => {
      const date = new Date();
      date.setTime(date.getTime() - 3600 * 1000 * 24);
      return date;
    },
  },
  {
    text: "A week ago",
    value: () => {
      const date = new Date();
      date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
      return date;
    },
  },
];

const disabledDate = (time: Date) => {
  return time.getTime() > Date.now();
};

// @Options({

// })
// export default class LabelTask extends Vue {}
export default defineComponent({
  components: {
    HelloWorld,
  },
  data() {
    return {
      value1: true,
      value2: ref(true),
    };
  },
  setup() {
    // 定义响应式对象
    const company = ref("DiDi");
    const name = ref("小王");
    const salary = ref(18000);
    const double = () => {
      salary.value *= 2;
      console.log("double!");
    };
    const total = computed(() => 12 * salary.value);

    return {
      name,
      company,
      total,
      salary,
      double,
    };
  },
  // props: {
  //   value1: Boolean,
  //   value2: Boolean,
  // }
});
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
.demo-date-picker {
  display: flex;
  width: 100%;
  padding: 0;
  flex-wrap: wrap;
}
.demo-date-picker .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color-base);
  flex: 1;
}
.demo-date-picker .block:last-child {
  border-right: none;
}
.demo-date-picker .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}
</style>