from robot.api import TestSuite
from robot.api import ResultWriter
if __name__ == "__main__":
    print("Robot Framework基本执行过程演示代码")
      # 创建套件
    suite = TestSuite("百度搜索测试套件")

    # 导入SeleniumLibrary库
    suite.resource.imports.library("SeleniumLibrary")
      # 创建测试用例：启动浏览器
    test_01 = suite.tests.create("启动浏览器")
    test_01.keywords.create("Open Browser",
        args=["http://www.baidu.com", "Chrome"])
    test_01.keywords.create("Title Should Be",
        args=["百度一下，你就知道"])

    # 创建测试用例：百度搜索测试
    test_02 = suite.tests.create("百度搜索测试")
    test_02.keywords.create("Input Text",
        args=["id=kw", "开源优测"])
    test_02.keywords.create("Click Button", args=["id=su"])
    test_02.keywords.create("Sleep", args=["5s"])

    # 创建测试用例：断言验证搜索结果标题
    test_03 = suite.tests.create("断言验证搜索结果标题")
    test_03.keywords.create("Title Should Be",
        args=["开源优测_百度搜索"])

    # 创建测试用例：关闭测试用例
    test_04 = suite.tests.create("关闭浏览器")
    test_04.keywords.create("Close All Browsers")

    # 运行套件
    result = suite.run(critical="百度搜索", output="output.xml")

    # 生成日志、报告文件
    ResultWriter(result).write_results(report="report.html",
        log="log.html")