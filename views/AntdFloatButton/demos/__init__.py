from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component
import feffery_markdown_components as fmc

import views
from . import (
    basic_usage,  # noqa: F401
    button_types,  # noqa: F401
    button_shapes,  # noqa: F401
    button_icon,  # noqa: F401
    button_description,  # noqa: F401
    button_tooltip,  # noqa: F401
    as_link,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from config import AppConfig
from components import mock_browser

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最基础的悬浮按钮。'),
        'iframe': True,
    },
    {
        'path': 'button_types',
        'title': '按钮类型',
        'description': fac.AntdParagraph('不同类型的悬浮按钮。'),
        'iframe': True,
    },
    {
        'path': 'button_shapes',
        'title': '按钮形状',
        'description': fac.AntdParagraph('不同形状的悬浮按钮。'),
        'iframe': True,
    },
    {
        'path': 'button_icon',
        'title': '按钮图标',
        'description': fac.AntdParagraph('为悬浮按钮自定义图标元素。'),
        'iframe': True,
    },
    {
        'path': 'button_description',
        'title': '描述信息',
        'description': fac.AntdParagraph('为悬浮按钮添加额外描述信息。'),
        'iframe': True,
    },
    {
        'path': 'button_tooltip',
        'title': '气泡卡片',
        'description': fac.AntdParagraph('为悬浮按钮添加额外气泡卡片信息。'),
        'iframe': True,
    },
    {
        'path': 'as_link',
        'title': '链接跳转功能',
        'description': fac.AntdParagraph('点击悬浮按钮进行链接跳转。'),
        'iframe': True,
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('监听悬浮按钮的点击事件。'),
        'iframe': True,
    },
]


def render(component: Component) -> Component:
    """渲染当前组件演示用例"""

    return fac.AntdSpace(
        [
            html.Div(
                [
                    html.Div(
                        (
                            fac.AntdSpace(
                                [
                                    mock_browser.render(),
                                    # 懒加载优化
                                    fuc.FefferyLazyLoad(
                                        html.Iframe(
                                            src='/~demo/{}/{}'.format(
                                                component.__name__, item['path']
                                            ),
                                            style={
                                                'border': '1px solid #f0f0f0',
                                                'boxSizing': 'border-box',
                                                'width': '100%',
                                                'height': 350,
                                            },
                                        ),
                                        height=350,
                                        throttle=500,
                                    ),
                                ],
                                direction='vertical',
                                size=0,
                                style={'width': '100%'},
                            )
                            if item.get('iframe')
                            else getattr(
                                views.AntdFloatButton.demos, item['path']
                            ).render()
                        ),
                        className='demo-box',
                    ),
                    html.Div(
                        [
                            fac.AntdText(
                                [
                                    item['title'],
                                    fac.AntdTooltip(
                                        html.A(
                                            fac.AntdIcon(
                                                icon='antd-edit',
                                                className='demo-github-link',
                                            ),
                                            href='{}/edit/{}/views/{}/demos/{}.py'.format(
                                                AppConfig.doc_library_repo,
                                                AppConfig.doc_library_branch,
                                                component.__name__,
                                                item['path'],
                                            ),
                                            target='_blank',
                                        ),
                                        title='在Github上编辑此示例',
                                    ),
                                ],
                                className='demo-title',
                            ),
                            html.Div(
                                item['description'],
                                style={'padding': '18px 24px 12px 28px'},
                            ),
                        ],
                        style={'position': 'relative'},
                    ),
                    fac.AntdCenter(
                        fac.AntdSpace(
                            [
                                fac.AntdTooltip(
                                    dcc.Link(
                                        fac.AntdIcon(icon='antd-export'),
                                        href='/~demo/{}/{}'.format(
                                            component.__name__, item['path']
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title='在新窗口打开',
                                ),
                                fac.AntdTooltip(
                                    fac.AntdIcon(
                                        id={
                                            'type': 'demo-code-toggle',
                                            'index': '{}/{}'.format(
                                                component.__name__, item['path']
                                            ),
                                        },
                                        icon='antd-code',
                                        className='demo-operations-icon',
                                    ),
                                    title='展开/收起代码',
                                ),
                                fac.AntdTooltip(
                                    dcc.Link(
                                        fac.AntdIcon(icon='antd-github'),
                                        href='{}/tree/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_library_repo,
                                            AppConfig.doc_library_branch,
                                            component.__name__,
                                            item['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-icon',
                                    ),
                                    title='在Github中查看完整代码',
                                ),
                                fac.AntdTooltip(
                                    dcc.Link(
                                        html.Img(
                                            src='/assets/imgs/gitee-logo.svg',
                                            width=18,
                                            height=18,
                                            style={
                                                'display': 'block',
                                                'transform': 'translate(-0.05em, 0.05em)',
                                            },
                                        ),
                                        href='{}/blob/{}/views/{}/demos/{}.py'.format(
                                            AppConfig.doc_gitee_library_repo,
                                            AppConfig.doc_library_branch,
                                            component.__name__,
                                            item['path'],
                                        ),
                                        target='_blank',
                                        className='demo-operations-img',
                                    ),
                                    title='在Gitee中查看完整代码',
                                ),
                            ],
                            size=12,
                        ),
                        className='demo-operations',
                    ),
                    fac.AntdTabs(
                        items=[
                            {
                                'label': item.get('language') or 'Python',
                                'key': item.get('language') or 'Python',
                                'children': fmc.FefferySyntaxHighlighter(
                                    codeString=item['code'],
                                    language=(
                                        item.get('language') or 'Python'
                                    ).lower(),
                                    codeTheme='coy-without-shadows',
                                    codeBlockStyle={'overflowX': 'auto'},
                                ),
                            }
                            for item in getattr(
                                views.AntdFloatButton.demos, item['path']
                            ).code_string
                        ],
                        centered=True,
                        className='demo-code-tabs',
                        id={
                            'type': 'demo-code',
                            'index': '{}/{}'.format(
                                component.__name__, item['path']
                            ),
                        },
                        style={'display': 'none'},
                    ),
                ],
                className='demo-container',
                id='demo-container-' + item['path'],
            )
            for item in demos_config
        ],
        direction='vertical',
        size='large',
        style={'width': '100%'},
    )
