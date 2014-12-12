# -*- coding: utf-8  -*-
"""Tests for the Tk UI."""
#
# (C) Pywikibot team, 2008-2014
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id$'

import os
import sys

if os.environ.get('PYWIKIBOT2_TEST_GUI', '0') == '1':
    if sys.version_info[0] > 2:
        import tkinter as Tkinter
    else:
        import Tkinter
import pywikibot
from scripts import flickrripper
from pywikibot.userinterfaces.gui import EditBoxWindow

from tests.aspects import unittest, TestCase, DefaultSiteTestCase


class TestFlickrRipper(TestCase):

    """Test Tkdialog."""

    net = True

    @classmethod
    def setUpClass(cls):
        if os.environ.get('PYWIKIBOT2_TEST_GUI', '0') != '1':
            raise unittest.SkipTest('FlickrRipper tests are disabled on Travis-CI')
        super(TestFlickrRipper, cls).setUpClass()

    def testTkdialog(self):
        box = flickrripper.Tkdialog('foo', 'tests/data/MP_sounds.png', 'MP_sounds.png')
        box.run()


class TestTkinter(DefaultSiteTestCase):

    """Test Tkinter."""

    net = True

    @classmethod
    def setUpClass(cls):
        if os.environ.get('PYWIKIBOT2_TEST_GUI', '0') != '1':
            raise unittest.SkipTest('Tkinter tests are disabled on Travis-CI')
        super(TestTkinter, cls).setUpClass()

    def testTkinter(self):
        root = Tkinter.Tk()
        root.resizable(width=Tkinter.FALSE, height=Tkinter.FALSE)
        root.title("pywikibot GUI")
        page = pywikibot.Page(pywikibot.Site(), u'Main Page')
        content = page.get()
        myapp = EditBoxWindow(root)
        myapp.bind("<Control-d>", myapp.debug)
        v = myapp.edit(content, highlight=page.title())
        assert v is None


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
