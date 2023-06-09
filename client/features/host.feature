Feature: Python Host-Client BDD tests

  @ci
  Scenario: List instances on host
    Given host is running
    When asked for instances
    Then host is still running

  @ci
  Scenario: List sequences on host
    Given host is running
    When asked for sequences
    Then host is still running

  @ci
  Scenario: Give version from host
    Given host is running
    When asked for version
    Then returns response with version
    Then host is still running

  @ci
  Scenario: Send sequence to host
    Given host is running
    When sequence ../test_sequences/python-alice.tar.gz loaded
    Then returns response with Client: SequenceClient
    Then host is still running

  @ci
  Scenario: Get sequence from host
    Given host is running
    When sequence ../test_sequences/python-alice.tar.gz loaded
    When - sequence get info
    Then returns response with id
    Then host is still running

  @ci 
  Scenario: Delete sequence from host
    Given host is running
    When sequence ../test_sequences/python-alice.tar.gz loaded
    When - sequence deleted
    Then returns response with id
    Then host is still running
