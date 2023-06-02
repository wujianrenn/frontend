<template>
    <div class="app-container one">
      <el-image
        style="width: 100%; height: 100%; position: absolute; z-index: -1;"
        :src="url"
      />
        <!-- 画布 -->
      <canvas ref="canvas"></canvas>

      <!-- 按钮 -->
      <el-row class="buttons">
          <el-col :span="8">
              <el-button type="success" class="button"  circle round @click="$router.push('/view/fine_grained')"><h2>细粒度情感倾向可视化</h2></el-button>
          </el-col>
          <el-col :span="8">
              <el-button type="success" class="button"  circle round @click="$router.push('/view/dataing')"><h2>数据分析可视化</h2></el-button>
          </el-col>
          <el-col :span="8">
              <el-button type="success" class="button"  circle round @click="$router.push('/view/clustering')"><h2>聚类效果可视化</h2></el-button>
          </el-col>
      </el-row>
  </div>
</template>
  
  <script>
  export default {
    data() {
    return {
      url: require('../../../public/主页/主页图4.jpg')
    }
  },
    mounted() {
      this.initCanvas();
    },
    methods: {
      initCanvas() {
        // 创建画布
        const canvas = this.$refs.canvas;
        const ctx = canvas.getContext("2d");
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        // 定义三角形顶点坐标和颜色
        const triangleVertices = [
          { x: canvas.width / 2 - 30 , y: 300 },
          { x: canvas.width / 2 - 200, y: canvas.height - 400 },
          { x: canvas.width / 2 + 200, y: canvas.height - 400 },
        ];
  
        // 绘制三角形边框
        ctx.beginPath();
        ctx.moveTo(triangleVertices[0].x, triangleVertices[0].y);
        triangleVertices.forEach((vertex) => {
          ctx.lineTo(vertex.x, vertex.y);
        });
        ctx.closePath();
        ctx.lineWidth = 2;
        ctx.strokeStyle = "green";
        ctx.stroke();
  
        // 将按钮移到对应位置
        const buttons = document.querySelectorAll(".button");
        buttons.forEach((button, i) => {
          const pos = triangleVertices[i];
          button.style.top = `${pos.y}px`;
          button.style.left = `${pos.x}px`;
        });
      },
    },
  };
  </script>
  
<style scoped>
    .top {
        position: relative;
        top: 100px;
        left: 10%;
    }

    .left {
        position: relative;
        top: 320px;
        right: 70%;
    }

    /* .right {
        position: relative;
        top: 30px;
    } */


    one {
        margin: 0;
        padding: 0;
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        /* background-color: rgb(240, 176, 138); */
      }

      .row {
        display: flex;
        height: 50%;
        /* flex: 1; */
      }

      .col {
        flex: 1;
        border: none; /* 取消边框框线 */
        /* display: flex;s */
        align-items: center;
        justify-content: censter;
        filter: blur(2px);
        height: 100%;
        width: 100%;
      }

      #top-left {
        height: 500px;
      }

      canvas {
            position: absolute;
            top: 0;
            left: 0;
            /* background-color: rgb(233, 200, 181); */
            /* background-color: rgb(250, 249, 245); */
            /* background-color: gold; */
            z-index: -1; /* 将画布放在容器底部 */
        }
.buttons {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.button {
  position: absolute;
  transform: translate(-50%, -50%);
  height: 70px;
  width: 260px;
  border-radius: 20px; /* 减小圆角 */
}

#top-right {
    position: relative;
    left: 100px;
}

#bottom-left {
    position: relative;
    top: 90px;
    left: 10px;
    width: 20px;
}

#bottom-right {
    position: relative;
    top: 90px;
    left: 100px;
}

/* .middle {
    justify-content: center;
    align-items: center;
    height: 1px;
    width: 3px;
} */

.top {
        display: inline-block;
        
        height: 100%;
        width: 50%;
        background-color:#fff;
    }

    .right {
        display: inline-block;
        height: 100%;
        width: 50%;
        /* background-color: greenyellow; */
    }
</style>
  