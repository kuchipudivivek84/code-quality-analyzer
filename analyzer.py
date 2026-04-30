import tempfile
import subprocess
from radon.complexity import cc_visit

def analyze_code(code):
    issues = []

    # Save code to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
        temp.write(code.encode())
        temp_path = temp.name

    # Run pylint using subprocess
    result = subprocess.run(
        ["pylint", temp_path],
        capture_output=True,
        text=True
    )

    pylint_output = result.stdout

    # Extract and clean issues
    for line in pylint_output.split("\n"):
        if ":" in line:
            # Get only the message part (clean output)
            parts = line.split(":")
            if len(parts) > 3:
                issues.append(parts[-1].strip())

    # Complexity calculation
    complexity_blocks = cc_visit(code)
    complexity = sum(block.complexity for block in complexity_blocks)

    # ✅ Improved scoring logic
    score = 10

    # Deduct based on issues
    score -= min(len(issues), 5)

    # Deduct based on complexity
    if complexity > 10:
        score -= 3
    elif complexity > 5:
        score -= 2

    # Keep score between 1 and 10
    score = max(min(score, 10), 1)

    return score, issues[:5], complexity