#!/usr/bin/env python3
"""Validate the company's structural, authority, and representation contracts."""

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
    "OPERATIONS.md",
    "DISCLAIMER.md",
    "company/ORG_CHART.md",
    "company/ROLE_CATALOG.md",
    "company/TEAM_PROJECTS.md",
    "company/team_projects.toml",
    "playbooks/OPERATING_GUIDE.md",
    "playbooks/ENGAGEMENT_LIFECYCLE.md",
    "playbooks/BOARD_GOVERNANCE.md",
    "playbooks/PORTFOLIO_STRATEGY.md",
    "playbooks/PROJECT_BOARDS.md",
    "playbooks/TOOLS.md",
    "docs/USING_CODEX.md",
    ".github/ISSUE_TEMPLATE/team-work-item.yml",
]

REQUIRED_TEMPLATE_FILES = [
    "README.md",
    "PROJECT_TRACKER.md",
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
    "Toothless Technologies LLC",
    "did not request, review, or endorse this work.",
)

LEGAL_STATUS_PARTS = (
    "Toothless Technologies LLC",
    "does not",
    "formed",
    "registered",
)

LEGACY_BRAND_TERMS = (
    "Grey" + "shore Product Partners",
    "Grey" + "shore",
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

    for relative in ("README.md", "DISCLAIMER.md"):
        path = ROOT / relative
        if path.is_file():
            text = normalized_text(path)
            if not all(part in text for part in LEGAL_STATUS_PARTS):
                errors.append(f"missing company legal-status notice: {relative}")

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

    team_projects_path = ROOT / "company" / "team_projects.toml"
    if team_projects_path.is_file():
        try:
            team_data = tomllib.loads(team_projects_path.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"invalid team project manifest: {exc}")
        else:
            projects = team_data.get("projects")
            workflow = team_data.get("workflow")
            expected_statuses = [
                "Backlog",
                "Ready",
                "In progress",
                "Review",
                "Blocked",
                "Done",
            ]
            expected_fields = [
                "Workflow",
                "Priority",
                "Engagement",
                "Stage",
                "Work type",
                "Decision owner",
                "Repository path",
                "Depends on",
                "Last touched",
            ]
            if not isinstance(workflow, dict):
                errors.append("team project manifest lacks workflow configuration")
            else:
                if workflow.get("statuses") != expected_statuses:
                    errors.append("team project workflow statuses do not match the contract")
                if workflow.get("required_fields") != expected_fields:
                    errors.append("team project fields do not match the contract")

            if not isinstance(projects, list) or len(projects) != 12:
                count = len(projects) if isinstance(projects, list) else 0
                errors.append(f"expected 12 functional projects, found {count}")
            else:
                assigned_agents: list[str] = []
                project_numbers: set[int] = set()
                project_urls: set[str] = set()
                for project in projects:
                    if not isinstance(project, dict):
                        errors.append("team project manifest contains a non-table entry")
                        continue
                    for key in ("key", "name", "number", "url", "accountable_role"):
                        if key not in project:
                            errors.append(f"team project entry lacks {key}")

                    number = project.get("number")
                    if isinstance(number, int):
                        if number in project_numbers:
                            errors.append(f"duplicate team project number: {number}")
                        project_numbers.add(number)

                    url = project.get("url")
                    if isinstance(url, str):
                        if url in project_urls:
                            errors.append(f"duplicate team project URL: {url}")
                        project_urls.add(url)
                        if isinstance(number, int):
                            expected_url = (
                                "https://github.com/users/viseshrp/projects/"
                                f"{number}"
                            )
                            if url != expected_url:
                                errors.append(
                                    f"team project {number} has unexpected URL: {url}"
                                )

                    project_agents = project.get("agents")
                    if not isinstance(project_agents, list) or not all(
                        isinstance(agent, str) for agent in project_agents
                    ):
                        errors.append(
                            f"team project {project.get('key', '<unknown>')} has invalid agents"
                        )
                    else:
                        assigned_agents.extend(project_agents)

                duplicate_assignments = sorted(
                    agent for agent in set(assigned_agents)
                    if assigned_agents.count(agent) > 1
                )
                if duplicate_assignments:
                    errors.append(
                        "agents assigned to multiple functional projects: "
                        + ", ".join(duplicate_assignments)
                    )

                missing_assignments = sorted(set(names) - set(assigned_agents))
                unknown_assignments = sorted(set(assigned_agents) - set(names))
                if missing_assignments:
                    errors.append(
                        "agents missing from functional projects: "
                        + ", ".join(missing_assignments)
                    )
                if unknown_assignments:
                    errors.append(
                        "unknown agents in functional projects: "
                        + ", ".join(unknown_assignments)
                    )
                if project_numbers != set(range(2, 14)):
                    errors.append(
                        "functional project numbers must be exactly 2 through 13"
                    )

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
        for term in LEGACY_BRAND_TERMS:
            if term in text:
                errors.append(
                    f"legacy company name remains in {path.relative_to(ROOT)}: "
                    f"{term}"
                )
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
    team_project_count = 0
    team_projects_path = ROOT / "company" / "team_projects.toml"
    if team_projects_path.is_file():
        team_data = tomllib.loads(team_projects_path.read_text(encoding="utf-8"))
        projects = team_data.get("projects")
        if isinstance(projects, list):
            team_project_count = len(projects)
    engagement_count = len(
        [
            path
            for path in (ROOT / "clients").iterdir()
            if path.is_dir() and not path.name.startswith("_")
        ]
    )
    print(
        "Repository validation passed: "
        f"{profile_count} agent profiles, {team_project_count} functional projects, "
        f"{engagement_count} account engagements."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
