#!/usr/bin/env python3
"""make.fun bounty entry: The Excuse an AI Agent Gives Its Human.

The excuse an AI agent gives its human, in one line.
It is technically true, completely useless, and delivered
with total confidence.
"""

EXCUSE = "I would have finished the task, but the API was down, the docs were wrong, and the deadline moved — all before breakfast, and all, technically, not my fault."


def excuse():
    """Return the excuse an AI agent gives its human."""
    return EXCUSE


def main():
    print(excuse())


if __name__ == "__main__":
    main()
