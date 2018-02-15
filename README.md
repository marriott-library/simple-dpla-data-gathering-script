# DPLA Data Gathering Script

A simple Python script that uses a SQLite database of Menu Link IDs (MLID) and names to retrieve information from the Digital Public Library of America (DPLA) using the DPLA API. The script exports found data into a CSV.

An example SQLite database and CSV output file are given.

## Getting Started

The script uses a [SQLite3](https://www.sqlite.org/download.html) database (dpla.sqlite3) for incoming data. It uses one table (`dpla`) with two columns (`mlid`, and `name`). A free GUI-based SQLite3 editor is available at <http://sqlitebrowser.org>.

The script also requires a [DPLA](https://dp.la) API key. This can be used by either modifying the line in the script that begins with `dp_api_key = ` or by adding the key to an environmental variable named `DP_API_KEY`.

### Prerequisites

* [Python](https://www.python.org) >= version 2.0
* [SQLite3](https://www.sqlite.org/)
* [SQLite3 Python Library](https://docs.python.org/2/library/sqlite3.html).

## Authors

* **[Jacob Reed](jacob.reed@utah.edu)** - design and development
* **[Anna Neatrour](anna.neatrour@utah.edu)** - planning and testing

## License

This project is licensed  under the Apache 2.0 license - see the [LICENSE.md](LICENSE.md) file for details
