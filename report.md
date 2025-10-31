#  Report


Author: Rebecca Yan


## Security Report
- *What you sent*: ```bash<script>alert(1)</script>```

- *What happened in the browser*: The browser executed the JavaScript code and displayed an alert popup with "1". This demonstrated that the malicious script was not just displayed as text, but was actually executed by the browser.
- *Why the server was vulnerable*: Lack of Input Encoding and Missing Content Security Policy, they allowed people to attack the website easily


## Pytest
```bash
(.venv) a86133@unknown2e2a699de723 procedures-lab % pytest -vvv
================================ test session starts ================================
platform darwin -- Python 3.14.0, pytest-7.4.2, pluggy-1.6.0 -- /Users/a86133/opencs/procedures-lab/procedures-lab/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/a86133/opencs/procedures-lab/procedures-lab
configfile: pytest.ini
collected 8 items                                                                   

tests/test_endpoints.py::test_add_endpoint PASSED                             [ 12%]
tests/test_endpoints.py::test_fib_endpoint PASSED                             [ 25%]
tests/test_endpoints.py::test_item_crud PASSED                                [ 37%]
tests/test_endpoints.py::test_vulnerable_echo_reflection SKIPPED (Reflection
test ignored because fixed test passes)                                       [ 50%]
tests/test_endpoints.py::test_vulnerable_echo_fixed PASSED                    [ 62%]
tests/test_utils.py::test_add_simple PASSED                                   [ 75%]
tests/test_utils.py::test_fib_basic PASSED                                    [ 87%]
tests/test_utils.py::test_db_crud PASSED                                      [100%]

=========================== 7 passed, 1 skipped in 0.02s ============================

```