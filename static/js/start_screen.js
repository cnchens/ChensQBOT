document.getElementById("screen_text").innerHTML="<p>简介简介简介</p>";

document.getElementById("section-1").onclick=function () {change_sc1()};
function change_sc1() {
    document.getElementById("screen_text").innerHTML="<p>简介简介简介</p>";
};

document.getElementById("section-2").onclick=function () {change_sc2()};
function change_sc2() {
    document.getElementById("screen_text").innerHTML="<p>安装安装安装</p>";
};

document.getElementById("section-3").onclick=function () {change_sc3()};
function change_sc3() {
    document.getElementById("screen_text").innerHTML="<p>JSON配置JSON配置JSON配置</p>";
};

document.getElementById("section-4").onclick=function () {change_sc4()};
function change_sc4() {
    document.getElementById("screen_text").innerHTML="<p>MongoDB配置MongoDB配置MongoDB配置</p>";
};