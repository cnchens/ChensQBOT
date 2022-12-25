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
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>
`

inner_s2=`

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