#!/usr/bin/env python3
#coding=utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
# from email.mime.multipart import MIMEMultipart

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = '18271676080@163.com'
password = 'FBLATPX4869'
to_addr = '846058904@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('''
     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=gbk"></meta></head><body><style>
          html,body,div,p{margin:0;padding:0}
          body{font-size:14px;font-family:"microsoft yahei";background-color:#ffffff}
          table{border-collapse:collapse;border-spacing:0;table-layout:fixed}
          th,td{font-size:14px;padding:0}
          a{text-decoration:none}
          img{border:0 none}
          .blue{text-decoration:none;color:#3c3d5d}
          .chead{width:1002px}
          .chead .logo{width:698px;height:90px}
          .chead .txt{width:152px;height:90px}
          .column{width:1002px;line-height:28px;border:1px solid #dedede}
          .column .hbox{width:185px;height:154px}
          .column .head{display:block;background-color:#fafafa}
          .column .box{width:100%;background-color:#ffffff;border-top:2px solid #f2f3f5}
          .column .box1{width:100%;word-wrap:break-word;color:#ffffff;background-color:#3f4160}
          .column .box2{width:100%;background-color:#f8f9fa}
          .column .tba{width:940px;padding:0 30px 15px}
          .column .tbb{width:940px;padding:0 30px}
          .column .tb1{width:900px;line-height:28px;color:#333333;word-break:break-all;padding:0 20px}
          .column .tb2{width:430px;padding:0 20px}
          .column .tb3{width:900px;padding:15px 20px 15px 0}
          .column .gray,.column .gray2{color:#999999;word-break:break-all}
          .column .gray2{color:#666666}
          .column .plate1,.column .plate2{width:430px;height:54px;font-size:16px;font-weight:bold;color:#818ba3}
          .column .plate1{width:900px;padding:0 50px}
          .column .plate1 .f16{font-size:14px;font-weight:normal;color:#333333}
          .column .plate1 .f12{font-size:12px;font-weight:normal;color:#999999}
          .column .keys,.column .keys2{width:85px;line-height:28px;color:#666666}
          .column .keys2{width:110px}
          .column .txt1,.column .txt2,.column .txt3{width:815px;line-height:28px;color:#333333;word-break:break-all}
          .column .txt2{width:345px}
          .column .txt3{width:auto;max-width:815px;font-size:14px;font-weight:bold}
          .column .txt4{width:305px;color:#ffffff;word-break:break-all}
          .column .infr{width:767px;color:#ffffff;table-layout:auto}
          .column .vam,.column .grcha{vertical-align:middle;margin-left:5px}
          .column .box1 .vam{margin-right:5px;margin-left:0}
          .column .name{font-size:24px;padding-bottom:18px}
          .column .icard{color:#a1a3ae;padding-bottom:18px}
          .column .con{border-top:1px dotted #ddd}
          .column .pr20{width:225px;padding-right:20px}
          .column .time{width:120px;line-height:28px;color:#666666;padding-left:20px}
          .column .rtbox{width:765px;line-height:28px;color:#333333;padding:0 20px 0 15px;word-break:break-all}
          .column .hai,.column .guan{line-height:18px;font-size:12px;color:#ffffff;vertical-align:text-top;margin-left:5px;padding:1px 3px;background-color:#3cbe7f;border-radius:2px}
          .column .guan{background-color:#ff9f20}
          .column .tag{display:inline-block;word-break:break-all;#display:inline;#zoom:1}
          .column .all{color:#666;padding:10px 20px;background-color:#fafafa}
          .column .tit{width:900px;height:40px;color:#666666;padding:0 20px;background-color:#f5f5f5}
          .column .p15{padding:15px 0}
          .column .p5{display:inline-block;color:#666666;padding:0 5px;#display:inline;#zoom:1}
          .column .cell .skill{width:165px;text-align:right;padding-right:15px}
          .column .cell .skbg,.column .cell .skco{display:inline-block;width:245px;height:18px;line-height:18px;font-size:12px;color:#ffffff;vertical-align:top;margin-top:6px;background-color:#dddddd;border-radius:20px;#display:inline;#zoom:1}
          .column .cell .skco{width:235px;font-style:normal;margin-top:0;padding-left:10px;background-color:#ff9f20;z-index:3}
          .column .sl .skco{width:173px}
          .column .lh .skco{width:112px}
          .column .yb .skco{width:51px}
          .column .fbox strong{font-size:14px;font-weight:bold}
          .column .cha{font-size:12px;font-weight:normal;color:#00457d;margin-left:5px}
          .column .cha:hover{color:#ff6000}
          .column .email{width:330px}

          .eng td,.eng .txt3,.eng .fbox strong{font-size:13px;font-family:'Arial'}
          .eng .txt1,.eng .rtbox,.eng .phd{width:775px;font-size:13px;font-family:'Arial';line-height:28px}
          .eng .txt2{width:305px}
          .eng .txt4{width:245px}
          .eng .cell .txt3{width:120px}
          .eng .time,.eng .keys{width:110px;font-size:13px;text-align:right}
          .eng .cell .skill{width:130px}
          .eng .phd{padding-left:145px}
          .eng .keys{padding-right:15px}
          .eng .pr20{width:205px}
          .eng .pr20 .keys{width:100px}
          .eng .email{width:270px}
        </style><table cellpadding="0" cellspacing="0" align="center" bgcolor="#fff" class="column"><tbody><tr><td valign="top"><table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box1"><tbody><tr>
<td class="hbox" align="middle"><img src="http://i.51job.com/resume/ajax/image.php?type=avatar&amp;userid=377422576&amp;key=70a0980dedcb928016a1bd3f1b236c30" width="85" height="104" class="head" alt="头像"></td>
<td><table cellspacing="0" cellpadding="0" border="0" class="infr"><tbody>
<tr>
<td colspan="2" class="name">范炳林</td>

</tr>
<tr>
<td valign="top">
<img class="vam" src="http://img01.51jobcdn.com/im/2016/resume/y1.png" width="20" height="20">目前正在找工作</td>
<td valign="top">
<img class="vam" src="http://img01.51jobcdn.com/im/2016/resume/y2.png" width="20" height="20">18271676080</td>
<td valign="top"><table cellspacing="0" cellpadding="0" border="0" class="email"><tbody><tr>
<td valign="top" width="25"><img class="vam" src="http://img01.51jobcdn.com/im/2016/resume/y3.png" width="20" height="20"></td>
<td valign="top" class="txt4"><a href = "mailto:18271676080@163.com"  text-decoration="none">18271676080@163.com</a></td>
</tr></tbody></table></td>
</tr>
<tr><td valign="top" colspan="3"><p><img class="vam" src="http://img01.51jobcdn.com/im/2016/resume/y4.png" width="20" height="20">男<span class="p5">|</span>25 岁 (1992/12/28)<span class="p5">|</span>现居住广州-天河区<span class="p5">|</span>2年工作经验
                    </p></td></tr>
</tbody></table></td>
</tr></tbody></table>
<table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box2"><tbody><tr><td class="tba"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="tb2"><table cellspacing="0" cellpadding="0" border="0">
<thead style="height:0"><tr>
<td valign="top" class="keys"></td>
<td valign="top" class="txt2"></td>
</tr></thead>
<tbody>
<tr><td colspan="2" class="plate2">最近工作</td></tr>
<tr>
<td valign="top" class="keys">职位：</td>
<td valign="top" class="txt2">主管工程师-HW</td>
</tr>
<tr>
<td valign="top" class="keys">公司：</td>
<td valign="top" class="txt2"><a href = "http://www.isoftstone.com/" target = _blank>深圳软通动力技术有限公司</a></td>
</tr>
<tr>
<td valign="top" class="keys">行业：</td>
<td valign="top" class="txt2">计算机软件</td>
</tr>
</tbody>
</table></td>
<td valign="top" class="tb2"><table cellspacing="0" cellpadding="0" border="0">
<thead style="height:0"><tr>
<td valign="top" class="keys"></td>
<td valign="top" class="txt2"></td>
</tr></thead>
<tbody>
<tr><td colspan="2" class="plate2">最高学历/学位</td></tr>
<tr>
<td valign="top" class="keys">专业：</td>
<td valign="top" class="txt2">机械设计制造及其自动化</td>
</tr>
<tr>
<td valign="top" class="keys">学校：</td>
<td valign="top" class="txt2"><a href = "http://www.hbpu.edu.cn/" target = _blank>湖北理工学院</a></td>
</tr>
<tr>
<td valign="top" class="keys">学历/学位：</td>
<td valign="top" class="txt2">本科</td>
</tr>
</tbody>
</table></td>
</tr></tbody></table></td></tr></tbody></table>
<table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box"><tbody>
<tr><td class="plate1">个人信息</td></tr>
<tr><td class="tba"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">QQ号：
                                  </td>
<td valign="top" class="txt2">846058904</td>
</tr></tbody></table></td>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">户口/国籍：</td>
<td valign="top" class="txt2"><a href = "https://baike.baidu.com/item/%E8%95%B2%E6%98%A5%E5%8E%BF/2782567?fr=aladdin" target = _blank>湖北省黄冈市蕲春县</a></td>
</tr></tbody></table></td>
</tr>
<tr>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">身高：</td>
<td valign="top" class="txt2">172cm</td>
</tr></tbody></table></td>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">婚姻状况：</td>
<td valign="top" class="txt2">未婚</td>
</tr></tbody></table></td>
</tr>
<tr>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">博客主页：</td>
<td valign="top" class="txt2"><a href = "https://blog.csdn.net/qq_37608398" target = _blank>https://blog.csdn.net/qq_37608398</a></td>
</tr></tbody></table></td>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">个人主页：</td>
<td valign="top" class="txt2"><a href = "http://www.fanbinglin.com" target = _blank>http://www.fanbinglin.com</a></td>
</tr></tbody></table></td>
</tr>
</tbody></table></td></tr>
</tbody></table>
<table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box"><tbody><tr><td class="plate1">
              目前年收入
              <span>&nbsp;12万元</span><span class="f12">（包含基本工资、补贴、奖金、股权收益等）</span>
</td></tr></tbody></table>
<table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box"><tbody>
<tr><td class="plate1">求职意向</td></tr>
<tr><td class="tba"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0">
<thead style="height:0"><tr>
<td valign="top" class="keys"></td>
<td valign="top" class="txt1"></td>
</tr></thead>
<tbody><tr>
<td valign="top" class="keys">个人标签：</td>
<td valign="top" class="txt1">
<span class="tag">pyhon爬虫&nbsp;&nbsp;</span><span class="tag">Django&nbsp;&nbsp;</span><span class="tag">C/C++&nbsp;&nbsp;</span><span class="tag">Linux</span>
</td>
</tr></tbody>
</table></td></tr>
<tr>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">期望薪资：</td>
<td valign="top" class="txt2">13000-16000
                                            元/月
                                          </td>
</tr></tbody></table></td>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">地点：</td>
<td valign="top" class="txt2"><span class="tag">广州</span></td>
</tr></tbody></table></td>
</tr>
<tr>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">职能/职位：</td>
<td valign="top" class="txt2">
<span class="tag">软件工程师
</span><span class="tag">&nbsp;&nbsp;Python开发工程师</span>
</td>
</tr></tbody></table></td>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">行业：</td>
<td valign="top" class="txt2"><span class="tag">计算机软件</span></td>
</tr></tbody></table></td>
</tr>
<tr>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">到岗时间：</td>
<td valign="top" class="txt2">随时</td>
</tr></tbody></table></td>
<td class="tb2" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">工作类型：</td>
<td valign="top" class="txt2">全职</td>
</tr></tbody></table></td>
</tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0">
<thead style="height:0"><tr>
<td valign="top" class="keys"></td>
<td valign="top" class="txt1"></td>
</tr></thead>
<tbody><tr>
<td valign="top" class="keys">自我评价：</td>
<td valign="top" class="txt1">1、有2年以上实际项目相关工作经验，擅长Python爬虫、Django框架Web编程，熟悉BeautifulSoup、requests、xlrd、xlwt、lxml、PyMySQL库，对面向对象、函数式编程、MVC设计模式有深刻理解，良好的PEP8编程习惯，熟练掌握C/C++、<a  href = "https://baike.baidu.com/item/DOS%E5%91%BD%E4%BB%A4/5143255?fr=aladdin" target = _blank>DOS</a>/Shell脚本，Microsoft&#x20;excel的<a href = "https://baike.baidu.com/item/VBA/1596798?fr=aladdin" target = _blank>VBA</a>数据处理；<br>2、熟练掌握HTML5+CSS3+JavaScript编写网页，熟悉xml，json；<br>3、熟练掌握标准SQL语句，熟悉MySQL，Sqlite数据库；<br>4、熟练掌握linux命令，能用Ubuntu系统进行开发，熟悉vim、Sublime、Notepad++编辑器，熟悉Visual&#x20;Studio&#x20;2017开发环境，熟练运用Git、SVN管理源代码，良好的Code&#x20;Review习惯；<br>5、熟悉TCP/IP协议，了解Radius、Diameter、SS7协议；<br>6、活跃于Github、<a href = "https://blog.csdn.net/qq_37608398" target = _blank>CSDN</a>等开源社区，经常与其他人一起探讨技术问题，在<a href = "https://blog.csdn.net/qq_37608398" target = _blank>CSDN</a>博客上分享自己在编程中遇到的问题、解决办法以及经验总结；<br>7、熟练操作服务器，有自己的阿里云服务器，能快速解决服务器常见问题；<br>8、善于分析代码并总结，在工作中曾通过优化脚本工作流程，总时间提高了60%。</td>
</tr></tbody>
</table></td></tr>
</tbody></table></td></tr>
</tbody></table>
<table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box"><tbody>
<tr><td class="plate1">工作经验</td></tr>
<tr><td class="tbb"><table cellspacing="0" cellpadding="0" border="0">
<tr><td class="p15"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="time">2017/7-2018/7</td>
<td valign="top" class="rtbox">
<strong class="txt3">主管工程师-HW</strong><span class="p5">|</span><span><a href = "http://carrier.huawei.com/cn/products/core-network" target = _blank>云核心网</a>实施一部</span>
</td>
</tr>
<tr><td class="phd tb1" colspan="2">
<span><a href = "http://www.isoftstone.com/" target = _blank>深圳软通动力技术有限公司</a></span><span class="gray">&nbsp;[1年]
                    </span>
</td></tr>
<tr><td class="phd tb1 gray2" colspan="2">计算机软件<span class="p5">|</span>30000人以上<span class="p5">|</span>上市公司</td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">工作描述：</td>
<td valign="top" class="txt1">担任<a href = "http://carrier.huawei.com/cn/products/core-network" target = _blank>云核心网</a>SPS网元的<a href = "http://support.huawei.com/enterprise/zh/network-management/imanager-u2000-pid-15315" target = _blank>网管</a>接口人<br>主要负责:<a href = "https://www.huawei.com/cn/" target = _blank ><b><i>华为</i></b></a><a href = "http://carrier.huawei.com/cn/products/core-network" target = _blank>云核心网</a>信令产品，负责SPS&#x20;19.0、18.0、18.1、补丁版本、维护版本的<a href = "http://support.huawei.com/enterprise/zh/network-management/imanager-u2000-pid-15315" target = _blank>网管</a>适配包。<br>作为软件工程师（<a href = "http://support.huawei.com/enterprise/zh/network-management/imanager-u2000-pid-15315" target = _blank>网管</a>适配包方向）主要负责的工作有：<br>1、将本网元开发和其他平台同步的相关数据写入数据库，对数据准确性进行判断验证，对某些数据的变更进行评审；<br>2、根据SE的要求开发相应的功能特性；<br>3、将源文件编译成不同系统下可用的中间文件；<br>4、根据不同版本编写与我相关部分的用户手册；<br>5、指导其他员工操作网元与<a href = "http://support.huawei.com/enterprise/zh/network-management/imanager-u2000-pid-15315" target = _blank>网管</a>平台的对接以及<a href = "http://support.huawei.com/enterprise/zh/network-management/imanager-u2000-pid-15315" target = _blank>网管</a>平台的相关组件的操作；<br>6、将其他平台的组件、中间件以及源代码通过脚本编译成最终的<a href = "http://support.huawei.com/enterprise/zh/network-management/imanager-u2000-pid-15315" target = _blank>网管</a>适配包给测试经理，测试完成后提交给版本经理进行发布；<br>7、解决<a href = "http://support.huawei.com/enterprise/zh/network-management/imanager-u2000-pid-15315" target = _blank>网管</a>平台周边问题。</td>
</tr></tbody></table></td></tr>
</tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="time">2016/10-2017/7</td>
<td valign="top" class="rtbox">
<strong class="txt3">初级软件工程师</strong><span class="p5">|</span><span>技术部</span>
</td>
</tr>
<tr><td class="phd tb1" colspan="2">
<span><a href = "http://news.enorth.com.cn/system/2016/08/24/031120418.shtml" target = _blank>天津锦标科技有限公司</a></span><span class="gray">&nbsp;[9个月]
                    </span>
</td></tr>
<tr><td class="phd tb1 gray2" colspan="2">计算机软件<span class="p5">|</span>少于50人<span class="p5">|</span>民营公司</td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">工作描述：</td>
<td valign="top" class="txt1">该公司主要为负责互联网安全的后期维护，软件开发。<br>主要工作内容：<br>1、根据产品经理的需求开发相应的功能模块；<br>2、负责客户服务器的正常运行，远程查看运行状态；<br>3、对客户服务器出现的问题进行修复；<br>4、测试整个程序并修复bug。</td>
</tr></tbody></table></td></tr>
</tbody></table></td></tr>
</table></td></tr>
</tbody></table>
<table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box"><tbody>
<tr><td class="plate1">项目经验</td></tr>
<tr><td class="tba"><table cellspacing="0" cellpadding="0" border="0">
<tr><td class="p15"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="time">2017/12-2018/5</td>
<td valign="top" class="rtbox"><strong><a href = "http://carrier.huawei.com/cn/products/core-network/cs-ims/dra-stp" target = _blank>SPSV3</a>&#x20;R018C10</strong></td>
</tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">所属公司：</td>
<td valign="top" class="txt1"><a href = "http://www.isoftstone.com/" target = _blank>深圳软通动力技术有限公司</a></td>
</tr></tbody></table></td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">项目描述：</td>
<td valign="top" class="txt1"><a href = "https://www.huawei.com/cn/" target = _blank ><b><i>华为</i></b></a><a href = "http://carrier.huawei.com/cn/products/core-network" target = _blank>云核心网</a>信令业务处理系统18.1版本，集DRA（Diameter&#x20;Routing&#x20;Agent）、DEA（Diameter&#x20;Edge&#x20;Agent）、TDM-STP、IP-STP和信令分析系统<a href = "http://carrier.huawei.com/cn/products/core-network/cs-ims/dra-stp/SANEX9510" target = _blank>SANEX</a>（Signaling&#x20;Application&#x20;Network&#x20;EXpert）于一体的融合信令解决方案，具备SS7/Sigtran/Diameter/SIP等多种信令接入能力、具有丰富路由管理与控制能力，旨在帮助运营商打造高效、安全和智能的融合信令网，确保运营商信令网可视、可预测和可管理。整个项目两百多人在之前的版本下根据客户需求进行特性迭代。</td>
</tr></tbody></table></td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">责任描述：</td>
<td valign="top" class="txt1">在本项目中，我作为SPS网元接口人，独立完成本岗位的职责之外，积极支持持续集成的诉求（将编译工作模块化，便于每个开发人员进行特性开发。），经过半个多月的研究以及请教编译工具开发人员、持续集成搭建人员终于将编译工程所需的文件拆分，最终实现适配包可持续集成，时间从2.5个小时缩短到45分钟，而且支持多版本同时编译。提高效率之后接了更多的特性开发任务，包括VTS工具上的license文件收集、主机备份失败告警收集、收集项影响程度说明，在开发过程中研究前人的代码发现一些注释有问题的找到代码开发人员仔细核对。在改问题单时多次发现测试人员未发现的联机帮助资料中超链接地址错误以及中英文版本符号不一致等问题，小心谨慎的态度受到大家的认可。</td>
</tr></tbody></table></td></tr>
</tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="time">2017/7-2017/12</td>
<td valign="top" class="rtbox"><strong><a href = "http://carrier.huawei.com/cn/products/core-network/cs-ims/dra-stp" target = _blank>SPSV3</a>&#x20;R018C00</strong></td>
</tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">所属公司：</td>
<td valign="top" class="txt1"><a href = "http://www.isoftstone.com/" target = _blank>深圳软通动力技术有限公司</a></td>
</tr></tbody></table></td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">项目描述：</td>
<td valign="top" class="txt1"><a href = "https://www.huawei.com/cn/" target = _blank ><b><i>华为</i></b></a><a href = "http://carrier.huawei.com/cn/products/core-network" target = _blank>云核心网</a>信令业务处理系统18.0版本，集DRA（Diameter&#x20;Routing&#x20;Agent）、DEA（Diameter&#x20;Edge&#x20;Agent）、TDM-STP、IP-STP和信令分析系统<a href = "http://carrier.huawei.com/cn/products/core-network/cs-ims/dra-stp/SANEX9510" target = _blank>SANEX</a>（Signaling&#x20;Application&#x20;Network&#x20;EXpert）于一体的融合信令解决方案，具备SS7/Sigtran/Diameter/SIP等多种信令接入能力、具有丰富路由管理与控制能力，旨在帮助运营商打造高效、安全和智能的融合信令网，确保运营商信令网可视、可预测和可管理。该项目主要服务对象是网络运营商包括<a href = "http://www.10086.cn/index/bj/index_100_100.html" target = _blank><b><i>中国移动</i></b></a>、<a href = "http://www.ais.co.th/en/" target = _blank><b><i>泰国AIS</i></b></a>。整个项目两百多人在之前的版本下根据客户需求进行特性迭代。</td>
</tr></tbody></table></td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">责任描述：</td>
<td valign="top" class="txt1">在本项目中，我作为SPS网元接口人，经过导师一个月的培训，能独立完成适配包的编译工作，定位适配包功能缺陷。经过对编译脚本的研究改进了编译流程，将不同版本的资料文件单独放置，在资料不需要重新编译的情况下，编译整个适配包的时间从原来的4个小时减少到2.5个小时。独立开发SE设计的“WEB一件事信息收集”特性，多次协助其他项目组解决<a href = "http://support.huawei.com/enterprise/zh/network-management/imanager-u2000-pid-15315" target = _blank>U2000</a>对接CGP失败、告警无法上报、核心网元发现不了、测量对象缺失、<a href = "http://support.huawei.com/enterprise/zh/network-management/imanager-u2000-pid-15315" target = _blank>U2000</a>导出设备档案失败、话务测量报错等问题并总结分享到内部wiki和博客中供其他人问题定位分析，受到客户一致好评。</td>
</tr></tbody></table></td></tr>
</tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="time">2017/2-2017/7</td>
<td valign="top" class="rtbox"><strong>流量审计系统</strong></td>
</tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">所属公司：</td>
<td valign="top" class="txt1"><a href = "http://news.enorth.com.cn/system/2016/08/24/031120418.shtml" target = _blank>天津锦标科技有限公司</a></td>
</tr></tbody></table></td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">项目描述：</td>
<td valign="top" class="txt1">该项目主要功能是对网络流量进行控制，黑名单设置。<br>主要内容：<br>1、搭建<a href = "https://www.dpdk.org/" target = _blank>DPDK</a>开发环境；<br>2、根据功能需求选择相应的数据结构和算法；<br>3、网络数据包类型的判断；<br>4、统计相应数据包的总流量；<br>5、指定黑名单ip段。</td>
</tr></tbody></table></td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">责任描述：</td>
<td valign="top" class="txt1">我在项目中主要负责以下几点：<br>1、搭建<a href = "https://www.dpdk.org/" target = _blank>DPDK</a>开发环境；<br>2、开发黑名单功能模块；<br>3、测试程序是否符合功能需求；<br>4、参与修复程序bug；<br>5、优化代码。</td>
</tr></tbody></table></td></tr>
</tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="time">2016/10-2017/2</td>
<td valign="top" class="rtbox"><strong>酒店管理系统</strong></td>
</tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">所属公司：</td>
<td valign="top" class="txt1"><a href = "http://news.enorth.com.cn/system/2016/08/24/031120418.shtml" target = _blank>天津锦标科技有限公司</a></td>
</tr></tbody></table></td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">项目描述：</td>
<td valign="top" class="txt1">该项目主要是用来查看远程服务器的运行状态，查看特定程序是否正常运行。<br>主要工作内容：<br>1、用ssh配置远程服务器与本地机器的公钥、私钥文件；<br>2、将远程服务器ip加入到配置文件的特定组；<br>3、写一个yaml脚本用来实现指定功能；<br>4、使用ansible执行脚本并生成日志文件。</td>
</tr></tbody></table></td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">责任描述：</td>
<td valign="top" class="txt1">我负责内容：<br>1、配置公、私钥文件；<br>2、写yaml脚本；<br>3、每天执行脚本，根据日志文件信息采取相应措施。</td>
</tr></tbody></table></td></tr>
</tbody></table></td></tr>
</table></td></tr>
</tbody></table>
<table xmlns="" class="box"><tbody>
<tr><td class="plate1">教育经历</td></tr>
<tr><td class="tba"><table cellspacing="0" cellpadding="0" border="0"><tr><td class="p15"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="time">2012/9-2016/6</td>
<td valign="top" class="rtbox"><strong><a href = "http://www.hbpu.edu.cn/" target = _blank>湖北理工学院</a></strong></td>
</tr>
<tr><td class="tb1" colspan="2">本科<span class="p5">|</span>机械设计制造及其自动化</td></tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">专业描述：</td>
<td valign="top" class="txt1">在校期间主要课程包括：高等数学、线性代数、数据统计与概率论、工程力学、材料力学、PLC可编程逻辑控制器、单片机应用技术、数控技术、计算机辅助设计（CAD）、大学物理、电工学、C语言程序设计、计算机基础、计算机辅助制造（CAM）、大学英语等，其中编程类科目成绩优异，在学习之余自学HTML5+CSS3+JavaScript网页设计，自主学习计算机课程，包括计算机组成原理、数据结构、操作系统、Python程序设计、数据库等，自学能力强。</td>
</tr></tbody></table></td></tr>
</tbody></table></td></tr></table></td></tr>
</tbody></table>
<table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box"><tbody>
<tr><td class="plate1">在校情况</td></tr>
<tr><td class="tbb">
<table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr><td class="tit">校内荣誉</td></tr>
<tr><td class="tb3"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="time">2016/6</td>
<td valign="top" class="rtbox">
<strong class="txt3">优秀毕业生</strong><span>（校级）</span>
</td>
</tr></tbody></table></td></tr>
<tr><td class="tb3 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="time">2015/11</td>
<td valign="top" class="rtbox">
<strong class="txt3">2015届全国大学生数学竞赛三等奖</strong><span>（省级）</span>
</td>
</tr></tbody></table></td></tr>
<tr><td class="tb3 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="time">2015/3</td>
<td valign="top" class="rtbox">
<strong class="txt3">校级丙等奖学金</strong><span>（校级）</span>
</td>
</tr></tbody></table></td></tr>
<tr><td class="tb3 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="time">2014/3</td>
<td valign="top" class="rtbox">
<strong class="txt3">校级丙等奖学金</strong><span>（校级）</span>
</td>
</tr></tbody></table></td></tr>
</tbody></table>
<table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr><td class="tit">校内职务</td></tr>
<tr><td class="p15"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="time">2012/10-2013/6</td>
<td valign="top" class="rtbox"><strong class="txt3">体育委员</strong></td>
</tr>
<tr><td class="tb1" colspan="2"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="keys">职务描述：</td>
<td valign="top" class="txt1">主要工作内容：<br>1.组织人员每节课上课之前去仓库拿运动器材；<br>2.组织全班人员去登高、远足、校园活动等<br>3.组织安排全班人员体育成绩测试</td>
</tr></tbody></table></td></tr>
</tbody></table></td></tr>
</tbody></table>
</td></tr>
</tbody></table>
<table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box"><tbody>
<tr><td class="plate1">
              技能特长
              <span class="f12">（包括IT技能、语言能力、证书、成绩、培训经历）</span>
</td></tr>
<tr><td class="tbb">
<table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr><td class="tit">技能/语言</td></tr>
<tr><td class="p15"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="tb2 cell sl" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">Linux</strong></td>
<td valign="top"><span class="skbg"><span class="skco">熟练</span></span></td>
</tr></tbody></table></td>
<td class="tb2 cell lh" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">MS&#x20;OneNote</strong></td>
<td valign="top"><span class="skbg"><span class="skco">良好</span></span></td>
</tr></tbody></table></td></tr><tr><td class="tb2 cell lh" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">MySQL</strong></td>
<td valign="top"><span class="skbg"><span class="skco">良好</span></span></td>
</tr></tbody></table></td>
<td class="tb2 cell lh" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">HTML5+CSS3+JS</strong></td>
<td valign="top"><span class="skbg"><span class="skco">良好</span></span></td>
</tr></tbody></table></td></tr><tr><td class="tb2 cell sl" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">C/C++</strong></td>
<td valign="top"><span class="skbg"><span class="skco">熟练</span></span></td>
</tr></tbody></table></td>
<td class="tb2 cell lh" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">XML/XSLT</strong></td>
<td valign="top"><span class="skbg"><span class="skco">良好</span></span></td>
</tr></tbody></table></td></tr><tr><td class="tb2 cell lh" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">英语</strong></td>
<td valign="top"><span class="skbg"><span class="skco">良好</span></span></td>
</tr></tbody></table></td>
<td class="tb2 cell sl" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">Python</strong></td>
<td valign="top"><span class="skbg"><span class="skco">熟练</span></span></td>
</tr></tbody></table></td></tr><tr><td class="tb2 cell yb" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">Web前端</strong></td>
<td valign="top"><span class="skbg"><span class="skco">一般</span></span></td>
</tr></tbody></table></td>
<td class="tb2 cell lh" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">OutLook&#x20;Express</strong></td>
<td valign="top"><span class="skbg"><span class="skco">良好</span></span></td>
</tr></tbody></table></td></tr><tr><td class="tb2 cell lh" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">MS&#x20;Excel</strong></td>
<td valign="top"><span class="skbg"><span class="skco">良好</span></span></td>
</tr></tbody></table></td>
<td class="tb2 cell sl" valign="top"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td class="skill"><strong class="txt3">AUTOCAD</strong></td>
<td valign="top"><span class="skbg"><span class="skco">熟练</span></span></td>
</tr></tbody></table></td></tr></tbody></table></td></tr>
</tbody></table>
<table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr><td class="tit">证书</td></tr>
<tr><td class="tb3"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="time">2017/3</td>
<td valign="top" class="rtbox">
<strong class="txt3">C1驾照</strong><span>
                      （93）
                    </span>
</td>
</tr></tbody></table></td></tr>
<tr><td class="tb3 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr>
<td valign="top" class="time">2014/6</td>
<td valign="top" class="rtbox">
<strong class="txt3">全国计算机等级二级</strong><span>
                      （81）
                    </span>
</td>
</tr></tbody></table></td></tr>
</tbody></table>
</td></tr>
</tbody></table>
<table xmlns="" cellspacing="0" cellpadding="0" border="0" class="box"><tbody>
<tr><td class="plate1">附加信息</td></tr>
<tr><td class="tbb"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr><td class="tit">附件</td></tr>
<tr><td class="p15"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="tb1"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="keys">附件：</td>
<td valign="top" class="txt3"><strong>个人服务器</strong></td>
</tr>
<tr>
<td valign="top" class="keys">附件链接：</td>
<td valign="top" class="txt1"><a href = "http://www.fanbinglin.com" target = _blank>http://www.fanbinglin.com</a></td>
</tr>
<tr>
<td valign="top" class="keys">附件描述：</td>
<td valign="top" class="txt1">利用阿里云服务器搭建的个人网站，包括我经常访问的网站，该服务器主要是用来进行个人学习。</td>
</tr>
</tbody></table></td></tr></tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="tb1"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="keys">附件：</td>
<td valign="top" class="txt3"><strong>GitHub个人主页</strong></td>
</tr>
<tr>
<td valign="top" class="keys">附件链接：</td>
<td valign="top" class="txt1"><a href = "https://fblrainbow.github.io/" target = _blank>https://fblrainbow.github.io/</a></td>
</tr>
<tr>
<td valign="top" class="keys">附件描述：</td>
<td valign="top" class="txt1">利用GitHub搭建的个人主页，跟阿里云服务器类似。</td>
</tr>
</tbody></table></td></tr></tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="tb1"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="keys">附件：</td>
<td valign="top" class="txt3">
<strong>2016届优秀毕业生</strong><a target="_blank" class="cha" href="http://i.51job.com/resume/ajax/image.php?type=image&amp;userid=377422576&amp;attachid=45204175&amp;key=70a0980dedcb928016a1bd3f1b236c30">
                              查看&gt;
                            </a>
</td>
</tr>
<tr>
<td valign="top" class="keys">附件描述：</td>
<td valign="top" class="txt1">大学四年在校各方面表现优异，得到老师和同学的高度认可，投票获得此荣誉。</td>
</tr>
</tbody></table></td></tr></tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="tb1"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="keys">附件：</td>
<td valign="top" class="txt3">
<strong>合作之星</strong><a target="_blank" class="cha" href="http://i.51job.com/resume/ajax/image.php?type=image&amp;userid=377422576&amp;attachid=45204176&amp;key=70a0980dedcb928016a1bd3f1b236c30">
                              查看&gt;
                            </a>
</td>
</tr>
<tr>
<td valign="top" class="keys">附件描述：</td>
<td valign="top" class="txt1">2017年第四季度，在跟<a href = "https://www.huawei.com/cn/" target = _blank ><b><i>华为</i></b></a>方客户交流中多次发现历史遗留的问题并提出解决方案，得到<a href = "https://www.huawei.com/cn/" target = _blank ><b><i>华为</i></b></a>方合作代表及主管的认可，被评为第四季度合作之星。</td>
</tr>
</tbody></table></td></tr></tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="tb1"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="keys">附件：</td>
<td valign="top" class="txt3"><strong><a href = "https://blog.csdn.net/qq_37608398" target = _blank>CSDN</a>博客</strong></td>
</tr>
<tr>
<td valign="top" class="keys">附件链接：</td>
<td valign="top" class="txt1"><a href =  "https://blog.csdn.net/qq_37608398" target = _blank>https://blog.csdn.net/qq_37608398</a></td>
</tr>
<tr>
<td valign="top" class="keys">附件描述：</td>
<td valign="top" class="txt1">该博客是我工作之后精心维护的结晶，在学习中经常进行总结分享，也方便日后进行回顾。通过该博客我认识不少志同道合的朋友，看到评论中我的经验让他们解决问题我十分欣慰，也是我长期坚持写博客的动力。</td>
</tr>
</tbody></table></td></tr></tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="tb1"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="keys">附件：</td>
<td valign="top" class="txt3"><strong>Django开发的博客网站</strong></td>
</tr>
<tr>
<td valign="top" class="keys">附件链接：</td>
<td valign="top" class="txt1"><a href = "http://www.fanbinglin.com:8000/myBlog" target = _blank>http://www.fanbinglin.com:8000/myBlog</a></td>
</tr>
<tr>
<td valign="top" class="keys">附件描述：</td>
<td valign="top" class="txt1">该网站是学习Python3的Django时搭建的网站。</td>
</tr>
</tbody></table></td></tr></tbody></table></td></tr>
<tr><td class="p15 con"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="tb1"><table cellspacing="0" cellpadding="0" border="0"><tbody>
<tr>
<td valign="top" class="keys">附件：</td>
<td valign="top" class="txt3">
<strong>2015届全国大学生数学竞赛三等奖</strong><a target="_blank" class="cha" href="http://i.51job.com/resume/ajax/image.php?type=image&amp;userid=377422576&amp;attachid=45204174&amp;key=70a0980dedcb928016a1bd3f1b236c30">
                              查看&gt;
                            </a>
</td>


</tr>
<tr>
<td valign="top" class="keys">附件描述：</td>
<td valign="top" class="txt1">从学校六月的初赛以及后来的培训之后的决赛，经过两轮淘汰赛之后留下来作为参赛选手，在武汉科技大学参加全国大学生数学竞赛湖北赛区并取得该荣誉。</td>
</tr>
</tbody></table></td></tr></tbody></table></td></tr>
</tbody></table></td></tr>
</tbody></table></td></tr></tbody></table></body></html>

     ''','html','utf-8')
# from_addr = input('From:')
# password = input('Password:')
# to_addr = input('To:')
# smtp_server = input('SMTP server:')

msg['From'] = _format_addr('(简历)Python开发工程师-2年 <%s>' % from_addr)
msg['To'] = _format_addr('HR <%s>' % to_addr)
msg['Subject'] = Header('Python3开发工程师-自荐','utf-8').encode()
server = smtplib.SMTP_SSL(smtp_server)
server.set_debuglevel(2)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()