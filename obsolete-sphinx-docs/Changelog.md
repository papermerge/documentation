# Changelog

The format is based on [Keep a Changelog]
(https://keepachangelog.com/en/1.0.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2022-04-03

### Changes

  - Content updates


## [1.2.0] - 2021-09-12

### Added

- Versioned documentation (sphinx-multiversion)
- GitHub CI
- Add roadmap for 2.1.x

## [1.1.1] - 2021-08-11
### Changed
- Serve docs only on port 80

## [1.1.0] - 2021-08-10
### Changed
- Removed service prefix. Now nginx will serve html starting with root

### Added
- Add support for TLS. Documentation can be served from ports 80 and 443


## [1.0.1] - 2021-08-08
### Changed

- Change docker/Dockerfile so that nginx will serve html via "/docs/" prefix
  insead of "/"
