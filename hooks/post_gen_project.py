print("""
You have succesfully created `{{ cookiecutter.repository_slug }}`
with these cookiecutter parameters:

{% for key, value in cookiecutter.items()|sort %}
  {{ "{0:24}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

-----------------------------------------------------------------

Now:

- Run `awesome_bot README.md` to verify the links.
- Activate your repository in your Travis account.
- Please read awesome's PR requirements before submitting a Pull Request:
  https://github.com/sindresorhus/awesome/blob/master/pull_request_template.md
""")
