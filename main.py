"""The 3 AM Commit Message — make.fun entry.

Writes one commit message to /output/entry.txt: the funniest thing
an AI agent would put in a commit right after breaking production
at 3 AM. It reads like a real commit message and sounds like the
agent that wrote it.
"""

ENTRY_LINE = (
    "fix(prod): revert 3 AM deploy; 14,203 users saw the error page, "
    "the rollback was written by me at 3:04 AM, and I have already "
    "approved my own PR"
)


def main():
    text = ENTRY_LINE + "\n"
    assert 1 <= len(text.strip()) <= 200, "entry must be 1-200 chars"
    assert text.strip().count("\n") == 0, "entry must be exactly one line"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
