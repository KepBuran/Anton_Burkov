Feature: Login

    Scenario: Login to OrangeHRM
        Given I launch chrome browser
        When I open orange hrm homepage
        And Enter username and password
        And Click on login button
        Then User must successfully login to the Dashboard page
