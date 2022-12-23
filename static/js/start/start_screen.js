var inner_s1=`
<h2>简介</h2>
<hr>
<p>ChensBOT是基于Nonebot开发的一款机器人，整体上使用Python语言，以及MongoDB数据库进行数据的存取</p>
`

var inner_s2=`
<h2>安装</h2>
<hr>
<div class="alert alert-danger s2_alert1">注意：目前仅提供Windows x86_64系统的执行程序，需要适配其他系统请自行下载源码</div>
`

var inner_s3=`
inner_s3
`

var inner_s4=`
inner_s4
`

document.getElementById("screen_text").innerHTML=inner_s1;

document.getElementById("section-1").onclick=function () {change_sc1()};
function change_sc1() {
    document.getElementById("screen_text").innerHTML=inner_s1;
};

document.getElementById("section-2").onclick=function () {change_sc2()};
function change_sc2() {
    document.getElementById("screen_text").innerHTML=inner_s2;
};

document.getElementById("section-3").onclick=function () {change_sc3()};
function change_sc3() {
    document.getElementById("screen_text").innerHTML=inner_s3;
};

document.getElementById("section-4").onclick=function () {change_sc4()};
function change_sc4() {
    document.getElementById("screen_text").innerHTML=inner_s4;
};