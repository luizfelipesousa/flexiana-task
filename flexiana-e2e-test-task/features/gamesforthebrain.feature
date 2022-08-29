Feature: E2E Game testing

  Scenario: Simple checkers game test
        Given start a new game by restarting
        When make your first move
        And let computer move
        When make your second move
        And let computer take your piece
        Then make sure your piece is taken
        And start a new game