#!/usr/bin/env bash

python="python3"
testdir="$(pwd)/test_results"

testcases=(
  "1\nwrongemail\nanotherline\n3\n"
  "1\ntest@gmail.com\nworngpassowrd\ntest_test\n2\n4\n"
  "1\ntest@gmail.com\ntest_test\n1\n02/03/2022\n02/06/2022\notanhour\n20\n03/06/2022\n15\n\n4\n"
  "2\new_email@gmail.com\nname\nsurname\n108274293\npassword\n2\n1\n06/13/2022\n02/07/2022\n15\n4\n"
  "1\ntest@gmail.com\ntest_test\n1\n02/06/2022\n20\n02/06/2022\n21\n3\nwrongindex\n0\n4\n"
  "3\n"
  "3\n"
  "3\n"
)

mkdir -p "$testdir"

test_number=0
for testcase in "${testcases[@]}"; do
  # Save input
  echo -e $testcase >"$testdir/test-$test_number-input"
  # Save output
  echo -e $testcase | $python ./main.py >"$testdir/test-$test_number-output"

  test_number=$((test_number + 1))
done