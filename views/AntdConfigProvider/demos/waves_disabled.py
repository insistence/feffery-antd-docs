import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton(
                '未禁用',
                type='primary',
            ),
            fac.AntdConfigProvider(
                fac.AntdButton(
                    '已禁用',
                    type='primary',
                ),
                wavesDisabled=True,
            ),
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            '未禁用',
            type='primary',
        ),
        fac.AntdConfigProvider(
            fac.AntdButton(
                '已禁用',
                type='primary',
            ),
            wavesDisabled=True,
        ),
    ]
)
"""
    }
]
