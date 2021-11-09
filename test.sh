set -e
export PYTHONPATH=$(pwd)/src:$(pwd)/test
cd build/test
my_tests
