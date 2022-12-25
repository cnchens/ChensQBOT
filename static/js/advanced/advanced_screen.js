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
<p>前面几行在上一张已经讲过了，我们直接跳过，下表列出了剩余部分的配置方法</p>
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
            <td>notice_group_increase</td>
            <td>dictionary</td>
            <td>
                <pre class="prettyprint linenums code_screen">
{
    "enable" : "true", 
    "method" : "basic", 
    "notice_msg" : "欢迎新人欢迎入群"
}
                </pre>
            </td>
            <td>
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
                            <td>enable</td>
                            <td>str</td>
                            <td>true</td>
                            <td>
                                是否启用
                                <table class="table table-dark table-striped">
                                    <thead>
                                        <tr>
                                            <th>值名称</th>
                                            <th>值类型</th>
                                            <th>处理结果</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>true</td>
                                            <td>str</td>
                                            <td>启用</td>
                                        </tr>
                                        <tr>
                                            <td>false</td>
                                            <td>str</td>
                                            <td>停用</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td>method</td>
                            <td>str</td>
                            <td>basic</td>
                            <td>
                                发送类型（请勿更改）
                                <table class="table table-dark table-striped">
                                    <thead>
                                        <tr>
                                            <th>值名称</th>
                                            <th>值类型</th>
                                            <th>处理结果</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>basic</td>
                                            <td>str</td>
                                            <td>/</td>
                                        </tr>
                                        <tr>
                                            <td>special</td>
                                            <td>str</td>
                                            <td>/</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td>notice_msg</td>
                            <td>str</td>
                            <td>欢迎新人欢迎入群</td>
                            <td>
                                发送的欢迎消息
                                <table class="table table-dark table-striped">
                                    <thead>
                                        <tr>
                                            <th>值名称</th>
                                            <th>值类型</th>
                                            <th>处理结果</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>任意str类型数据</td>
                                            <td>str</td>
                                            <td>/</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>notice_group_decrease</td>
            <td>dictionary</td>
            <td>
                <pre class="prettyprint linenums code_screen">
{
    "enable" : "true"
}
                </pre>
            </td>
            <td>
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
                            <td>enable</td>
                            <td>str</td>
                            <td>true</td>
                            <td>
                                是否启用
                                <table class="table table-dark table-striped">
                                    <thead>
                                        <tr>
                                            <th>值名称</th>
                                            <th>值类型</th>
                                            <th>处理结果</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>true</td>
                                            <td>str</td>
                                            <td>启用</td>
                                        </tr>
                                        <tr>
                                            <td>false</td>
                                            <td>str</td>
                                            <td>停用</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>enable_allcmd</td>
            <td>str</td>
            <td>true</td>
            <td>
                是否启用显示本命令功能
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>值名称</th>
                            <th>值类型</th>
                            <th>处理结果</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>true</td>
                            <td>str</td>
                            <td>启用</td>
                        </tr>
                        <tr>
                            <td>false</td>
                            <td>str</td>
                            <td>停用</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>enable_time</td>
            <td>str</td>
            <td>true</td>
            <td>
                是否启用显示当前时间功能
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>值名称</th>
                            <th>值类型</th>
                            <th>处理结果</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>true</td>
                            <td>str</td>
                            <td>启用</td>
                        </tr>
                        <tr>
                            <td>false</td>
                            <td>str</td>
                            <td>停用</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>enable_finder</td>
            <td>str</td>
            <td>true</td>
            <td>
                是否启用查询各种数据功能
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>值名称</th>
                            <th>值类型</th>
                            <th>处理结果</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>true</td>
                            <td>str</td>
                            <td>启用</td>
                        </tr>
                        <tr>
                            <td>false</td>
                            <td>str</td>
                            <td>停用</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>enable_rdsfz</td>
            <td>str</td>
            <td>true</td>
            <td>
                是否启用随机身份证功能
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>值名称</th>
                            <th>值类型</th>
                            <th>处理结果</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>true</td>
                            <td>str</td>
                            <td>启用</td>
                        </tr>
                        <tr>
                            <td>false</td>
                            <td>str</td>
                            <td>停用</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>enable_tfish</td>
            <td>str</td>
            <td>true</td>
            <td>
                是否启用摸鱼功能
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>值名称</th>
                            <th>值类型</th>
                            <th>处理结果</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>true</td>
                            <td>str</td>
                            <td>启用</td>
                        </tr>
                        <tr>
                            <td>false</td>
                            <td>str</td>
                            <td>停用</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>enable_handrush</td>
            <td>str</td>
            <td>true</td>
            <td>
                是否启用是否手冲功能
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>值名称</th>
                            <th>值类型</th>
                            <th>处理结果</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>true</td>
                            <td>str</td>
                            <td>启用</td>
                        </tr>
                        <tr>
                            <td>false</td>
                            <td>str</td>
                            <td>停用</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>enable_rdsimg</td>
            <td>str</td>
            <td>true</td>
            <td>
                是否启用随机涩图功能
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>值名称</th>
                            <th>值类型</th>
                            <th>处理结果</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>true</td>
                            <td>str</td>
                            <td>启用</td>
                        </tr>
                        <tr>
                            <td>false</td>
                            <td>str</td>
                            <td>停用</td>
                        </tr>
                    </tbody>
                </table>
            </td>
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