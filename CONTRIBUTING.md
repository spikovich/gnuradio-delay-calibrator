# Contributing to GNU Radio Delay Calibrator

Thank you for your interest in contributing to the GNU Radio Delay Calibrator project! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing to the project. We expect all contributors to adhere to these guidelines to foster an open and welcoming community.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/gnuradio-delay-calibrator.git
   cd gnuradio-delay-calibrator
   ```
3. Install the development dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### Making Changes

1. Make your changes to the codebase
2. Add or update tests as necessary
3. Update documentation as needed
4. Ensure all tests pass

### Testing

Please ensure all your code changes pass the existing tests. If you're adding new functionality, include appropriate tests.

To run tests:
```bash
# Command to run tests (to be implemented)
```

### Documentation

Documentation is crucial for the project. If you're adding new features or modifying existing ones, please update the relevant documentation:
- Update README.md if necessary
- Update inline code comments
- Add examples if appropriate

## Pull Request Process

1. Update your fork to the latest version of the main repository
2. Commit your changes following the [commit message guidelines](#commit-messages)
3. Push your changes to your fork on GitHub
4. Submit a pull request to the main repository
5. Address any feedback from code reviewers and make necessary changes
6. Once approved, your pull request will be merged

## Commit Messages

Please follow these guidelines for commit messages:
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add automatic delay compensation feature

- Implements feedback control algorithm
- Adds user interface controls
- Updates documentation
- Closes #123
```

## Style Guide

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Comment complex sections of code
- Keep functions focused on a single task

## Reporting Bugs

If you find a bug, please report it by creating an issue on GitHub. Please include:
- A clear, descriptive title
- A detailed description of the issue
- Steps to reproduce the bug
- Expected and actual results
- GNU Radio and Python versions
- Any relevant screenshots or error messages

## Feature Requests

Feature requests are welcome! Please submit them as GitHub issues and include:
- A clear, descriptive title
- A detailed description of the proposed feature
- Any relevant context or examples
- Explanation of why this feature would be useful to other users

## Questions or Need Help?

If you have questions or need help with the project, you can:
- Open an issue on GitHub
- Reach out to project maintainers (provide contact information)

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

Thank you for contributing to GNU Radio Delay Calibrator!