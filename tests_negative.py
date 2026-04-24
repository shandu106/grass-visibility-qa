from logic import calculate_visibility

def create_bug_report(name, expected, actual):
    print("\n======================")
    print("BUG REPORT")
    print("======================")
    print(f"Title: {name}")
    print("Severity: HIGH")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print("======================\n")


results = []

def run_test(name, actual, expected):
    passed = actual == expected
    results.append((name, passed))

    if not passed:
        create_bug_report(name, expected, actual)

    return passed


print("NEGATIVE TEST RUN STARTED\n")

run_test(
    "Sprint should NOT be HIDDEN in any case",
    calculate_visibility(0.9, 2, True, "night"),
    "HIDDEN"

)

run_test(
    "Low grass crouch should NOT become HIDDEN",
    calculate_visibility(0.2, 0, True, "day"),
    "VISIBLE"
)

run_test(
    "Night should NOT break sprint visibility",
    calculate_visibility(0.8, 2, False, "night"),
    "VISIBLE"
)

# ---------------- REPORT ----------------
print("\n======================")
print("QA TEST REPORT")
print("======================\n")

total = len(results)
passed = sum(1 for r in results if r[1])
failed = total - passed
success_rate = (passed / total) * 100

print(f"Total tests: {total}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Success rate: {success_rate:.0f}%")

print("\nSTATUS:", "PASS ✔" if failed == 0 else "FAIL ❌")


