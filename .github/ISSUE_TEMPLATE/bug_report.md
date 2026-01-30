---
name: Bug Report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

## Bug Description
A clear and concise description of what the bug is.

## Steps To Reproduce
Steps to reproduce the behavior:
1. Configure '...'
2. Run command '...'
3. Check logs '...'
4. See error

## Expected Behavior
A clear and concise description of what you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., Ubuntu 22.04, Windows 11, macOS 14]
- Docker Version: [e.g., 24.0.5]
- Docker Compose Version: [e.g., 2.20.2]
- n8n Version: [e.g., 1.108.2]
- Project Version/Commit: [e.g., v2.0.0 or commit hash]

## Configuration
Please provide relevant parts of your configuration (remove sensitive data):

```yaml
# docker-compose.yml snippets if relevant
```

```bash
# .env snippets (redact sensitive information)
MIN_REPLICAS=1
MAX_REPLICAS=5
# etc.
```

## Logs
Please provide relevant logs:

```
# Autoscaler logs
docker compose logs n8n-autoscaler

# Worker logs
docker compose logs n8n-worker

# Other relevant logs
```

## Additional Context
Add any other context about the problem here (screenshots, error messages, etc.).

## Possible Solution
If you have an idea of what might be causing this or how to fix it, please share.
