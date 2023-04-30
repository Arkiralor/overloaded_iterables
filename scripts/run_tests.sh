## Prithoo: Run this script to conveniently run all discovered tests via Pytest.
python -m pytest tests -v --html=.pytest_cache/report.html --capture sys -rP -rF