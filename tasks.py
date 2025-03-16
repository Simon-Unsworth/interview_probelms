from invoke import task


@task
def format_code(c):
    """Run black to format the code."""
    c.run("black src")


@task
def type_check(c):
    """Run mypy to check types."""
    c.run("mypy src --strict")


@task(pre=[format_code, type_check])
def validate(c):
    """Format code and check types."""
    print("Code formatted and type-checked successfully!")
