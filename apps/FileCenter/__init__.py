from apps.FileCenter.view import view

route = [{
    'prefix': '/file',
    'tags': ['FileCenter'],
    'router': view,
}]
