# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Prepared project for open-source release
- Updated LICENSE copyright holder
- Improved .gitignore with comprehensive patterns
- Enhanced documentation structure

### Added
- CONTRIBUTING.md with detailed contribution guidelines
- CHANGELOG.md for tracking project changes

## [2.0.0] - 2025-01-XX

### Added
- Cloudflare Tunnel integration for secure external access
- Traefik reverse proxy for n8n UI and webhooks
- Support for BullMQ v4+ queue patterns
- Graceful shutdown support for workers
- Task broker and runner authentication
- Puppeteer and Chrome integration for web scraping
- Tailscale IP binding support for PostgreSQL
- Comprehensive health checks for all services
- Redis queue monitoring service
- External network support (`shark` network)

### Changed
- Updated to n8n version 1.108.2
- Updated to Node.js version 22.19
- Updated to PostgreSQL 17
- Updated to Redis 7 Alpine
- Improved autoscaler logic with better error handling
- Enhanced cooldown period management
- Better Redis connection handling with retry logic
- Improved Docker Compose configuration structure

### Fixed
- Queue length detection across different BullMQ versions
- Worker scaling with proper cooldown periods
- Container replica counting accuracy
- Redis connection error handling

## [1.0.0] - 2024-XX-XX

### Added
- Initial release of n8n-autoscaling
- Dynamic worker scaling based on Redis queue length
- Docker Compose based deployment
- PostgreSQL database integration
- Redis queue integration
- Configurable scaling thresholds and limits
- Autoscaler Python script
- Redis queue monitoring script
- Basic documentation

### Features
- Minimum and maximum replica configuration
- Queue threshold based scaling decisions
- Polling interval configuration
- Cooldown period between scaling actions
- Docker socket integration for container management
- Environment-based configuration

---

## Version History

### Understanding Version Numbers

This project uses Semantic Versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Incompatible API changes or major feature overhauls
- **MINOR**: New features added in a backwards-compatible manner
- **PATCH**: Backwards-compatible bug fixes

### Release Types

- **[Unreleased]**: Changes that are committed but not yet released
- **[X.Y.Z]**: Released versions with date

### Change Categories

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes

---

[Unreleased]: https://github.com/barisariburnu/n8n-autoscaling/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/barisariburnu/n8n-autoscaling/releases/tag/v2.0.0
[1.0.0]: https://github.com/barisariburnu/n8n-autoscaling/releases/tag/v1.0.0
