import importlib
from pathlib import Path
from core.config import settings
from core.log import log


class InitApps:
    def __init__(self, app):
        self.app = app

    def start(self):
        self.load_apps()

    def load_apps(self):
        for path in Path(settings.APPS_DIR).iterdir():
            if path.is_dir() and not path.name.startswith('_'):
                app_path = f'{settings.APPS_DIR}.{path.name}'
                view = importlib.import_module(app_path)
                if hasattr(view, 'route'):
                    for route in getattr(view, 'route'):
                        self.app.include_router(**route)
                        log.info(f'Load {route["prefix"]} success')
