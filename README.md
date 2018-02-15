# DPLA Data Gathering Script

A simple Python script that connects to a SQLite database of Menu Link IDs (MLID) and names. Using the DPLA api, it processes each line of the database and exports found data into a CSV.

An example SQLite database and CSV output file are given.

## Getting Started

In order to work properly the script requires a [SQLite3](https://www.sqlite.org/download.html) database (dpla.sqlite3) available. The script uses one table (`dpla`) with two columns (`mlid`, and `name`). A good, free GUI based SQLite3 editor is available at [http://sqlitebrowser.org](http://sqlitebrowser.org).

The script also uses a [DPLA](https://dp.la) API key. This can be used either by modifying the line in the script that begins with `dp_api_key = ` or by adding your key to an environmental variable named `DP_API_KEY`.

### Prerequisites

* [Python](https://www.python.org) >= version 2.0
* [SQLite3](https://www.sqlite.org/)
* [sqlite3 python library](https://docs.python.org/2/library/sqlite3.html).

## Authors

* **Jacob Reed** - design and development
* **Anna Neatrour** - planning and testing

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

