Feature: DeleteFile
	Delete file

Scenario Outline: Delete file
	Given <file> is at Dropbox
	When I send POST request to Dropbox <endpoint>
	Then I should get the response "200 OK"
	Examples: 
		| file                | endpoint                                     |
		| /Lab7WebAPI/dog.png | https://api.dropboxapi.com/2/files/delete_v2 |