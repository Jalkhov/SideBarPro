import sublime
import sublime_plugin
import unittest

# Importa la clase SideBarEditCommand desde SideBar.py usando una importación absoluta
from SideBarPro.SideBar import SideBarEditCommand


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
        print("Editing file: {}".format(self.path))
        return view


class MockCachedSelection:
    def __init__(self, paths):
        self.paths = paths

    def hasFiles(self):
        return bool(self.paths)


class TestSideBarEditCommand(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.window = sublime.active_window()
        self.command = SideBarEditCommand(self.window)
        global SideBarSelection, CACHED_SELECTION
        SideBarSelection = MockSideBarSelection
        CACHED_SELECTION = MockCachedSelection

    def test_run_command(self):
        paths = ["/path/to/file1.txt", "/path/to/file2.txt"]
        self.command.run(paths)
        # Verificar que se intenta editar los archivos proporcionados

    def test_is_enabled(self):
        paths = ["/path/to/file1.txt"]
        self.assertTrue(self.command.is_enabled(paths))
        paths = []
        self.assertFalse(self.command.is_enabled(paths))


if __name__ == "__main__":
    unittest.main()
