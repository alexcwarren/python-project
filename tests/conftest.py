import pytest

def pytest_addoption(parser):
    parser.addoption("--keep-test-dir", action="store_true")

@pytest.fixture
def project_path(request: pytest.FixtureRequest) -> str:
    """TODO"""
    return str(request.config.rootpath)
