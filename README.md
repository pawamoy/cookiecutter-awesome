# cookiecutter-awesome
Cookiecutter to create an [awesome][awesome] list.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [Development](#development)
  - [History](#history)
  - [Community](#community)
- [Credits](#credits)
- [License](#license)

## Features

- Creative Commons CC0 1.0 Universal License (as recommended in awesome's
  [manifesto](https://github.com/sindresorhus/awesome/blob/master/awesome.md)).
- Travis configuration with [awesome_bot][awesome_bot] check.
- Changelog, code of conduct, contributing, and pull request template files.
- Compliant with awesome's [PR requirements][pr-requirements].

## Requirements

- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- [cookiecutter](https://github.com/audreyr/cookiecutter)
- ([awesome_bot][awesome_bot])

## Usage

```bash
cookiecutter gh:moodule/cookiecutter-awesome
# OR
cookiecutter https://github.com/moodule/cookiecutter-awesome
```

Once your project has been generated:
- Run `awesome_bot README.md` to verify the links.
- Activate your repository in your Travis account.
- **Please read [the PR requirements][pr-requirements]**
  before submitting a Pull Request to [awesome][awesome].

## Example

See the [awesome-repository](https://github.com/sindresorhus/awesome) list.

## Development

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

### History

See [CHANGELOG](CHANGELOG.md).

### Community

See [CODE OF CONDUCT](CODE_OF_CONDUCT.md)

## Credits

This cookiecutter was created using contents from
[cookie-cookie](https://github.com/tuxredux/cookie-cookie) and the
[cookiecutter-awesome](https://github.com/Pawamoy/cookiecutter-awesome) template,
which itself was generated with this
[Yeoman generator](https://github.com/dar5hak/generator-awesome-list).

Also see [AUTHORS](AUTHORS.md).

## License

See [LICENSE](LICENSE).

[awesome]: https://github.com/sindresorhus/awesome
[awesome_bot]: https://github.com/dkhamsing/awesome_bot
[pr-requirements]: https://github.com/sindresorhus/awesome/blob/master/pull_request_template.md
