#!/usr/bin/env python3
"""Validate the studio's structural and safety contracts."""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".codex" / "agents"
TEMPLATE_DIR = ROOT / "clients" / "_template"

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "DISCLAIMER.md",
    "company/ORG_CHART.md",
    "company/ROLE_CATALOG.md",
    "playbooks/START_HERE.md",
    "playbooks/ENGAGEMENT_LIFECYCLE.md",
    "playbooks/COACHING.md",
    "playbooks/CURRICULUM.md",
    "playbooks/TOOLS.md",
    "docs/USING_CODEX.md",
]

REQUIRED_TEMPLATE_FILES = [
    "README.md",
    "BRIEF.md",
    "TEAM.md",
    "RESEARCH.md",
    "DECISION_LOG.md",
    "PRODUCT_STRATEGY.md",
    "PRD.md",
    "ROADMAP.md",
    "METRICS.md",
    "COACHING_LOG.md",
    "RETROSPECTIVE.md",
    "design/README.md",
    "delivery/README.md",
    "delivery/BUILD_LOG.md",
]

DISCLAIMER_PARTS = (
    "Fictional educational exercise.",
    "did not request this work",
    "not affiliated with CPO Practice Studio.",
)

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def normalized_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def has_disclaimer(path: Path) -> bool:
    if not path.is_file():
        return False
    text = normalized_text(path)
    return all(part in text for part in DISCLAIMER_PARTS)


def validate() -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    agents_path = ROOT / "AGENTS.md"
    if agents_path.is_file() and agents_path.stat().st_size > 32 * 1024:
        errors.append("AGENTS.md exceeds Codex's default 32 KiB instruction limit")

    for relative in REQUIRED_TEMPLATE_FILES:
        if not (TEMPLATE_DIR / relative).is_file():
            errors.append(f"missing client-template file: {relative}")

    for relative in ("README.md", "BRIEF.md"):
        path = TEMPLATE_DIR / relative
        if not has_disclaimer(path):
            errors.append(f"client template lacks complete disclaimer: {relative}")

    profiles = sorted(AGENT_DIR.glob("*.toml"))
    if len(profiles) < 20:
        errors.append(f"expected at least 20 agent profiles, found {len(profiles)}")

    names: dict[str, Path] = {}
    required_keys = ("name", "description", "developer_instructions")
    for profile in profiles:
        try:
            data = tomllib.loads(profile.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"invalid TOML in {profile.relative_to(ROOT)}: {exc}")
            continue

        for key in required_keys:
            value = data.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{profile.relative_to(ROOT)} has no non-empty {key}")

        name = data.get("name")
        if isinstance(name, str) and name.strip():
            if name in names:
                errors.append(
                    f"duplicate agent name {name!r}: "
                    f"{names[name].relative_to(ROOT)} and {profile.relative_to(ROOT)}"
                )
            else:
                names[name] = profile

    clients_dir = ROOT / "clients"
    if clients_dir.is_dir():
        for engagement in sorted(clients_dir.iterdir()):
            if not engagement.is_dir() or engagement.name.startswith("_"):
                continue
            for relative in ("README.md", "BRIEF.md"):
                path = engagement / relative
                if not has_disclaimer(path):
                    errors.append(
                        f"engagement lacks complete disclaimer: "
                        f"{path.relative_to(ROOT)}"
                    )

    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_target = unquote(target.split("#", 1)[0])
            if not (markdown.parent / local_target).exists():
                errors.append(
                    f"broken local Markdown link in {markdown.relative_to(ROOT)}: "
                    f"{raw_target}"
                )

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    profile_count = len(list(AGENT_DIR.glob("*.toml")))
    engagement_count = len(
        [
            path
            for path in (ROOT / "clients").iterdir()
            if path.is_dir() and not path.name.startswith("_")
        ]
    )
    print(
        "Repository validation passed: "
        f"{profile_count} agent profiles, {engagement_count} practice engagements."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
