# 🎵 Poetry Command Cheat Sheet

## 🔹 1. Project Setup
```bash
poetry new my_project
```
Creates a **new project structure** with `pyproject.toml`, tests, etc.

```bash
poetry init
```
Initializes a new Poetry project in an **existing folder**.

---

## 🔹 2. Dependency Management
```bash
poetry add requests
```
Adds `requests` as a dependency and updates `poetry.lock`.

```bash
poetry add requests@^2.30.0
```
Adds with version constraints.

```bash
poetry add --dev pytest
```
Adds a **development dependency** (e.g., test tools).

```bash
poetry remove requests
```
Removes a dependency cleanly.

```bash
poetry update
```
Updates all dependencies to their latest allowed versions.

```bash
poetry update requests
```
Updates only `requests`.

---

## 🔹 3. Virtual Environment Management
```bash
poetry install
```
Installs dependencies listed in `pyproject.toml`.

```bash
poetry env list
```
Shows all virtual environments Poetry created for the project.

```bash
poetry env use python3.11
```
Switches to a specific Python version for your venv.

```bash
poetry shell
```
Activates the virtual environment.

```bash
poetry run python main.py
```
Runs commands **inside the venv** without activating it manually.

---

## 🔹 4. Running & Testing
```bash
poetry run pytest
```
Runs tests with dependencies in venv.

```bash
poetry run jupyter notebook
```
Runs external tools inside the venv.

---

## 🔹 5. Lockfile Management
```bash
poetry lock
```
Regenerates `poetry.lock`.

---

## 🔹 6. Packaging & Publishing
```bash
poetry build
```
Builds **source distribution** (`.tar.gz`) and **wheel** (`.whl`).

```bash
poetry publish --username __token__ --password <pypi-token>
```
Publishes package to PyPI (or private registry).

```bash
poetry config pypi-token.pypi <token>
```
Stores PyPI token so you don’t have to pass it every time.

---

## 🔹 7. Config & Info
```bash
poetry show
```
Shows installed packages and versions.

```bash
poetry show requests
```
Shows detailed info about a package.

```bash
poetry config --list
```
Shows Poetry configuration (e.g., venv location).

```bash
poetry config virtualenvs.in-project true
```
Forces venvs to be created **inside the project** as `.venv/`.

---

## 🔹 8. Miscellaneous
```bash
poetry check
```
Validates your `pyproject.toml` and lock file.

```bash
poetry export -f requirements.txt --output requirements.txt
```
Exports dependencies for tools that only support `requirements.txt`.

---

# 🚀 Workflow Example
```bash
poetry new my_project
cd my_project
poetry add requests
poetry add --dev pytest
poetry install
poetry run pytest
poetry build
poetry publish
```
