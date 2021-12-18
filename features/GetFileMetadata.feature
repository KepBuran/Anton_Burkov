Feature: GetFileMetadata
	Get file metadata

Scenario Outline: Get file metadata
	Given <file> is uploaded to Dropbox
	When I send POST request to Dropbox <endpoint>
	Then I should get a response "200 OK"
	Examples: 
		| file                              | endpoint                                               |
		| /Burkov_Lab7/angy-bladerunner.gif | https://api.dropboxapi.com/2/sharing/get_file_metadata |