<template>
  <el-container>
    <!-- <div id="nav"> -->
    <el-aside width="200px">
      <el-menu
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="el-menu-vertical-demo"
        default-active="2"
        text-color="#fff"
        @open="handleOpen"
        @close="handleClose"
      >
        <router-link to="/">
          <el-menu-item index="1">
            <el-icon><home-filled /></el-icon><span>Home</span>
          </el-menu-item>
        </router-link>
        <!-- <el-sub-menu index="1">
          <template #title>
            <el-icon><home-filled /></el-icon>
            <span>图片标注</span>
          </template>
          <router-link to="/labeltask"
            ><el-menu-item index="1-1"
              ><el-icon><list /></el-icon><span>标注任务</span></el-menu-item
            ></router-link
          >
          <router-link to="/labelmanager"
            ><el-menu-item index="1-2"
              ><el-icon><price-tag /></el-icon>标签管理</el-menu-item
            ></router-link
          >
        </el-sub-menu> -->

        <el-sub-menu index="2">
          <template #title>
            <el-icon><picture-filled /></el-icon>
            <span>图片标注</span>
          </template>
          <router-link to="/labeltask"
            ><el-menu-item index="2-1"
              ><el-icon><list /></el-icon><span>标注任务</span></el-menu-item
            ></router-link
          >
          <router-link to="/labelmanager"
            ><el-menu-item index="2-2"
              ><el-icon><price-tag /></el-icon>标签管理</el-menu-item
            ></router-link
          >
        </el-sub-menu>
        <el-menu-item index="3">
          <el-icon><user-filled /></el-icon>
          <span>Navigator Two</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <!-- </div> -->

    <el-main><router-view /></el-main>
  </el-container>
</template>

<script  lang="ts">
import { defineComponent } from "vue";
// import { Picture, Setting, Menu, Document } from "@element-plus/icons-vue";
// import { Picture, } from "@element-plus/icons-vue";
import {
  PictureFilled,
  List,
  PriceTag,
  UserFilled,
  HomeFilled,
} from "@element-plus/icons-vue";

// import { Edit } from "@element-plus/icons";

export default defineComponent({
  name: "Navigation",
  components: {
    PictureFilled,
    List,
    PriceTag,
    UserFilled,
    HomeFilled,
    // Picture,
    // Location
    // Aim
    // Setting,
    // Menu ,
    // Document
  },
  props: {
    // msg: String,
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* :root {
  --el-color-primary: #409eff;
  --el-color-success: #67c23a;
  --el-color-warning: #e6a23c;
  --el-color-danger: #f56c6c;
  --el-color-error: #f56c6c;
  --el-color-info: #909399;
} */
/* .common-layout .el-header,
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
} */

/* #nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
