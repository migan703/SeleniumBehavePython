Feature: Enter facebook's website with a new user

  Scenario: Enter to the website with a new woman's account
    Given I am in Facebook page 
    When I create a new user for a woman
    Then I can log into Facebook as a woman

  Scenario: Enter to the website with a new man's account
    Given I am in Facebook page 
    When I create a new user for a man
    Then I can log into Facebook as a man