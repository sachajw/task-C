import nox


@nox.session(python=["3.8"])
def test(session):
    """Run the test suite"""
    session.install("-r", "requirements.txt")
    session.run("pytest","app/bubble-sort.py", "--collect-only")


@nox.session(python="3.8")
def lint(session):
    """Run the lint suite"""
    session.install("-r", "requirements.txt")
    session.run("flake8", "app/bubble-sort.py")


@nox.session(python=["3.8"])
def coverage(session):
    """Run the coverage suite"""
    session.install("-r", "requirements.txt")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report")
