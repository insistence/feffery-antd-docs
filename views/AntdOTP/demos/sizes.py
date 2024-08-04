import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('size="small"', innerTextOrientation='left'),
            fac.AntdOTP(size='small'),
            fac.AntdDivider(
                'size="middle"（默认）', innerTextOrientation='left'
            ),
            fac.AntdOTP(),
            fac.AntdDivider('size="large"', innerTextOrientation='left'),
            fac.AntdOTP(size='large'),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('size="small"', innerTextOrientation='left'),
        fac.AntdOTP(size='small'),
        fac.AntdDivider(
            'size="middle"（默认）', innerTextOrientation='left'
        ),
        fac.AntdOTP(),
        fac.AntdDivider('size="large"', innerTextOrientation='left'),
        fac.AntdOTP(size='large'),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
