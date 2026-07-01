#!/usr/bin/env python3
"""CLI entry point for the LangChain refund agent."""

from __future__ import annotations

import contextlib
import sys

from agent import invoke


def main() -> int:
    prompt = sys.argv[1] if len(sys.argv) > 1 else ""
    if not prompt:
        print('Missing prompt. Usage: python run_agent.py "Refund order 123"', file=sys.stderr)
        return 1

    # LangChain verbose logs use stdout; keep stdout clean for piping.
    with contextlib.redirect_stdout(sys.stderr):
        answer = invoke(prompt)

    print(answer)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
