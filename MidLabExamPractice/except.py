class InsufficientFundsError(Exception):
    """Raised when a withdrawal amount exceeds the account balance."""
    pass

class InvalidMarksError(Exception):
    """Raised when inputted marks fall outside the standard 0-100 range."""
    pass

def process_student_marks(marks_input):
    """Validates marks using the full exception handling lifecycle."""
    print(f"--- Processing Input: '{marks_input}' ---")

    try:
        # 1. The TRY Block: Attempt the risky operation
        marks = float(marks_input)

        # Enforce business rules by raising our custom error
        if marks < 0 or marks > 100:
            raise InvalidMarksError(f"Marks must be between 0 and 100. Received: {marks}")

    except ValueError:
        # 2a. EXCEPT Block: Catch built-in Python typing errors
        print("Failure: Input must be a valid numeric value.")

    except InvalidMarksError as e:
        # 2b. EXCEPT Block: Catch our specific business logic violation
        print(f"Policy Violation: {e}")

    else:
        # 3. The ELSE Block: Runs ONLY if no exceptions were raised whatsoever
        print(f"Success: Student marks mathematically validated as {marks}.")
        # Real-world use case: This is where you would commit to the database.

    finally:
        # 4. The FINALLY Block: ALWAYS runs, whether it succeeded or crashed
        print("Cleanup: Releasing memory and closing input stream.\n")


# Execution Examples
process_student_marks("85")  # Triggers Try -> Else -> Finally
process_student_marks("150")  # Triggers Try -> Except (InvalidMarks) -> Finally
process_student_marks("abc")  # Triggers Try -> Except (ValueError) -> Finally