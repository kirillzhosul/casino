"""
Casino App Runner.
"""

# Importing.

# System.
import os
import sys

# Application.
import app


def typescript_compile():
    """
    Compiles TypeScript using `tsc` command.
    """

    # Compile.
    os.chdir(os.path.join(os.path.dirname(__file__), "..").replace("\\", "/"))
    os.system("tsc")


if __name__ == "__main__":
    # Entry point.

    if len(sys.argv) == 0 or sys.argv[0] != "-tsc":
        # If -tsc is not passed.

        # Compile TypeScript.
        print("Compiling TypeScript...")
        typescript_compile()

    # Running.
    print("Running Flask app...")
    app.create().run(debug=True, port=80)
