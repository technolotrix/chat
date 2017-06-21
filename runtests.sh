#! /bin/bash
source .env
nosetests -vs tests/

# To only run critical tests
# nosetests -vs -a priority=critical tests/

# To run tests that are known to pass (skip ones that are failing due to known bugs)
# nosetests -vs -a priority=critical tests/