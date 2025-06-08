# AIAgent

AIAgent is an experimental framework for building and evaluating AI agents that can interact with code, files, and external tools. The project is designed to facilitate research and development of autonomous agents capable of performing complex tasks in a codebase.

## Features

- **Agent Core**: The main agent logic is implemented in `main.py`, with supporting modules for configuration, prompting, and function calling.
- **Function Library**: The `functions/` directory contains utility functions for file operations, code execution, and more.
- **Sample Calculator**: The `calculator/` folder provides a sample calculator package, including tests and supporting files. This can be used to evaluate the agent's ability to understand, modify, and test code.
- **Testing**: Example tests are provided in `tests.py` and within the `calculator/` directory.

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the agent**:
   ```bash
   python main.py
   ```
3. **Evaluate with the Calculator**:
   The `calculator/` directory contains a simple calculator implementation and tests. You can use this as a sandbox for the agent to demonstrate its capabilities.

## Project Structure

- `main.py` - Entry point for the agent.
- `config.py`, `prompt.py`, `call_function.py` - Core modules for agent configuration and operation.
- `functions/` - Utility functions for file and code operations.
- `calculator/` - Sample calculator package with code and tests.
- `tests.py` - Additional tests for the agent framework.

## License

This project is licensed under the MIT License. See `LICENSE` for details.