import sublime
import sublime_plugin
import unittest


class MockSideBarSelection:
    def __init__(self, paths):
        self.paths = paths

    def getSelectedFiles(self):
        return [MockSideBarItem(path) for path in self.paths]


class MockSideBarItem:
    def __init__(self, path):
        self.path = path

    def edit(self):
        # Simular la edición del archivo
        view = sublime.active_window().new_file()
        view.set_name(self.path)
        return view


class MockCachedSelection:
    def __init__(self, paths):
        self.paths = paths

    def hasFiles(self):
        return bool(self.paths)


class TestSideBarEditToRightCommand(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.window = sublime.active_window()
        self.command = SideBarEditToRightCommand(self.window)
        global SideBarSelection, CACHED_SELECTION
        SideBarSelection = MockSideBarSelection
        CACHED_SELECTION = MockCachedSelection

    def test_run_command(self):
        paths = ["/path/to/file1.txt", "/path/to/file2.txt"]
        self.command.run(paths)

        # Verificar que el layout se ha establecido correctamente
        layout = self.window.get_layout()
        expected_layout = {
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 1.0],
            "cells": [[0, 0, 1, 1], [1, 0, 2, 1]],
        }
        self.assertEqual(layout, expected_layout)

        # Verificar que los archivos se abrieron y movieron al grupo correcto
        for view in self.window.views_in_group(1):
            self.assertIn(view.name(), ["file1.txt", "file2.txt"])

    def test_is_enabled(self):
        paths = ["/path/to/file1.txt"]
        self.assertTrue(self.command.is_enabled(paths))
        paths = []
        self.assertFalse(self.command.is_enabled(paths))


if __name__ == "__main__":
    unittest.main()
