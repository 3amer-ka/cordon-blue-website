import unittest
from unittest.mock import patch, mock_open, MagicMock
from fix_replace_header import replace_header_content, main, NEW_HEADER

class TestFixReplaceHeader(unittest.TestCase):

    def test_replace_header_content_projects_match(self):
        # Arrange
        filepath = "projects.html"
        content = """<header>
<div class="flex items-center gap-3">
<div class="size-10 bg-primary rounded-lg flex items-center justify-center text-white">
<img src="foo">
</div>
<div>
<h2>Cordon Blue Global Services Ltd.</h2>
<p>Global Services Ltd.</p>
</div>
</div>
</header>"""

        # Act
        new_content, changed = replace_header_content(filepath, content)

        # Assert
        self.assertTrue(changed)
        self.assertIn(NEW_HEADER, new_content)
        self.assertNotIn("<h2>Cordon Blue Global Services Ltd.</h2>", new_content)

    def test_replace_header_content_other_match(self):
        # Arrange
        filepath = "index.html"
        content = """<header>
<div class="flex items-center gap-3">
<div class="flex items-center justify-center bg-primary p-2 rounded-xl shadow-lg shadow-primary/20">
<span class="material-symbols-outlined text-white text-2xl">architecture</span>
</div>
<span class="text-xl font-bold tracking-tight text-slate-900 dark:text-white uppercase">Cordon Blue Global Services Ltd.</span>
</div>
</header>"""

        # Act
        new_content, changed = replace_header_content(filepath, content)

        # Assert
        self.assertTrue(changed)
        self.assertIn(NEW_HEADER, new_content)
        self.assertNotIn("uppercase\">Cordon Blue Global Services Ltd.</span>", new_content)

    def test_replace_header_content_no_match(self):
        # Arrange
        filepath = "index.html"
        content = """<header><div>Something else</div></header>"""

        # Act
        new_content, changed = replace_header_content(filepath, content)

        # Assert
        self.assertFalse(changed)
        self.assertEqual(content, new_content)

    @patch('fix_replace_header.replace_header_content')
    @patch('builtins.open', new_callable=mock_open, read_data="mock data")
    @patch('sys.stdout', new_callable=MagicMock)
    def test_main_file_updated(self, mock_stdout, mock_file, mock_replace):
        # Arrange
        # Force the first file to trigger a change, the rest not
        def mock_replace_side_effect(filepath, content):
            if filepath == "index.html":
                return "new data", True
            return content, False

        mock_replace.side_effect = mock_replace_side_effect

        # Act
        main()

        # Assert
        self.assertEqual(mock_replace.call_count, 3) # Called for index, projects, services
        mock_file.assert_any_call('index.html', 'w')
        # Check that it writes the new content for the first file
        handle = mock_file()
        handle.write.assert_called_with("new data")
        # Ensure that projects and services are not written to

        # Verify stdout output
        stdout_calls = [call.args[0] for call in mock_stdout.write.call_args_list if call.args[0] != '\n']
        self.assertIn("Successfully updated index.html", stdout_calls)
        self.assertIn("Could not find matching div in projects.html", stdout_calls)
        self.assertIn("Could not find matching div in services.html", stdout_calls)

    @patch('builtins.open', side_effect=FileNotFoundError())
    @patch('sys.stdout', new_callable=MagicMock)
    def test_main_file_not_found(self, mock_stdout, mock_file):
        # Act
        main()

        # Assert
        # Verify stdout output
        stdout_calls = [call.args[0] for call in mock_stdout.write.call_args_list if call.args[0] != '\n']
        self.assertIn("File not found: index.html", stdout_calls)
        self.assertIn("File not found: projects.html", stdout_calls)
        self.assertIn("File not found: services.html", stdout_calls)

if __name__ == '__main__':
    unittest.main()
