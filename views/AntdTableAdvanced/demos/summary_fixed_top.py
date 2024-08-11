import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 10,
        bordered=True,
        summaryRowContents=[
            {'content': '第1列总结'},
            {'content': '第2到4列总结', 'colSpan': 3, 'align': 'center'},
            {'content': '第5列总结', 'align': 'right'},
        ],
        summaryRowFixed='top',
        maxHeight=150,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
        for i in range(1, 6)
    ],
    data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 10,
    bordered=True,
    summaryRowContents=[
        {'content': '第1列总结'},
        {'content': '第2到4列总结', 'colSpan': 3, 'align': 'center'},
        {'content': '第5列总结', 'align': 'right'},
    ],
    summaryRowFixed='top',
    maxHeight=150,
)
"""
    }
]
