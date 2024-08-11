from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {'title': 'int型示例', 'dataIndex': 'int型示例'},
            {'title': 'float型示例', 'dataIndex': 'float型示例'},
            {'title': 'str型示例', 'dataIndex': 'str型示例'},
            {'title': '日期时间示例', 'dataIndex': '日期时间示例'},
        ],
        data=[
            {
                'int型示例': 123,
                'float型示例': 1.23,
                'str型示例': '示例字符',
                '日期时间示例': datetime.now(),
            }
        ]
        * 3,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {'title': 'int型示例', 'dataIndex': 'int型示例'},
        {'title': 'float型示例', 'dataIndex': 'float型示例'},
        {'title': 'str型示例', 'dataIndex': 'str型示例'},
        {'title': '日期时间示例', 'dataIndex': '日期时间示例'},
    ],
    data=[
        {
            'int型示例': 123,
            'float型示例': 1.23,
            'str型示例': '示例字符',
            '日期时间示例': datetime.now(),
        }
    ]
    * 3,
)
"""
    }
]
