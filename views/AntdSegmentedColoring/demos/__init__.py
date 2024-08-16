import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    sizes,  # noqa: F401
    border,  # noqa: F401
    auxiliary_button,  # noqa: F401
    disabled_status,  # noqa: F401
    read_only_status,  # noqa: F401
    color_block_position,  # noqa: F401
    basic_callbacks,  # noqa: F401
    color_block_click_event,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最简单的分段着色。'),
    },
    {
        'path': 'sizes',
        'title': '不同的尺寸规格',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('size', code=True),
                '控制尺寸规格。',
            ]
        ),
    },
    {
        'path': 'border',
        'title': '边框',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('bordered', code=True),
                '显示或隐藏边框。',
            ]
        ),
    },
    {
        'path': 'auxiliary_button',
        'title': '辅助按钮',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('controls', code=True),
                '显示或隐藏数字输入框右侧内部辅助快捷增减按钮。',
            ]
        ),
    },
    {
        'path': 'disabled_status',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabled=True', code=True),
                '开启禁用状态。',
            ]
        ),
    },
    {
        'path': 'read_only_status',
        'title': '只读状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('readOnly=True', code=True),
                '开启只读状态。',
            ]
        ),
    },
    {
        'path': 'color_block_position',
        'title': '颜色块位置',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('colorBlockPosition', code=True),
                '控制颜色块位置。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('可用于监听当前的各分段断点值。'),
    },
    {
        'path': 'color_block_click_event',
        'title': '监听色块点击事件',
        'description': fac.AntdParagraph(
            [
                '通过监听属性',
                fac.AntdText('colorBlockClickEvent', code=True),
                '变化来获取色块点击事件。',
            ]
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
