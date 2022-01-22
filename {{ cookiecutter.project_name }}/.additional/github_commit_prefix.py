#!/usr/bin/env python3

from typing import NoReturn

import argparse
import re
import subprocess  # nosec


def get_ticket_id_from_branch_name(branch):
    # Get first number from branch name
    matches = re.findall("[0-9]{1,5}", branch)
    if len(matches) > 0:
        return matches[0]


def main() -> NoReturn:
    parser = argparse.ArgumentParser()
    parser.add_argument("commit_msg_filepath")
    parser.add_argument(
        "-t",
        "--template",
        default="[{}]",
        help="Template to render ticket id into",
    )
    args = parser.parse_args()
    commit_msg_filepath = args.commit_msg_filepath
    template = args.template

    branch = ""
    try:
        branch = subprocess.check_output(  # nosec
            ["git", "symbolic-ref", "--short", "HEAD"],
            universal_newlines=True,
        ).strip()
    except Exception as e:
        print(e)
        return 1

    result = get_ticket_id_from_branch_name(branch)
    issue_number = ""

    if result:
        issue_number = result.upper()
        prefix = template.format("#" + issue_number)
    else:
        prefix = template.format(branch)

    with open(commit_msg_filepath, "r+") as f:
        content = f.read()
        content_subject = content.split("\n", maxsplit=1)[0].strip()
        f.seek(0, 0)
        if prefix not in content_subject:
            f.write(f"{prefix} {content}")
        else:
            # Write back
            f.write(content)


if __name__ == "__main__":
    exit(main())
