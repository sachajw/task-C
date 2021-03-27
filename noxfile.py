import nox


@nox.session(python=["3.8"])
def test(session):
    session.install("-r", "requirements.txt")
    """Run the test suite"""
    session.run("pytest")


@nox.session(python="3.8")
def lint(session):
    session.install("-r", "requirements.txt")
    """Run the lint suite"""
#    session.run("flake8", "app/bubble-sort.py")
    session.run("black", "app/bubble-sort.py", "--check")
#    ignore = ("E117") #E203 E226 E302 E304 E305 E712 F401 W291 W293 
