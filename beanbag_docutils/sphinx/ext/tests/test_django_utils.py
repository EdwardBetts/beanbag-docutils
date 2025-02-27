"""Unit tests for beanbag_docutils.sphinx.ext.django_utils."""

from beanbag_docutils.sphinx.ext.tests.testcase import SphinxExtTestCase


class DjangoUtilsTests(SphinxExtTestCase):
    """Unit tests for Django doc utilities."""

    extensions = [
        'beanbag_docutils.sphinx.ext.django_utils',
    ]

    def test_setting_crossref(self):
        """Testing Django :setting: crossref"""
        rendered = self.render_doc(
            '.. setting:: MY_TEST\n'
            '\n'
            'Some content.\n'
            '\n'
            'Now link to :setting:`MY_TEST`.'
        )

        self.assertEqual(
            rendered,
            (
                '<p id="std-setting-MY_TEST">Some content.</p>\n'
                '<p>Now link to <a class="reference internal"'
                ' href="#std-setting-MY_TEST"><code class="xref std'
                ' std-setting docutils literal notranslate">'
                '<span class="pre">MY_TEST</span></code></a>.</p>'
            )
        )
