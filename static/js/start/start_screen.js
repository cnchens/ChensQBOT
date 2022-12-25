var inner_s1=`
<h2>简介</h2>
<hr>
<p>ChensBOT是基于Nonebot开发的一款机器人，整体上使用Python语言，以及MongoDB数据库进行数据的存取</p>
`

var inner_s2=`
<h2>安装</h2>
<hr>
<p><div class="alert alert-danger alert_div">注意：目前仅提供Windows x86_64系统的执行程序，需要适配其他系统请自行下载源码</div></p>
<p>在安装前请确认已经配置好Python3.7+和MongoDB环境，在<a href="https://github.com/cnchens/ChensBOT/releases">Releases</a>中下载最新的压缩包并解压</p>
<p>确保你的pip配置正确，运行modinstall.bat，等待安装完成，进入下一步</p>
`

var inner_s3=`
<h2>JSON配置</h2>
<hr>
<p>本小节只会介绍部分JSON配置的方法，完整版请至<a href="https://cnchens.github.io/ChensBOT/templates/advanced.html">进阶</a>查看</p>
<p>打开config.json（在根目录中），有以下几行代码需要特别注意：</p>
<pre class="prettyprint linenums code_screen">
    "mdb_conn" : "mongodb://127.0.0.1:27017/", 

    "superusers" : [114514], 
    "cmd_start" : [""], 
    "host" : "127.0.0.1", 
    "port" : "32808", 
    "api_root" : "http://127.0.0.1:32808", 
</pre>
<p>这几行的配置方法在下表中已经列出来了</p>
<table class="table table-dark table-striped">
    <thead>
        <tr>
            <th>键名称</th>
            <th>值类型</th>
            <th>值默认数据</th>
            <th>备注</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>mdb_conn</td>
            <td>str</td>
            <td>mongodb://127.0.0.1:27017/</td>
            <td>MongoDB连接url</td>
        </tr>
        <tr>
            <td>superusers</td>
            <td>list</td>
            <td>空</td>
            <td>超级用户</td>
        </tr>
        <tr>
            <td>cmd_start</td>
            <td>list</td>
            <td>空</td>
            <td>命令起始字符</td>
        </tr>
        <tr>
            <td>host</td>
            <td>str</td>
            <td>127.0.0.1</td>
            <td>go-cqhttp连接ip</td>
        </tr>
        <tr>
            <td>port</td>
            <td>str</td>
            <td>32808</td>
            <td>go-cqhttp连接端口</td>
        </tr>
        <tr>
            <td>api_root</td>
            <td>str</td>
            <td>http://127.0.0.1:32809</td>
            <td>nonebot_api连接url</td>
        </tr>
    </tbody>
</table>
`

var inner_s4=`
inner_s4
`

var inner_s5=`
inner_s5
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

document.getElementById("section-5").onclick=function () {change_sc5()};
function change_sc5() {
    document.getElementById("screen_text").innerHTML=inner_s5;
};
