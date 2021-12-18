from __future__ import annotations
from behave import *
import sys
import pathlib


sys.path.insert(1, pathlib.Path(__file__).parent.parent.resolve())

from Request import UploadFile


from abc import ABC, abstractmethod
from typing import Any

class UploadFileSteps():
    def __init__(self):
        self.Builder = UploadFile()
        self.response = ''

    @given(u'I have some angy-bladerunner.gif i want to upload to /Burkov_Lab7/angy-bladerunner.gif')
    def set_file(self):
        with open(str(pathlib.Path(__file__).parent.resolve())+"/angy-bladerunner.gif", 'rb') as f:
            data = f.read()
        self.Builder.set_body(data)
        self.Builder.add_header("Dropbox-API-Arg", "{\"path\":\"/Burkov_Lab7/angry-bladerunner.gif\",\"mode\":\"add\"}")
        self.Builder.set_auth()
        self.Builder.add_header("Content-Type", "application/octet-stream")


    @when(u'I send POST request to Dropbox https://content.dropboxapi.com/2/files/upload')
    def send_request(self):
        self.response = self.Builder.send_request('https://content.dropboxapi.com/2/files/upload')


    @then(u'I should get response "200 OK"')
    def check_response(self):
        if "<Response [200]>" == str(self.response):
            return 0
        else:
            return 1

    def test(self):
        self.set_file()
        self.send_request()
        return self.check_response()
