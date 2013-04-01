Memonic Exporter
================


An export function for Memonic `has been promised
<http://support.memonic.com/entries/20196536-datensicherung>`_ in 2011, but
nothing has happened since then.

This small Python 2/3 script allows you to export your Memonic Sets / Groups /
Notes to JSON files using the official API.

The data is pretty raw and not preprocessed. But it should be enough so you can
write import scripts for other services.


Requirements
------------

- Python 2.6+ or 3
- python-requests (install via ``pip install -r requirements.txt``)


Usage
-----

Unfortunately the OAuth authentication is not documented, therefore I stuck to
basic auth. First, set the memonic username, password and `API key
<https://www.memonic.com/developers/api/keys>`_ environment variables::

    export MEMONIC_USER='username'
    export MEMONIC_PASS='password'
    export MEMONIC_API_KEY='api_key'

Then run the export script::

    python export.py

Alternatively, you could also run this as a one-liner::

    MEMONIC_USER='username' \
    MEMONIC_PASS='password' \
    MEMONIC_API_KEY='api_key' \
    python export.py

The data is then written into the following files in your current working
directory:

- ``memonic_sets.json``
- ``memonic_groups.json``
- ``memonic_notes.json``


License (MIT)
-------------

Copyright (C) 2013 Danilo Bargen

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
