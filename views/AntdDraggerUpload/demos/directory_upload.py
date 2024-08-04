import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDraggerUpload(
        apiUrl='/upload/',
        fileMaxSize=1,
        directory=True,
        text='文件夹拖拽上传示例',
        hint='点击或拖拽文件夹至此处进行上传',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    directory=True,
    text='文件夹拖拽上传示例',
    hint='点击或拖拽文件夹至此处进行上传',
)
"""
    }
]
