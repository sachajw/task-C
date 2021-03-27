import nox


@nox.session(python=["3.8"])
def test(session):
    session.install("-r", "requirements.txt")
    """Run the test suite"""
    session.run("pytest","app/bubble-sort.py", "--collect-only")


@nox.session(python="3.8")
def lint(session):
    session.install("-r", "requirements.txt")
    """Run the lint suite"""
    session.run("flake8", "app/bubble-sort.py")


@nox.session(python=["3.8"])
def coverage(session):
    """Run the coverage suite"""
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report")
