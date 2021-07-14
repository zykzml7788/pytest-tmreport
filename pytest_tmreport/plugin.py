import pytest
import os
import copy
import datetime
import string
import random

base_dir = os.path.dirname(__file__)

cases = []


def pytest_collection_modifyitems(items):
    """
    修改用例名称中文乱码
    :param items:
    :return:
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')


# 添加一个命令行参数
def pytest_addoption(parser, pluginmanager):
    report = parser.getgroup("tmreport")
    report.addoption("--pytest-tmreport-name",  # 报告存储名称
                     # default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.html'html,  # 参数的默认值
                     help='set your report name'  # 帮助提示参数的描述信息
                     )
    report.addoption("--pytest-tmreport-path",  # 报告存储路径
                     default='.',  # 参数的默认值
                     help='set your report path'  # 帮助提示参数的描述信息
                     )


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    report = out.get_result()
    if report.when == "call":
        cases.append({'id': random.randint(0, 9999999), 'title': item.nodeid})
        longrepr = str(report.longrepr) if report.longrepr else ""
        logs = longrepr + "\n".join(["\n".join(section) for section in report.sections])  # 用例执行日志
        logs = "\n | INFO |".join(logs.split("| INFO |"))  # 换行处理
        result = 1 if report.outcome == 'passed' else 0  # 是否通过
        duration = report.duration  # 执行时间
        title = report.nodeid
        doc = item.function.__doc__
        result_info = {
            "logs": logs,
            "result": result,
            "duration": duration,
            "doc": doc if doc else "",
            "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        # 更新结果
        for case in cases:
            if case["title"] == title:
                case["title"] = case["title"].encode('ISO-8859-1').decode("utf-8")
                case.update(result_info)


def generate_report(name, path='.', **kwargs):
    with open(base_dir + '/reports/' + 'template.html', 'r', encoding="utf-8") as f:
        template_html_str = f.read()

    filename = os.path.join(path, name)
    with open(filename, 'w', encoding="utf-8") as f:
        template = string.Template(template_html_str)  # 获取一个模板文件
        html_str = template.substitute(kwargs)
        f.write(html_str)


@pytest.fixture(scope="session", autouse=True)
def setup_fixture(request):
    report_name = request.config.getoption("--pytest-tmreport-name")
    yield
    if report_name:
        print("all test over, begin to generate tmreport " + report_name)
        # 结束后生成测试报告
        for case in cases:
            for k, v in case.items():
                if v == None:
                    case[k] = ""

        success = len(list(filter(lambda x: x["result"] == 1, cases)))
        failed = len(cases) - success
        duration = sum([case["duration"] for case in cases])
        avg_duration = duration / len(cases)
        success_rate = success / len(cases)
        summary = {
            "total": len(cases),
            "success": success,
            "failed": failed,
            "success_rate": success_rate,
            "fail_rate": failed / len(cases),
            "duration": duration,
            "avg_duration": avg_duration,
        }
        series_data = [
            {"value": success, "name": 'Success'},
            {"value": failed, "name": 'Failed'}
        ]

        report_path = request.config.getoption("--pytest-tmreport-path", default='.')
        generate_report(name=report_name, path=report_path, cases=cases, summary=summary, series_data=series_data, success_rate=success_rate)
        print("the tmreport is generated !")