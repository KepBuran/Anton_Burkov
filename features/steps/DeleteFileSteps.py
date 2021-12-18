from __future__ import annotations
from behave import *
import sys
import pathlib


sys.path.insert(1, pathlib.Path(__file__).parent.parent.resolve())

from Request import DeleteFile


from abc import ABC, abstractmethod
from typing import Any

class DeleteFileSteps():
    def __init__(self):
        self.Builder = DeleteFile()
        self.response = ''

    @given(u'/Burkov_Lab7/angy-bladerunner.gif is at Dropbox')
    def set_file_path(self):
        self.Builder.set_body("/Burkov_Lab7/angry-bladerunner.gif")
        self.Builder.set_auth()
        self.Builder.add_header("Content-Type", "application/json")


    @when(u'I send POST request to Dropbox https://api.dropboxapi.com/2/files/delete_v2')
    def send_request(self):
        self.response = self.Builder.send_request('https://api.dropboxapi.com/2/files/delete_v2')


    @then(u'I should get the response "200 OK"')
    def check_response(self):
        if "<Response [200]>" == str(self.response):
            return 0
        else:
            return 1

    def test(self):
        self.set_file_path()
        self.send_request()
        return self.check_response()
