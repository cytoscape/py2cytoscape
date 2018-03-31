## ***cyclient.session.new***

**`cyclient.session.new(self, verbose=False)`**

Destroys the current session and creates a new, empty one.

* **`wid`** Window ID
* **`verbose`** print more

___

## ***cyclient.session.save***

**`cyclient.session.save(self, session_file, verbose=False)`**

Saves the current session to an existing file, which will be replaced.
If this is a new session that has not been saved yet, use 'save as'
instead.

* **`session_file`** The path to the file where the current session
must be saved to.
* **`verbose`** print more

___

## ***cyclient.session.open***

**`cyclient.session.open(self, session_file=None,session_url=None, verbose=False)`**

Opens a session from a local file or URL.

* **`session_file`** The path to the session file (.cys) to be loaded.
* **`session_url`** A URL that provides a session file.
* **`verbose`** print more

___

## ***cyclient.session.save_as***

**`cyclient.session.save_as(self, session_file, verbose=False)`**

Saves the current session as a new file.

* **`session_file`** The path to the file where the current session
must be saved to.
* **`verbose`** print more

___

