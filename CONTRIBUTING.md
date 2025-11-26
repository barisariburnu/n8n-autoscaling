# Contributing to n8n-autoscaling

First off, thank you for considering contributing to n8n-autoscaling! It's people like you that make n8n-autoscaling such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible.
* **Provide specific examples to demonstrate the steps**.
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include logs and error messages** from Docker containers.
* **Include your environment details**:
  - Docker version
  - Docker Compose version
  - Operating system
  - n8n version
  - Configuration (redact sensitive information)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps** or provide examples of how the enhancement would be used.
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Explain why this enhancement would be useful** to most n8n-autoscaling users.

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Follow the Python style guide (PEP 8)
* Include thoughtful comments in your code
* End all files with a newline
* Update the README.md with details of changes if applicable
* Update the CHANGELOG.md following the Keep a Changelog format
* Make sure your code passes all tests (if tests are implemented)

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/n8n-autoscaling.git
   cd n8n-autoscaling
   ```

3. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Make your changes and test them:
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env with your configuration
   # Important: Set strong passwords and encryption keys
   
   # Create the external network
   docker network create shark
   
   # Start the services
   docker compose up -d
   
   # Check logs
   docker compose logs -f
   ```

5. Commit your changes:
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```
   
   Use conventional commits:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for updates to existing features
   - `Remove:` for removed features
   - `Docs:` for documentation changes

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request from your fork to the main repository

## Code Style Guidelines

### Python

* Follow PEP 8 style guide
* Use meaningful variable and function names
* Add docstrings to functions and classes
* Keep functions focused and small
* Use type hints where appropriate
* Handle exceptions appropriately with proper logging

### Docker

* Keep Dockerfile instructions organized and commented
* Use multi-stage builds when appropriate
* Minimize layer count
* Use .dockerignore to exclude unnecessary files
* Pin versions for production dependencies

### Environment Variables

* Document all environment variables in .env.example
* Provide sensible defaults where possible
* Use clear, descriptive variable names
* Group related variables together

## Testing

* Test your changes locally using Docker Compose
* Verify autoscaling behavior:
  - Scale up when queue length increases
  - Scale down when queue length decreases
  - Respect cooldown periods
  - Stay within min/max replica bounds
* Check all services are healthy
* Monitor logs for errors

## Documentation

* Update README.md if you change functionality
* Update .env.example if you add new environment variables
* Add comments to complex code sections
* Update CHANGELOG.md with your changes

## Community

* Be respectful and constructive
* Help others when you can
* Share your experience and use cases
* Report issues you encounter

## Questions?

Feel free to open an issue with your question, or reach out to the maintainers.

Thank you for contributing! 🎉
