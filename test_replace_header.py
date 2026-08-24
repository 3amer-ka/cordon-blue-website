import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from replace_header import process_file, new_header

class TestReplaceHeader(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="<html><body>No header here</body></html>")
    @patch("sys.stdout", new_callable=StringIO)
    def test_no_header(self, mock_stdout, mock_file):
        process_file("index.html")
        self.assertIn("Could not find header", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_projects_div_match(self, mock_stdout):
        content = """<header>
<div class="flex items-center gap-3">
<div class="size-10 bg-primary foo bar"></div>
</div>
</header>"""
        with patch("builtins.open", mock_open(read_data=content)) as mock_file:
            process_file("projects.html")
            self.assertIn("Successfully updated", mock_stdout.getvalue())

            # Extract the content written to the file
            handle = mock_file()
            written_content = "".join(call[0][0] for call in handle.write.call_args_list)

            self.assertIn(new_header, written_content)
            self.assertNotIn('<div class="size-10', written_content)

    @patch("sys.stdout", new_callable=StringIO)
    def test_other_div_match(self, mock_stdout):
        content = """<header>
<div class="flex items-center gap-3">
<div class="flex items-center justify-center bg-primary foo bar"></div>
<span class="text-xl font-bold tracking-tight text-slate-900 dark:text-white uppercase">Cordon Blue Global Services Ltd.</span>
</div>
</header>"""
        with patch("builtins.open", mock_open(read_data=content)) as mock_file:
            process_file("index.html")
            self.assertIn("Successfully updated", mock_stdout.getvalue())

            handle = mock_file()
            written_content = "".join(call[0][0] for call in handle.write.call_args_list)

            self.assertIn(new_header, written_content)
            self.assertNotIn("Cordon Blue Global Services Ltd.", written_content)

    @patch("builtins.open", new_callable=mock_open, read_data="<header>\n<div>Wrong div</div>\n</header>")
    @patch("sys.stdout", new_callable=StringIO)
    def test_no_div_match(self, mock_stdout, mock_file):
        process_file("index.html")
        self.assertIn("Could not find matching div", mock_stdout.getvalue())

        handle = mock_file()
        handle.write.assert_not_called()

if __name__ == '__main__':
    unittest.main()
