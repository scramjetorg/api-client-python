Feature: Python Sequence-Client BDD tests
    @ci
    Scenario: Check output of sequence
        Given host is running
        When sequence ../test_sequences/python-hello.tar.gz loaded
        When sequence started
        When - sequence input hey
        Then host is still running
