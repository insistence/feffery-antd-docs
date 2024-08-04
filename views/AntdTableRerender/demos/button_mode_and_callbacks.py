import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTable(
            id='table-rerender-button-demo',
            columns=[
                {
                    'title': 'button示例1',
                    'dataIndex': 'button示例1',
                    'renderOptions': {'renderType': 'button'},
                },
                {
                    'title': 'button示例2',
                    'dataIndex': 'button示例2',
                    'renderOptions': {'renderType': 'button'},
                },
                {
                    'title': 'button示例3',
                    'dataIndex': 'button示例3',
                    'renderOptions': {
                        'renderType': 'button',
                        'renderButtonPopConfirmProps': {
                            'title': '确认执行？',
                            'okText': '确认',
                            'cancelText': '取消',
                        },
                    },
                },
            ],
            data=[
                {
                    'button示例1': {
                        'content': f'按钮1-{i}',
                        'type': 'link',
                        'custom': 'balabalabalabala',
                    },
                    'button示例2': [
                        {
                            'content': f'按钮2-{i}-{j}',
                            'type': 'primary',
                            'custom': 'balabalabalabala',
                        }
                        for j in range(1, 3)
                    ],
                    'button示例3': [
                        {
                            'content': f'按钮3-{i}-{j}',
                            'type': 'dashed',
                            'danger': True,
                            'custom': 'balabalabalabala',
                        }
                        for j in range(1, 3)
                    ],
                }
                for i in range(1, 4)
            ],
            bordered=True,
        ),
        html.Pre(id='table-rerender-button-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('table-rerender-button-demo-output', 'children'),
    Input('table-rerender-button-demo', 'nClicksButton'),
    [
        State('table-rerender-button-demo', 'clickedContent'),
        State('table-rerender-button-demo', 'clickedCustom'),
        State('table-rerender-button-demo', 'recentlyButtonClickedDataIndex'),
        State('table-rerender-button-demo', 'recentlyButtonClickedRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_button_demo(
    nClicksButton,
    clickedContent,
    clickedCustom,
    recentlyButtonClickedDataIndex,
    recentlyButtonClickedRow,
):
    return json.dumps(
        dict(
            nClicksButton=nClicksButton,
            clickedContent=clickedContent,
            clickedCustom=clickedCustom,
            recentlyButtonClickedDataIndex=recentlyButtonClickedDataIndex,
            recentlyButtonClickedRow=recentlyButtonClickedRow,
        ),
        indent=4,
        ensure_ascii=False,
    )


code_string = [
    {
        'code': """
[
    fac.AntdTable(
        id='table-rerender-button-demo',
        columns=[
            {
                'title': 'button示例1',
                'dataIndex': 'button示例1',
                'renderOptions': {'renderType': 'button'},
            },
            {
                'title': 'button示例2',
                'dataIndex': 'button示例2',
                'renderOptions': {'renderType': 'button'},
            },
            {
                'title': 'button示例3',
                'dataIndex': 'button示例3',
                'renderOptions': {
                    'renderType': 'button',
                    'renderButtonPopConfirmProps': {
                        'title': '确认执行？',
                        'okText': '确认',
                        'cancelText': '取消',
                    },
                },
            },
        ],
        data=[
            {
                'button示例1': {
                    'content': f'按钮1-{i}',
                    'type': 'link',
                    'custom': 'balabalabalabala',
                },
                'button示例2': [
                    {
                        'content': f'按钮2-{i}-{j}',
                        'type': 'primary',
                        'custom': 'balabalabalabala',
                    }
                    for j in range(1, 3)
                ],
                'button示例3': [
                    {
                        'content': f'按钮3-{i}-{j}',
                        'type': 'dashed',
                        'danger': True,
                        'custom': 'balabalabalabala',
                    }
                    for j in range(1, 3)
                ],
            }
            for i in range(1, 4)
        ],
        bordered=True,
    ),
    html.Pre(id='table-rerender-button-demo-output'),
]

...

@app.callback(
    Output('table-rerender-button-demo-output', 'children'),
    Input('table-rerender-button-demo', 'nClicksButton'),
    [
        State('table-rerender-button-demo', 'clickedContent'),
        State('table-rerender-button-demo', 'clickedCustom'),
        State('table-rerender-button-demo', 'recentlyButtonClickedDataIndex'),
        State('table-rerender-button-demo', 'recentlyButtonClickedRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_button_demo(
    nClicksButton,
    clickedContent,
    clickedCustom,
    recentlyButtonClickedDataIndex,
    recentlyButtonClickedRow,
):
    return json.dumps(
        dict(
            nClicksButton=nClicksButton,
            clickedContent=clickedContent,
            clickedCustom=clickedCustom,
            recentlyButtonClickedDataIndex=recentlyButtonClickedDataIndex,
            recentlyButtonClickedRow=recentlyButtonClickedRow,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
    }
]
