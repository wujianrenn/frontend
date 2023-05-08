<template>
    <div class="app-container">
      <div class="main-tea">
        <div class="left">
            <div class="boxf1">
            <div class="tit">
                <h2>好评</h2>
            </div>
            <div class="tea_item_xili">
                <p class="letter_fb">
                    <el-button id="xl1" class="next" @click="change1()">茶汤好</el-button>
                    <el-button id="xl2" class="next" @click="change2()">口感好</el-button>
                    <el-button id="xl3" class="next" @click="change3()">泡度好</el-button>
                    <el-button id="xl5" class="next" @click="change4()">品质好</el-button>
                    <el-button id="xl6" class="next" @click="change5()">汤色好</el-button>
                    <el-button id="xl7" class="next" @click="change6()">外形好</el-button>
                    <el-button id="xl8" class="next" @click="change7()">香气好</el-button>
                    <el-button id="xl9" class="next" @click="change8()">协调好</el-button>
                    <el-button id="xla" class="next" @click="change9()">叶底好</el-button>
                    <el-button id="xlc" class="next" @click="change10()">整体好</el-button>
                    <el-button id="xle" class="next" @click="change11()">原料好</el-button>
                    <el-button id="xlf" class="next" @click="change12()">滋味好</el-button>
                </p>
            </div>
            </div>
        </div>
        <div class="right">
            <div class="boxf1">
            <div class="tit">
                <h2>差评</h2>
            </div>
            <div class="tea_item_xili">
                <p class="letter_fb">
                    <el-button id="xl1" class="next" @click="change13()">茶汤差</el-button>
                    <el-button id="xl2" class="next" @click="change14()">口感差</el-button>
                    <el-button id="xl3" class="next" @click="change15()">泡度差</el-button>
                    <el-button id="xl5" class="next" @click="change16()">品质差</el-button>
                    <el-button id="xl6" class="next" @click="change17()">汤色差</el-button>
                    <el-button id="xl7" class="next" @click="change18()">外形差</el-button>
                    <el-button id="xl8" class="next" @click="change19()">香气差</el-button>
                    <el-button id="xl9" class="next" @click="change20()">协调差</el-button>
                    <el-button id="xla" class="next" @click="change21()">叶底差</el-button>
                    <el-button id="xlc" class="next" @click="change22()">整体差</el-button>
                    <el-button id="xle" class="next" @click="change23()">原料差</el-button>
                    <el-button id="xlf" class="next" @click="change24()">滋味差</el-button>
                </p>
            </div>
            </div>           
        </div>
        <div class="detail"> 
            <h2>提到原料的评价中有63%觉得原料差，共40条</h2>
        </div>
        <div class="boxf2">
          <div>
            <iframe src="../../../../../../../../input/观点之茶汤差.html"   frameborder="0" style="width: 100%; height: 640px"  id="iframeBox" allowfullscreen  ></iframe>
        </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  // a1.onclick = function() {
  //   // iframeBox.setAttribute('src', './')
  //   alert('asd')
  // }
  
export default {
data() {
    return {
    fileData: '',
    analysisResults: '',
    visible: false
    }
},
methods: {
        // 细粒度
        change1() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之茶汤好.html')
        },
        change2() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之口感好.html')
        },
        change3() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之泡度好.html')
        },
        change4() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之品质好.html')
        },
        change5() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之汤色好.html')
        },
        change6() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之外形好.html')
        },
        change7() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之香气好.html')
        },
        change8() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之协调好.html')
        },
        change9() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之叶底好.html')
        },
        change10() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之整体好.html')
        },
        change11() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之原料好.html')
        },
        change12() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之滋味好.html')
        },


        change13() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之滋味差.html')
        },
        change14() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之口感差.html')
        },
        change15() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之泡度差.html')
        },
        change16() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之品质差.html')
        },
        change17() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之汤色差.html')
        },
        change18() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之外形差.html')
        },
        change19() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之香气差.html')
        },
        change20() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之协调差.html')
        },
        change21() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之叶底差.html')
        },
        change22() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之整体差.html')
        },
        change23() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之原料差.html')
        },
        change24() {
            var iBox = document.getElementById('iframeBox')
            iBox.setAttribute('src', '../../../../input/观点之滋味差.html')
        },
    }
}
</script>
  
<style scoped>

    .left {
        display: inline-block;
        width: 50%;
    }
    
    .right {
        display: inline-block;
        width: 50%;
    }

    .next {
        margin: 5px;
    }
    .main-tea{
        background-color:rgba(233, 228, 214, 0.24);
    }
    .tit{
        color: green;
    }
    .boxf1{
        /* background-color: aquamarine; */
    }
    .letter_fb{
        color:gray;
        font-size: small;
        position: relative;
        /* left: 50px; */
    }
    .i1:hover{color:darkgoldenrod}

    .boxf2{
        /* background-color: burlywood; */
        height: 600px;
    }
    a {
        color:#444;
        text-decoration:none;
        font-size:12px;
        letter-spacing: 3px;
        margin: 5px;
    }
    /*a:link,a:visited{color:#999;}*/
    a:hover{
        color:#569091;
        color:#c19450;
        color:#c0501f;
    }
</style>

