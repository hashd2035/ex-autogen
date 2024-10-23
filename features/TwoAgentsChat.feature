Feature: Two Agents Chat
  # Enter feature description here

  Scenario:
        Given a calculator
        When I input <num1> and <num2>
        Then the result of "<operation>" should be <expected_result>

#Feature: Calculator
#    Scenario Outline: Basic arithmetic operations
#        Given a calculator
#        When I input <num1> and <num2>
#        Then the result of "<operation>" should be <expected_result>
#
#    Examples:
#        | num1 | num2 | operation   | expected_result |
#        | 1    | 2    | add         | 3               |
#        | 5    | 3    | subtract    | 2               |
#        | 6    | 2    | multiply    | 12              |
#        | 8    | 4    | divide      | 2               |
#        | 10   | 0    | divide      | ValueError      |
