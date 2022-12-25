inner_s1=`
<h2>本章简介</h2>
<hr>
<p>在这一个章节中，你将会学到ChensBOT的一些进阶操作（如果需要使用某些模块，请务必认证仔细看完这个章节）</p>
<p>以下是本章的大纲：</p>
<table class="table table-dark table-striped">
    <thead>
        <tr>
            <th>小节</th>
            <th>简介</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>JSON配置</td>
            <td>完整的config.json配置方法</td>
        </tr>
    </tbody>
</table>
`

inner_s2=`
<h2>JSON配置</h2>
<hr>
<p>打开config.json，它应该是这样的</p>
<pre class="prettyprint linenums code_screen">
{
    "mdb_conn" : "mongodb://127.0.0.1:27017/", 

    "superusers" : [1836178267], 
    "cmd_start" : [""], 
    "host" : "127.0.0.1", 
    "port" : "32808", 
    "api_root" : "http://127.0.0.1:32809", 

    "notice_group_increase" : {
        "enable" : "true", 
        "method" : "special", 
        "notice_msg" : ""
    }, 
    "notice_group_decrease" : {
        "enable" : "true"
    }, 

    "enable_allcmd" : "true", 
    "enable_time" : "true", 
    "enable_passwords" : "true", 
    "enable_finder" : "true", 
    "enable_rdsfz" : "true", 
    "enable_tfish" : "true", 
    "enable_handrush" : "true", 
    "enable_rdsimg" : "true"
}
</pre>
<p>前面几行在上一张已经讲过了，我们直接跳过，剩余部分的配置方法可以点击这个<a href="https://cnchens.github.io/ChensBOT/templates/advanced/advanced_sc2_table.html">链接</a></p>
`

var url=window.location.href;
var index=url.indexOf("flag");
if (index!=-1) {
    change_sc2()
} else {
    document.getElementById("screen_text").innerHTML=inner_s1;
}

document.getElementById("section-1").onclick=function () {change_sc1()};
function change_sc1() {
    document.getElementById("screen_text").innerHTML=inner_s1;
};

document.getElementById("section-2").onclick=function () {change_sc2()};
function change_sc2() {
    document.getElementById("screen_text").innerHTML=inner_s2;
};