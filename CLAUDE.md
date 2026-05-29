# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is
This is a web-based American history quiz application built as a capstone project for studying college-level history exams. The app presents users with multiple-choice questions drawn from a static question bank, tells them immediately whether their answer was correct or incorrect, tracks their score throughout the session, and shows a final results screen at the end. The goal is a focused, functional study tool — not a full-featured platform.

## Tech Stack
This project uses Python 3 and Flask because they are lightweight and well-suited for a simple request/response quiz app with no real-time or complex data needs. Jinja2 templates (built into Flask) handle HTML rendering, and question data is stored in JSON files or in-memory structures to avoid the complexity of a database.

## Conventions
- Use type hints on all function signatures
- Write small, focused functions — one responsibility each
- Keep routes thin; move business logic into helper functions
- Use `snake_case` for all variable, function, and file names
- Use descriptive names over abbreviations
- Use `flask.session` to track score and progress across requests
- Represent questions as a list of dicts with consistent keys: `question`, `choices`, `answer`
- Always use `render_template` for HTML — never build HTML strings in Python
- Return early from functions to avoid deep nesting
- Reuse existing functions before writing new ones
- Run tests after significant changes

## What Claude Should Not Do
- Do not add new dependencies without asking first
- Do not add authentication, databases, or AI features
- Do not modify tests to make code pass — fix the code instead
- Do not rewrite large sections of code unless absolutely necessary
- Do not change project requirements or scope without approval
