var para=document.createElement("p");
var node=document.createTextNode("这是一个新段落。");
para.appendChild(node);
var element=document.getElementById("screen_text");
element.appendChild(para);

document.getElementById("section-1").onclick=function () {change_sc1()};
function change_sc1() {
    var para=document.createElement("p");
    var node=document.createTextNode("简介简介简介");
    para.appendChild(node);
    var element=document.getElementById("screen_text");
    element.appendChild(para);
};

document.getElementById("section-2").onclick=function () {change_sc2()};
function change_sc2() {
    var para=document.createElement("p");
    var node=document.createTextNode("安装安装安装");
    para.appendChild(node);
    var element=document.getElementById("screen_text");
    element.appendChild(para);
};

document.getElementById("section-2").onclick=function () {change_sc2()};
function change_sc2() {
    var para=document.createElement("p");
    var node=document.createTextNode("JSON配置JSON配置JSON配置");
    para.appendChild(node);
    var element=document.getElementById("screen_text");
    element.appendChild(para);
};

document.getElementById("section-2").onclick=function () {change_sc2()};
function change_sc2() {
    var para=document.createElement("p");
    var node=document.createTextNode("MongoDB配置MongoDB配置MongoDB配置");
    para.appendChild(node);
    var element=document.getElementById("screen_text");
    element.appendChild(para);
};