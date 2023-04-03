<template>
    <div class="dataing-container">
        <div class="left box">
            <div class="one">
                <!-- <Year/> -->
                <iframe src="../../../../everyear.html"   frameborder="0" style="width: 100%; height: 450px"  id="iframeBox" allowfullscreen  ></iframe>
            </div>
            <!-- <div class="two">l
                <iframe src="../../../../品牌词云.html"   frameborder="0" style="width: 100%; height: 400px"  id="iframeBox" allowfullscreen  ></iframe>
 
            </div> -->
            <div class="three">
              <Ground/>
            </div>
        </div>
        <div class="middle box">
            <iframe src="../../../../品牌词云.html"   frameborder="0" style="width: 100%; height: 550px"  id="iframeBox" allowfullscreen  ></iframe>
           <div>
              <iframe src="../../../../热搜前20.html"   frameborder="0" style="width: 100%; height: 296px"  id="iframeBox" allowfullscreen  ></iframe>
           </div>
          
        </div>
        <div class="right box">
            <iframe src="../../../../评分分布.html"   frameborder="0" style="width: 100%; height: 450px"  id="iframeBox" allowfullscreen  ></iframe>
            <div>
                <img src="../../../../public/teaf.png" height="400px"> 
            </div>
        </div>
        
    </div>
  </template>

  <script>
  import Ground from './left/Ground.vue';
  import Year from './left/Year.vue'
  export default {
      components: { Ground, Year },
  };
</script>
  
<style scoped>
    .dataing-container {
        display: flex;
        
    }

    /* .box {
        width: 100px;
        height: 100px;
        background-color: #ac2929;
        margin-right: 10px;
    } */

    .left {
        display: inline-block;
        /* position: fixed; */
        height: 100%;
        width: 20%;
        background-color: rgb(85, 219, 108);
    }

    .middle {
        display: inline-block;
        
        height: 100%;
        width: 60%;
        background-color:#fff;
    }

    .right {
        display: inline-block;
        height: 100%;
        width: 20%;
        background-color: greenyellow;
    }
    
    .one {
       /* position: fixed; */
       /* height: ; */
       background-color: #fff;
    }
    .three{
        position: relative;
        left: 10px;
        height: 30%;
    }
</style>
  