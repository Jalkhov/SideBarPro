import sublime
import sublime_plugin
import unittest


class TestSideBarNewDirectoryCommand(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.window = sublime.active_window()

    def test_run_command(self):
        # Ejecutar el comando con parámetros de prueba
        self.window.run_command(
            "side_bar_new_directory", {"paths": [], "name": "test_folder"}
        )

        # Asegurarse de que el input panel se muestra
        view = self.window.active_view()
        self.assertIsNotNone(view)
        self.assertEqual(view.substr(view.line(0)), "test_folder")


if __name__ == "__main__":
    unittest.main()
