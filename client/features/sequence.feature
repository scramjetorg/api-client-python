Feature: Python Sequence-Client BDD tests
    @ci
    Scenario: List sequences on host
        Given host is running
        When sequence ../refapps/python-alice.tar.gz loaded
        When sequence started
        Then host is still running
