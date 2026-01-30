# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Upcoming features and fixes

## [0.0.1] - Milestone 1 - 2026-01-10

### Added

- Function specifications and documentation for `correlation_report()` [#15](https://github.com/UBC-MDS/data_fixr/pull/15)
- Function specifications and documentation for `detect_anomalies()` [#16](https://github.com/UBC-MDS/data_fixr/pull/16)
- Function specifications and documentation for `remove_duplicates()` [#21](https://github.com/UBC-MDS/data_fixr/pull/21)
- Function specifications and documentation for `missing_values()` [#22](https://github.com/UBC-MDS/data_fixr/pull/22)
- Support for handling missing values in categorical columns [#17](https://github.com/UBC-MDS/data_fixr/issues/17)

### Changed

- Updated README.md with project details and usage information [#24](https://github.com/UBC-MDS/data_fixr/pull/24)
- Updated CONTRIBUTING.md with contribution guidelines [#18](https://github.com/UBC-MDS/data_fixr/pull/18)
- Updated CODE_OF_CONDUCT.md with code of conduct [#23](https://github.com/UBC-MDS/data_fixr/pull/23)

## [1.0.0] - Milestone 2 - 2026-01-17

### Added

- Implementation of `correlation_report()` for computing pairwise correlations [#44](https://github.com/UBC-MDS/data_fixr/pull/44)
- Implementation of `detect_anomalies()` for identifying outliers in data [#42](https://github.com/UBC-MDS/data_fixr/pull/42)
- Implementation of `remove_duplicates()` for duplicate row detection and removal [#45](https://github.com/UBC-MDS/data_fixr/pull/45)
- Implementation of `missing_values()` for handling missing data [#49](https://github.com/UBC-MDS/data_fixr/pull/49)
- Unit tests for `correlation_report()` [#44](https://github.com/UBC-MDS/data_fixr/pull/44)
- Unit tests for `detect_anomalies()` [#42](https://github.com/UBC-MDS/data_fixr/pull/42)
- Unit tests for `remove_duplicates()` [#45](https://github.com/UBC-MDS/data_fixr/pull/45)
- Unit tests for `missing_values()` [#49](https://github.com/UBC-MDS/data_fixr/pull/49)
- Dependencies added to `pyproject.toml` [#42](https://github.com/UBC-MDS/data_fixr/pull/42)
- Environment configuration file `environment.yml` [#52](https://github.com/UBC-MDS/data_fixr/pull/52)

### Fixed

- Updated README.md installation instructions for clarity [#52](https://github.com/UBC-MDS/data_fixr/pull/52)

### Changed

- Updated CHANGELOG.md to reflect Milestone 1 and 2 progress [#39](https://github.com/UBC-MDS/data_fixr/pull/39)
- Updated `__init__.py` with correct package imports [#53](https://github.com/UBC-MDS/data_fixr/pull/53)

## [2.0.0] - Milestone 3 - 2026-01-24

### Added

- Implemented continuous integration for the project's workflow. This runs the test suite and conducts style checkers on pushed and pull requests to the main branch [#64](https://github.com/UBC-MDS/data_fixr/pull/64)
- Implemented continuous deployment for the project's workflow. This runs the test suite, style checkers, deploys our package to Test PyPI [#68](https://github.com/UBC-MDS/data_fixr/pull/68)
- Implemented continuous deployment to build and deploy function documentation via quartodoc [#65](https://github.com/UBC-MDS/data_fixr/pull/65)
- Added 4 new unit tests for `correlation_report()` function [#66](https://github.com/UBC-MDS/data_fixr/pull/66)
- Set up function documentation using quartodoc [#65](https://github.com/UBC-MDS/data_fixr/pull/65)

### Changed 

- Updated readme with new installation instructions [#70](https://github.com/UBC-MDS/data_fixr/pull/70)
- Updated Changelog to reflect Milestone 3 updates [#73](https://github.com/UBC-MDS/data_fixr/pull/73)
