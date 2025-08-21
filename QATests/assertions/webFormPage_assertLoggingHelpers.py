import logging

logger = logging.getLogger(__name__)

# Default value, overridden by pytest config
_USE_SOFT_ASSERTS = True

def set_global_soft_asserts(value: bool):
    global _USE_SOFT_ASSERTS
    _USE_SOFT_ASSERTS = value

# This is for soft assertions using a singleton pattern for tracking assertions
class AssertTracker:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AssertTracker, cls).__new__(cls)
            cls._instance.reset()
        return cls._instance

    def reset(self):
        self.assertions = []

    def log_assert(self, passed, requirement_id, description, actual=None, expected=None):
        result = {
            "requirement_id": requirement_id,
            "description": description,
            "passed": passed,
            "actual": actual,
            "expected": expected
        }
        self.assertions.append(result)

        status = "✅ PASS" if passed else "❌ FAIL"
        msg = f"[{requirement_id}] {description}"
        if actual is not None and expected is not None:
            msg += f" | Expected: {expected}, Got: {actual}"
        log_method = logger.info if passed else logger.error
        log_method(f"{status} - {msg}")

    def assert_all(self):
        failed = [a for a in self.assertions if not a["passed"]]
        if failed:
            messages = []
            for a in failed:
                msg = f"[{a['requirement_id']}] {a['description']} | Expected: {a['expected']}, Got: {a['actual']}"
                messages.append(msg)
            raise AssertionError("Soft assertion failures:\n" + "\n".join(messages))

# A helper class for commonly used assertions
class AssertHelper:

    @staticmethod
    def equal(actual, expected, requirement_id, description, fail_message=None, soft=None):
        tracker = AssertTracker()
        passed = actual == expected
        tracker.log_assert(passed, requirement_id, description, actual, expected)

        # Use global setting if soft is not explicitly provided
        effective_soft = _USE_SOFT_ASSERTS if soft is None else soft

        if not passed and not effective_soft:
            fail_text = fail_message or f"{description} | Expected: {expected}, Got: {actual}"
            raise AssertionError(f"❌ [{requirement_id}] {fail_text}")

    @staticmethod
    def lessThanOrEqual(actual, expected, requirement_id, description, fail_message=None, soft=None):
        tracker = AssertTracker()
        passed = actual <= expected
        tracker.log_assert(passed, requirement_id, description, actual, expected)

        # Use global setting if soft is not explicitly provided
        effective_soft = _USE_SOFT_ASSERTS if soft is None else soft

        if not passed and not effective_soft:
            fail_text = fail_message or f"{description} | Expected: {expected}, Got: {actual}"
            raise AssertionError(f"❌ [{requirement_id}] {fail_text}")

    @staticmethod
    def true(condition, requirement_id, description, fail_message=None, soft=None):
        tracker = AssertTracker()
        passed = bool(condition)
        tracker.log_assert(passed, requirement_id, description)

        # Use global setting if soft is not explicitly provided
        effective_soft = _USE_SOFT_ASSERTS if soft is None else soft

        if not passed and not effective_soft:
            fail_text = fail_message or f"{description} | Condition evaluated to False"
            raise AssertionError(f"❌ [{requirement_id}] {fail_text}")

    # Add other assertion types as needed...
