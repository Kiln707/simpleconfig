from .ini_formatter import INI_Formatter
from .json_formatter import JSON_Formatter
from .exceptions import NoExtensionError, NoFormatterError


class FormatFactory:
    def __init__(self):
        self._formatters = {
            "ini": INI_Formatter,
            "json": JSON_Formatter
        }

    def add_formatter(self, file_exts: list, formatter):
        for ext in file_exts:
            self._formatters[ext] = formatter

    def remove_formatter(self, ext):
        self._formatters.pop(ext, None)

    def get_formatter(self, filepath):
        if not filepath or len(str(filepath.name).split('.')) <= 1:
            raise NoExtensionError()
        ext = str(filepath.name).split('.')[1]
        print(ext, self._formatters, ext in self._formatters)
        if ext not in self._formatters:
            raise NoFormatterError(ext=ext)
        return self._formatters[ext]()
