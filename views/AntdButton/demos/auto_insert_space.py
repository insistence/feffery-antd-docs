import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [fac.AntdButton('汉字'), fac.AntdButton('汉字', autoInsertSpace=False)],
        wrap=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [fac.AntdButton('汉字'), fac.AntdButton('汉字', autoInsertSpace=False)],
    wrap=True,
)
"""
    }
]
