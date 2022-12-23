var inner_s1=`
<h2>简介</h2>
<hr>
<p>ChensBOT是基于Nonebot开发的一款机器人，整体上使用Python语言，以及MongoDB数据库进行数据的存取</p>
`

var inner_s2=`
<h2>安装</h2>
<hr>
<div class="alert alert-danger s2_alert">注意：目前仅提供Windows x86_64系统的执行程序，需要适配其他系统请自行下载源码</div>
<span>
    <p>在安装前请确认已经配置好</p>
    <strong>Python3.7+</strong>
    <p>和</p>
    <strong>MongoDB</strong>
    <p>环境</p>
</span>
<span>
    <p>在</p>
    <a href="https://github.com/cnchens/ChensBOT/releases">Releases</a>
    <p>中下载最新的压缩包并解压</p>
</span>
<span>
    <p>如果不需要额外配置的话，首先运行</p>
    <strong>modinstall.bat</strong>
    <p>等待安装完成</p>
</span>
<span>
    <p>然后分别运行</p>
    <strong>pystart.bat</strong>
    <p>和</p>
    <strong>cqstart.bat</strong>
</span>
<div class="alert alert-warning s2_alert">
    <p>
        首次运行会导入数据库，请确保你的MongoDB配置正确（连接时使用默认ip和端口，如果你修改过这两项内容请先往下看）
        导入完成会有提示，请勿在导入时关闭程序（如果不小心关闭了，请删除整个数据库重新导入）
    </p>
</div>
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