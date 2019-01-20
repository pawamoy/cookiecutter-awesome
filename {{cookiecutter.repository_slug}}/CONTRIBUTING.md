# Contributing

Contributions are welcome, and they are greatly appreciated!

Every little bit helps, and credit will always be given.
So feel free to create a [new merge/pull request][merge-link]!

And make sure to follow the [guidelines](#merge-pull-request-guidelines).

## Merge/Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:
1. Make sure to have atomic commits and contextual commit messages!
  [Check out this awesome blog post by Chris Beams for more information.][chris-beams]
2. Test the links :
```bash
  gem install awesome_bot
  awesome_bot README.md
  ```
3. Keep the contents sorted alphabetically
4. Update the table of contents if necesseray

Thank you for your suggestions!

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.

[issue-link]: {% if cookiecutter.remote_provider == "none" %}mailto:{{cookiecutter.author_email}}{% else %}https://{{cookiecutter.remote_provider}}/{{cookiecutter.remote_namespace}}/{{cookiecutter.repository_slug}}/issues/new{% endif %}
[merge-link]: {% if cookiecutter.remote_provider == "none" %}mailto:{{cookiecutter.author_email}}{% else %}https://{{cookiecutter.remote_provider}}/{{cookiecutter.remote_namespace}}/{{cookiecutter.repository_slug}}/{% if cookiecutter.remote_provider == "github.com" %}compare{% elif cookiecutter.remote_provider == "gitlab.com" %}merge_requests/new{% elif cookiecutter.remote_provider == "bitbucket.org" %}pull-requests/new{% endif %}{% endif %}
[chris-beams]: http://chris.beams.io/posts/git-commit/
