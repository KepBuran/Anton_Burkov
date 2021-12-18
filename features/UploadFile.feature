Feature: UploadFile
  Uploads file to Dropbox

  Scenario Outline: Upload some file
    Given I have some <file> i want to upload to <directory>
    When I send POST request to Dropbox <endpoint>
    Then I should get response "200 OK"
    Examples:
      | file                 | directory                         | endpoint                                      |
      | angy-bladerunner.gif | /Burkov_Lab7/angy-bladerunner.gif | https://content.dropboxapi.com/2/files/upload |