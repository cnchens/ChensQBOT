inner_s1=`
<h2>本章简介</h2>
<hr>
<p>在这一章中，我会详细讲解每一个命令的用法，这对开发者和使用者都很重要</p>
<div class="alert alert-danger alert_div">其中某些命令需要输入很多数据，对输入的顺序有要求，所以请仔细阅读</div>
`

inner_s2=`
<h2>要了解的基本语法</h2>
<hr>
<p>根据nonebot api，指令的发送可以分为以下两种情形</p>
<strong>私聊界面：[指令开始字符] 指令内容</strong>
<strong>群聊界面：@[机器人名称] [指令开始字符] 指令内容</strong>
<p>为了适应大众的需求，以下演示将在群聊中进行（私聊指令去除前面的at字段即可，是否需要添加指令开始字符需参考config.json）</p>
<p>如果没有配置指令开始字符（默认配置为空），就可以直接忽略，示例：群聊界面：@[机器人名称] 指令内容</p>
<div class="alert alert-danger alert_div">
    <strong>以下是本章中出现的一些特殊字符（如你已经掌握，可以跳过）</strong>
    <p>cq码的使用，请至<a href="https://docs.go-cqhttp.org/cqcode/#%E8%BD%AC%E4%B9%89">go-cqhttp 帮助中心 -&gt; CQ 码 / CQ Code</a>查看</p>
    <p>Python常见转义字符：\n 代表换行符；\t 代表横向跳格；\\ 代表反斜杠；\" 代表双引号；\' 代表单引号；\r代表回车；\b代表退格</p>
    <p>pytz日期转义字符：%Y = 年， %m = 月， %d = 日， %H = 时， %M = 分， %S = 秒</p>
    <p>ChensBOT自定义变量：req_qid = 执行本命令的用户QQ号</p>
</div>
`

inner_s3=`
<h2>allcmd</h2>
<hr>
<img src="https://cnchens.github.io/ChensBOT/static/image/to_users/allcmd.png" class="img-fluid" alt="allcmd.png">
<br>
<h5>群聊指令：@[机器人名称] [指令开始字符] allcmd</h5>
<br>
<p>返回值</p>
<table class="table table-dark table-striped">
    <thead>
        <tr>
            <th>传入指令</th>
            <th>传入类型</th>
            <th>返回值</th>
            <th>返回类型</th>
            <th>备注</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>allcmd</td>
            <td>str</td>
            <td>当前所有可用指令（版本不同，可用的指令也会不同）</td>
            <td>str</td>
            <td>/</td>
        </tr>
    </tbody>
</table>
`

inner_s4=`
<h2>time</h2>
<hr>
<img src="https://cnchens.github.io/ChensBOT/static/image/to_users/time.png" class="img-fluid" alt="time.png">
<br>
<h5>群聊指令：@[机器人名称] [指令开始字符] time</h5>
<br>
<p>返回值</p>
<table class="table table-dark table-striped">
    <thead>
        <tr>
            <th>传入指令</th>
            <th>传入类型</th>
            <th>返回值</th>
            <th>返回类型</th>
            <th>备注</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>time</td>
            <td>str</td>
            <td>[CQ:at,qq={req_qid}]当前GMT+8 Time是：\n%Y-%m-%d %H:%M:%S</td>
            <td>str</td>
            <td>/</td>
        </tr>
    </tbody>
</table>
`

