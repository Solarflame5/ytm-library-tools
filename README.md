# ytmtool
Command line tool based on [sigma67/ytmusicapi](https://github.com/sigma67/ytmusicapi) with various features for managing your YouTube Music library, mainly exporting playlists to JSON and getting statistics from them. 

# Installation and usage
- Clone the repository
- Run `pip install .` (you might want to use a venv)
- Authenticate
  - OAuth2 is currently broken with ytmusicapi, use browser cookies as follows:
  - create a `.env` file in your working directory(should be the repository root) with the following contents:
    ```
    AUTH_TYPE=browser
    ```
  - [Follow the instructions in the ytmusicapi documentation](https://ytmusicapi.readthedocs.io/en/stable/setup/browser.html)
  - Getting the cookies from a private browser window results in a longer lasting session cookie
- Use the tool with the `ytmtool` command

If you encounter any dependency issues, try using the requirements.txt file or `uv sync` to install them.
