<template>
  <div class="dataing-container">
    <div class="content">
        <div class="center">
        <el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>{{this.input }}</span>
  </div>
  <div  class="text item">
    
  </div>
</el-card>
        </div>
    </div>
    <div class="bottom">
      <el-input
        v-model="input"
        placeholder="请输入您遇到的问题（按Enter键提交问题）"
        class="input_question"
        @keyup.enter.native="onKeyDown"
      ></el-input>
      <el-button
        type="primary"
        circle
        icon="el-icon-s-promotion"
        class="send"
        @click="send_message"
      ></el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: "",
    };
  },
    methods: {
        onKeyDown() {
          this.send_message()  
        },
        send_message() {
            console.log(this.input)
        },
  },
};
</script>

<style scoped>
.dataing-container {
  display: flex;
  height: 900px;
  width: 1268.67px;
}

.bottom {
  position: fixed;
  bottom: 0;
  top: 900px;
  left: 35%;
  width: 100%;
}

.content {
    height: 900px;
  width: 1268.67px;
    display: flex;
  justify-content: center;
  /* align-items: center; */
}

.center {
    margin-top: 50px;
}
.send {
  margin-left: 20px;
}
.input_question {
  width: 500px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>
