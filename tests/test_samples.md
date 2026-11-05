
# Test Results

Python version used: 3.__
Operating system: Windows
Date: 2026-11-05

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No listed warning signs | | |
| 2 | http://192.0.2.10/account | IP address + HTTP | | |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | | |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | | |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | | |

## Notes

Write what you learned from testing the five sample URLs.
