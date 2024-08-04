import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTimeRangePicker(
        hourStep=3, minuteStep=10, secondStep=20
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTimeRangePicker(
    hourStep=3, minuteStep=10, secondStep=20
)
"""
    }
]
