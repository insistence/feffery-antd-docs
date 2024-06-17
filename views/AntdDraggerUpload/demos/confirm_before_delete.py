import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDraggerUpload(
        apiUrl='/upload/',
        fileMaxSize=1,
        text='拖拽上传示例',
        hint='点击或拖拽文件至此处进行上传',
        defaultFileList=[
            {'name': f'demo{i}.txt', 'status': 'done'} for i in range(1, 6)
        ],
        confirmBeforeDelete=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传',
    defaultFileList=[
        {'name': f'demo{i}.txt', 'status': 'done'} for i in range(1, 6)
    ],
    confirmBeforeDelete=True,
)
"""
    }
]
