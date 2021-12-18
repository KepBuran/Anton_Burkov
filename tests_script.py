import pytest
from features.steps.GetFileMetadataSteps import GetFileMetadataSteps
from features.steps.DeleteFileSteps import DeleteFileSteps
from features.steps.UploadFileSteps import UploadFileSteps


assert 0 == UploadFileSteps().test()
assert 0 == GetFileMetadataSteps().test()
assert 0 == DeleteFileSteps().test()
print("Tests are passed successfuly")