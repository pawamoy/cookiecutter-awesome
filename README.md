# cookiecutter-shellm
Cookiecutter to create an [awesome](https://github.com/sindresorhus/awesome) list.

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Documentation](#documentation)
- [Development](#development)
- [History](#history)
- [Credits](#credits)
- [License](#license)

## Features
- Creative Commons CC0 1.0 Universal License (as recommended in
  [awesome's manifesto](https://github.com/sindresorhus/awesome/blob/master/awesome.md)).
- Travis configuration with [awesome_bot][awesome_bot] check.
- Changelog, code of conduct, contributing, and pull request template files.
- Readme optionally updated with [DocToc][doctoc].

## Requirements
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- [cookiecutter](https://github.com/audreyr/cookiecutter)
- ([awesome_bot][awesome_bot])
- ([DocToc][doctoc])

## Usage
```bash
cookiecutter gh:Pawamoy/cookiecutter-awesome
# OR
cookiecutter https://github.com/Pawamoy/cookiecutter-awesome
```

- Run `doctoc README.md` to update the table of contents.
- Run `awesome_bot README.md` to verify the links.

## Example
See the [awesome-repository](https://github.com/Pawamoy/awesome-repository) list.

## Development
See [CONTRIBUTING](CONTRIBUTING.md).

## History
See [CHANGELOG](CHANGELOG.md).

## Credits
This cookiecutter was created using contents from
[cookie-cookie](https://github.com/tuxredux/cookie-cookie) and the
[awesome-repository](https://github.com/Pawamoy/awesome-repository) list,
which itself was generated with this
[Yeoman generator](https://github.com/dar5hak/generator-awesome-list).

Also see [AUTHORS](AUTHORS.md).

## License
See [LICENSE](LICENSE).

[awesome_bot]: https://github.com/dkhamsing/awesome_bot
[doctoc]: https://github.com/thlorenz/doctoc
