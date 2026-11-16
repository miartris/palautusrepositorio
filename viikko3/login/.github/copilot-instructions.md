# Copilot instructions for this repository

## Project overview
This repository is a small Flask-based login/registration demo. The important structure is:

- `src/app.py`: Flask routes and request handling. This is the entry point for the web app and the place where login/register flows are wired together.
- `src/services/user_service.py`: business logic for credential validation and user creation. Route handlers should delegate validation to this layer rather than embedding logic in the view code.
- `src/repositories/user_repository.py`: in-memory repository used for user storage. There is no database or ORM in this project; the repository keeps a Python list of `User` instances in memory.
- `src/entities/user.py`: the domain model (`User`) used by the service and repository.
- `src/tests/`: Robot Framework end-to-end browser tests. `resource.robot` contains shared setup/keywords, and the test files cover login and registration flows.

The app starts from `src/index.py`, which runs the Flask app on port `5001`.

## Commands
The project is configured for Python 3.14 and uses `uv` with a dev dependency group (`pyproject.toml`). The browser tests depend on `robotframework-browser`, which uses Playwright under the hood.

### Install dependencies
- `uv sync --group dev`

### Run the app
- `uv run python src/index.py`

The app serves the UI at `http://localhost:5001` and exposes the reset endpoint used by the tests at `POST /tests/reset`.

### Run the test suite
- Full suite: `uv run python -m robot src/tests`
- Single file: `uv run python -m robot src/tests/login.robot`
- Single file: `uv run python -m robot src/tests/register.robot`
- Single test case from a file: `uv run python -m robot -t "Login With Correct Credentials" src/tests/login.robot`

There is no dedicated lint or formatting command in this repository. If a lint tool is introduced later, prefer to add it to the project configuration rather than relying on ad hoc commands.

## Key conventions and patterns
- Keep business rules in `UserService`; routes should call the service and surface exceptions as flash messages to the UI.
- The repository is intentionally stateful in memory. Tests reset state through the `/tests/reset` route and then create a user via `AppLibrary` before proceeding.
- Validation failures are user-facing strings, not custom error codes. The exact wording from `UserService` is asserted in Robot tests, so changing a message requires updating the relevant tests.
- Username/password validation is centralized in `UserService.validate`, and “too short” checks are enforced there.
- Browser tests rely on `resource.robot` and `AppLibrary.py`; avoid duplicating setup logic in new tests.
- Prefer matching the current project style: simple Flask routes, plain Python objects, and Robot Framework keywords for browser automation.

## Practical guidance for Copilot
- When changing authentication or registration flows, review both the route handlers in `src/app.py` and the service/repository logic together; the app is small but the behavior spans multiple layers.
- When updating a user-facing error message, check both the service and the Robot tests that assert on it.
- Avoid introducing database persistence or framework abstractions unless the task explicitly requires them; this project is built around an in-memory repository and lightweight Flask views.
