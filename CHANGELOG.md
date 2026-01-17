# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Upcoming features and fixes

## [0.0.1] - Milestone 1 - 2026-01-10

### Added

- Function specifications and documentation for `correlation_report()` (#15)
- Function specifications and documentation for `detect_anomalies()` (#16)
- Function specifications and documentation for `remove_duplicates()` (#21)
- Function specifications and documentation for `missing_values()` (#22)
- Support for handling missing values in categorical columns (#17)

### Changed

- Updated README.md with project details and usage information (#24)
- Updated CONTRIBUTING.md with contribution guidelines (#18)
- Updated CODE_OF_CONDUCT.md with code of conduct (#23)

## [0.1.0] - Milestone 2 - 2026-01-17

### Added

- Implementation of `correlation_report()` for computing pairwise correlations (#44)
- Implementation of `detect_anomalies()` for identifying outliers in data (#42)
- Implementation of `remove_duplicates()` for duplicate row detection and removal (#45)
- Implementation of `missing_values()` for handling missing data (#49)
- Unit tests for `correlation_report()` (#44)
- Unit tests for `detect_anomalies()` (#42)
- Unit tests for `remove_duplicates()` (#45)
- Unit tests for `missing_values()` (#49)
- Dependencies added to `pyproject.toml` (#42)
- Environment configuration file `environment.yml` (#52)

### Fixed

- Updated README.md installation instructions for clarity (#51, #52, #53)

### Changed

- Updated CHANGELOG.md to reflect Milestone 1 and 2 progress (#39)
- Updated `__init__.py` with correct package imports (#53)