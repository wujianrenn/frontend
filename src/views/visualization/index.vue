<template>
    <div class="app-container">

      <el-row style="text-align: center; padding-top:20px;padding-bottom:20px;height: 880px;background-color: blueviolet;">
        <el-button type="primary"  class="top" round @click="$router.push('/view/fine_grained')">细粒度情感主题可视化</el-button>
        <el-button type="success"  class="left" round @click="$router.push('/view/dataing')">数据分析可视化</el-button>
        <el-button type="success"  class="right" round @click="$router.push('/view/clustering')">聚类效果可视化</el-button>
      </el-row>

    </div>
  </template>
  
<script>
    export default {
        data() {
                return {
                    fileData: '',
                    analysisResults: '',
                    visible: false
                }
        },
        methods: {
        }
    }
</script>
  
<style scoped>
    .top {
        position: relative;
        top: 100px;
        left: 10%;
    }

    .left {
        position: relative;
        top: 400px;
        right: 20%;
    }

    .right {
        position: relative;
        top: 400px;
    }
</style>
  