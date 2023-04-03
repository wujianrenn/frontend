<template>
    <div class="dataing-container">
       
        <div class="middle box">
            <!-- <iframe src="../../../../../clustering_png/lda主题数寻优.png"   frameborder="0" style="width: 100%; height: 500px"  id="iframeBox" allowfullscreen  ></iframe> -->
           <img src="../../../../public/clustering_png/lda主题数寻优.png" style="width: 610px;" height="450px">
            <div>
              <iframe src="../../../../clustering_png/tea总评关键词聚类后种类0.html"   frameborder="0" style="width: 100%; height: 450px"  id="iframeBox" allowfullscreen  ></iframe>
           </div>
          
        </div>
        <div class="right box">
            <iframe src="../../../../clustering_png/tea总评关键词聚类后种类1.html"   frameborder="0" style="width: 100%; height: 450px"  id="iframeBox" allowfullscreen  ></iframe>
            <div>
                <iframe src="../../../../clustering_png/tea总评关键词聚类后种类2.html"   frameborder="0" style="width: 100%; height: 450px"  id="iframeBox" allowfullscreen  ></iframe>
            </div>
        </div>
        
    </div>
  </template>

  <script>
  export default {
      
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

   
    .middle {
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
  