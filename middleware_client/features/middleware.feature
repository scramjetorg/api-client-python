Feature: Python Middleware BDD tests

  @prod
  @ci
  Scenario: List managers
    Given host is running
    When asked for managers
    Then returns response with managers
    Then host is still running

  @prod
  @ci
  Scenario: Get manager object
    Given host is running
    When asked for managers
    When asked for manager -
    Then returns response with Client: ManagerClient
    Then host is still running

