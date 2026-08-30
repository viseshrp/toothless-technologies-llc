#!/usr/bin/env python3
"""Validate Greyshore's structural, authority, and representation contracts."""

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
    "playbooks/OPERATING_GUIDE.md",
    "playbooks/ENGAGEMENT_LIFECYCLE.md",
    "playbooks/BOARD_GOVERNANCE.md",
    "playbooks/PORTFOLIO_STRATEGY.md",
    "playbooks/TOOLS.md",
    "docs/USING_CODEX.md",
]

REQUIRED_TEMPLATE_FILES = [
    "README.md",
    "BRIEF.md",
    "QUALIFICATION.md",
    "TEAM.md",
    "RESEARCH.md",
    "DECISION_LOG.md",
    "PRODUCT_STRATEGY.md",
    "PRD.md",
    "ROADMAP.md",
    "METRICS.md",
    "BOARD_ADVISORY.md",
    "ENGAGEMENT_REVIEW.md",
    "design/README.md",
    "delivery/README.md",
    "delivery/BUILD_LOG.md",
]

DISCLOSURE_PARTS = (
    "Independent speculative work.",
    "not a client of",
    "Greyshore Product Partners",
    "did not request, review, or endorse this work.",
)

LEGACY_FRAMING_TERMS = (
    "tr" + "ain" + "ing",
    "co" + "ach",
    "prac" + "tice",
    "educa" + "tional",
    "learn" + "er",
    "learn" + "ing",
    "curric" + "ulum",
    "rub" + "ric",
    "exer" + "cise",
    "simu" + "lation",
    "simu" + "lated",
    "fic" + "tional",
    "te" + "ach",
    "men" + "tor",
)

TEXT_SUFFIXES = {".md", ".toml", ".py", ".yml", ".yaml"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def normalized_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def has_disclosure(path: Path) -> bool:
    if not path.is_file():
        return False
    text = normalized_text(path)
    return all(part in text for part in DISCLOSURE_PARTS)


def repository_text_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.suffix.lower() in TEXT_SUFFIXES
    )


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
            errors.append(f"missing account-template file: {relative}")

    for relative in ("README.md", "BRIEF.md"):
        path = TEMPLATE_DIR / relative
        if not has_disclosure(path):
            errors.append(f"account template lacks complete disclosure: {relative}")

    profiles = sorted(AGENT_DIR.glob("*.toml"))
    if len(profiles) != 30:
        errors.append(f"expected 30 agent profiles, found {len(profiles)}")

    board_profile = AGENT_DIR / "board-product-advisor.toml"
    if not board_profile.is_file():
        errors.append("missing independent Board product-advisor profile")

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
                if not has_disclosure(path):
                    errors.append(
                        f"engagement lacks complete disclosure: "
                        f"{path.relative_to(ROOT)}"
                    )

    for path in repository_text_files():
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for term in LEGACY_FRAMING_TERMS:
            if term in lowered:
                errors.append(
                    f"legacy company framing remains in {path.relative_to(ROOT)}: "
                    f"{term}"
                )

        if path.suffix.lower() != ".md":
            continue
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_target = unquote(target.split("#", 1)[0])
            if not (path.parent / local_target).exists():
                errors.append(
                    f"broken local Markdown link in {path.relative_to(ROOT)}: "
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
        f"{profile_count} agent profiles, {engagement_count} account engagements."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