inner_s5=`
<h2>finder</h2>
<hr>
<img src="https://cnchens.github.io/ChensBOT/static/image/to_users/finder.png" class="img-fluid" alt="finder.png">
<br>
<h5>群聊指令：@[机器人名称] [指令开始字符] finder &lt;MODE&gt; &lt;INFO&gt;</h5>
<br>
<p>MODE：查找模式（必需）</p>
<table class="table table-dark table-striped">
    <thead>
        <tr>
            <th>传入参数</th>
            <th>传入类型</th>
            <th>备注</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>q2p</td>
            <td>str</td>
            <td>通过QQ号查询密保手机</td>
        </tr>
        <tr>
            <td>p2q</td>
            <td>str</td>
            <td>通过密保手机查询QQ号</td>
        </tr>
        <tr>
            <td>q2l</td>
            <td>str</td>
            <td>QQ号查询LOL信息</td>
        </tr>
        <tr>
            <td>l2q</td>
            <td>str</td>
            <td>LOL查询QQ信息</td>
        </tr>
        <tr>
            <td>q2pwd</td>
            <td>str</td>
            <td>QQ号查询老密</td>
        </tr>
        <tr>
            <td>w2p</td>
            <td>str</td>
            <td>微博通过ID查手机号</td>
        </tr>
        <tr>
            <td>p2w</td>
            <td>str</td>
            <td>微博通过手机号查ID</td>
        </tr>
        <tr>
            <td>sms</td>
            <td>str</td>
            <td>短轰</td>
        </tr>
    </tbody>
</table>
<p>INFO：要查询的信息（必需）</p>
<table class="table table-dark table-striped">
    <thead>
        <tr>
            <th>传入参数</th>
            <th>传入类型</th>
            <th>备注</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>一般为QID， 手机号， LOL名称或微博ID</td>
            <td>str</td>
            <td>/</td>
        </tr>
    </tbody>
</table>
<br>
<p>返回值</p>
<table class="table table-dark table-striped">
    <thead>
        <tr>
            <th>传入指令</th>
            <th>传入类型</th>
            <th>返回值</th>
            <th>返回类型</th>
            <th>备注</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>finder q2p &lt;INFO&gt;</td>
            <td>str</td>
            <td>查询到的数据或查询失败</td>
            <td>str</td>
            <td>/</td>
        </tr>
        <tr>
            <td>finder p2q &lt;INFO&gt;</td>
            <td>str</td>
            <td>查询到的数据或查询失败</td>
            <td>str</td>
            <td>/</td>
        </tr>
        <tr>
            <td>finder q2l &lt;INFO&gt;</td>
            <td>str</td>
            <td>查询到的数据或查询失败</td>
            <td>str</td>
            <td>/</td>
        </tr>
        <tr>
            <td>finder l2q &lt;INFO&gt;</td>
            <td>str</td>
            <td>查询到的数据或查询失败</td>
            <td>str</td>
            <td>/</td>
        </tr>
        <tr>
            <td>finder q2pwd &lt;INFO&gt;</td>
            <td>str</td>
            <td>查询到的数据或查询失败</td>
            <td>str</td>
            <td>/</td>
        </tr>
        <tr>
            <td>finder w2p &lt;INFO&gt;</td>
            <td>str</td>
            <td>查询到的数据或查询失败</td>
            <td>str</td>
            <td>/</td>
        </tr>
        <tr>
            <td>finder p2w &lt;INFO&gt;</td>
            <td>str</td>
            <td>查询到的数据或查询失败</td>
            <td>str</td>
            <td>/</td>
        </tr>
        <tr>
            <td>finder sms &lt;INFO&gt;</td>
            <td>str</td>
            <td>/</td>
            <td>/</td>
            <td>暂时停用</td>
        </tr>
    </tbody>
</table>
`

inner_s6=`
<h2>rdsfz</h2>
<hr>
<img src="https://cnchens.github.io/ChensBOT/static/image/to_users/rdsfz.png" class="img-fluid" alt="rdsfz.png">
<br>
<h5>群聊指令：@[机器人名称] [指令开始字符] rdsfz</h5>
<br>
<p>返回值</p>
<table class="table table-dark table-striped">
    <thead>
        <tr>
            <th>传入指令</th>
            <th>传入类型</th>
            <th>返回值</th>
            <th>返回类型</th>
            <th>备注</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>rdsfz</td>
            <td>str</td>
            <td>随机返回一个身份证信息</td>
            <td>str</td>
            <td>/</td>
        </tr>
    </tbody>
</table>
`

inner_s7=`
<h2>tfish</h2>
<p>此命令即将停用</p>
`

inner_s8=`
<h2>handrush</h2>
<p>此命令即将更名</p>
`

inner_s9=`
<h2>rdsimg</h2>
<hr>
<img src="https://cnchens.github.io/ChensBOT/static/image/to_users/allcmd.png" class="img-fluid" alt="allcmd.png">
<br>
<h5>群聊指令：@[机器人名称] [指令开始字符] rdsimg</h5>
<br>
<p>返回值</p>
<table class="table table-dark table-striped">
    <thead>
        <tr>
            <th>传入指令</th>
            <th>传入类型</th>
            <th>返回值</th>
            <th>返回类型</th>
            <th>备注</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>rdsimg</td>
            <td>str</td>
            <td>返回一张涩图</td>
            <td>image</td>
            <td>/</td>
        </tr>
    </tbody>
</table>
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

document.getElementById("section-6").onclick=function () {change_sc6()};
function change_sc6() {
    document.getElementById("screen_text").innerHTML=inner_s6;
};

document.getElementById("section-7").onclick=function () {change_sc7()};
function change_sc7() {
    document.getElementById("screen_text").innerHTML=inner_s7;
};

document.getElementById("section-8").onclick=function () {change_sc8()};
function change_sc8() {
    document.getElementById("screen_text").innerHTML=inner_s8;
};

document.getElementById("section-9").onclick=function () {change_sc9()};
function change_sc9() {
    document.getElementById("screen_text").innerHTML=inner_s9;
};
