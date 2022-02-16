<template>
  <div class="labelmanager">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <h3>标签管理界面</h3>
    <h5>CRUD 标签</h5>

    <div style="margin-bottom: 20px">
      <el-button size="small" @click="addTab(editableTabsValue)">
        add tab
      </el-button>
    </div>
    <el-tabs
      v-model="editableTabsValue"
      type="card"
      class="demo-tabs"
      closable
      @tab-remove="removeTab"
    >
      <el-tab-pane
        v-for="item in editableTabs"
        :key="item.name"
        :label="item.title"
        :name="item.name"
      >
        {{ item.content }}
      </el-tab-pane>
    </el-tabs>

    <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/> -->
    <!-- <Navigation/> -->
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
// import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
// import Navigation from '@/components/Navigation.vue'; // @ is an alias to /src
import { ref } from "vue";

// let tabIndex = 2
// const editableTabsValue = ref('2')

const editableTabs = ref([
  {
    title: "Tab 1",
    name: "1",
    content: "Tab 1 content",
  },
  {
    title: "Tab 2",
    name: "2",
    content: "Tab 2 content",
  },
]);

// const addTab = (targetName: string) => {
//   const newTabName = `${++tabIndex}`;
//   editableTabs.value.push({
//     title: "New Tab",
//     name: newTabName,
//     content: "New Tab content",
//   });
//   editableTabsValue.value = newTabName;
// };

// const removeTab = (targetName: string) => {
//   const tabs = editableTabs.value;
//   let activeName = editableTabsValue.value;
//   if (activeName === targetName) {
//     tabs.forEach((tab, index) => {
//       if (tab.name === targetName) {
//         const nextTab = tabs[index + 1] || tabs[index - 1];
//         if (nextTab) {
//           activeName = nextTab.name;
//         }
//       }
//     });
//   }

//   editableTabsValue.value = activeName;
//   editableTabs.value = tabs.filter((tab) => tab.name !== targetName);
// };

@Options({
  components: {
    // HelloWorld,
  },
  data() {
    return {
      tabIndex: 2,
      editableTabsValue: ref("2"),
    //   editableTabs: ref([
    //     {
    //       title: "Tab 1",
    //       name: "1",
    //       content: "Tab 1 content",
    //     },
    //     {
    //       title: "Tab 2",
    //       name: "2",
    //       content: "Tab 2 content",
    //     },
    //   ]),
    };
  },
  methods: {
    removeTab(targetName: string) {
      const tabs = editableTabs.value;
      let activeName = this.editableTabsValue.value;
      if (activeName === targetName) {
        tabs.forEach((tab, index) => {
          if (tab.name === targetName) {
            const nextTab = tabs[index + 1] || tabs[index - 1];
            if (nextTab) {
              activeName = nextTab.name;
            }
          }
        });
      }

      this.editableTabsValue.value = activeName;
      editableTabs.value = tabs.filter((tab) => tab.name !== targetName);
    },
    addTab(targetName: string) {
      const newTabName = `${++this.tabIndex}`;
      editableTabs.value.push({
        title: "New Tab",
        name: newTabName,
        content: "New Tab content",
      });
      this.editableTabsValue.value = newTabName;
    },
  },
})
export default class LabelManager extends Vue {}
</script>

<style>
.demo-tabs > .el-tabs__content {
  padding: 32px;
  background-color: #f4f5f7;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
</style>