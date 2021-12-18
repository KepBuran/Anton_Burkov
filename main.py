from features.steps.GetFileMetadataSteps import GetFileMetadataSteps
from features.steps.DeleteFileSteps import DeleteFileSteps
from features.steps.UploadFileSteps import UploadFileSteps

def test_UploadFile():
    assert 0 == UploadFileSteps().test()

def test_GetFileMetadata():
    assert 0  == GetFileMetadataSteps().test()

def test_DeleteFile():
    assert 0 == DeleteFileSteps().test()
