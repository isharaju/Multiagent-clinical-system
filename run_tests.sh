#!/bin/bash

# Ensure the script is executable
# If running below in bash works, it means it is executable:
#   ./run_tests.sh
#
# If not, run below in bash to make it executable:
#   chmod +x run_tests.sh

# Script to run all clinical trials agent tests sequentially
echo "🔧 Running Clinical Trials Agent Tests..."
echo "========================================="

# Ensure we're in project root
cd "$(dirname "$0")"

# Activate virtual environment if needed (optional)
# Condat activate env_a06

# List of test modules
tests=(
    "tests.test_clinical_trials"
    "tests.test_eligibility_parser"
    "tests.test_geopy_tool"
    "tests.test_summary_generator"
    "tests.test_end_to_end"
)

# Run each test sequentially
for test in "${tests[@]}"; do
    echo "▶️ Running: $test"
    python -m $test
    if [ $? -ne 0 ]; then
        echo "❌ Test failed: $test"
        exit 1
    else
        echo "✅ Passed: $test"
        echo "-----------------------------------------"
    fi
done

echo "🎉 All tests passed successfully!"


