# Changelog

The format is based on [Keep a Changelog]
(https://keepachangelog.com/en/1.0.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.1.0] - 2021-08-10
### Changed
- Removed service prefix. Now nginx will serve html starting with root

### Added
- Add support for TLS. Documentation can be served from ports 80 and 443


## [1.0.1] - 2021-08-08
### Changed

- Change docker/Dockerfile so that nginx will serve html via "/docs/" prefix
  insead of "/"
