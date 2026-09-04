import io
import unittest
import urllib.error
from unittest.mock import MagicMock, patch

from scripts.check_links import check_url


class LinkCheckerTests(unittest.TestCase):
    @patch("scripts.check_links.urllib.request.urlopen")
    def test_successful_response_is_reachable(self, urlopen):
        response = MagicMock()
        response.getcode.return_value = 200
        urlopen.return_value.__enter__.return_value = response

        self.assertEqual(check_url("https://example.com"), (True, "200"))

    @patch("scripts.check_links.urllib.request.urlopen")
    def test_restricted_response_is_not_reported_as_broken(self, urlopen):
        urlopen.side_effect = urllib.error.HTTPError(
            "https://example.com", 403, "Forbidden", {}, io.BytesIO()
        )

        self.assertEqual(
            check_url("https://example.com"),
            (True, "403 (restricted)"),
        )

    @patch("scripts.check_links.time.sleep")
    @patch("scripts.check_links.urllib.request.urlopen")
    def test_missing_page_retries_and_fails(self, urlopen, sleep):
        urlopen.side_effect = urllib.error.HTTPError(
            "https://example.com/missing", 404, "Not Found", {}, io.BytesIO()
        )

        self.assertEqual(
            check_url("https://example.com/missing", attempts=2),
            (False, "HTTP 404"),
        )
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(1)


if __name__ == "__main__":
    unittest.main()
