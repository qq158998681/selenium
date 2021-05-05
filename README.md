# selenium自动化测试框架
本框架使用seleium+unittest+ddt+email+beautifulReport
支持测试完成后自动生成测试报告，和自动发送邮件(config里面配置邮件地址及信息),测试报告和日志文件在本文件同级目录下生成


还欠缺： 测试报告模块 report、测试数据驱动 testdata、其他公共方法：截图，最大化等

未兼容： 多邮箱发送、浏览器是否复用判断


api 动作类
config 配置文件
emailfile  邮件工具
pagebase  公共方法，包括读取配置文件信息、运行日志、selenium基础方法的封装
report  测试报告,默认截取（beautifulReport）
testcase  测试用例（unittest）
testdata  测试数据驱动


     