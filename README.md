## font-size

[![Python CI](https://github.com/source-foundry/font-size/actions/workflows/py-ci.yml/badge.svg)](https://github.com/source-foundry/font-size/actions/workflows/py-ci.yml)
[![Python Lints](https://github.com/source-foundry/font-size/actions/workflows/py-lint.yml/badge.svg)](https://github.com/source-foundry/font-size/actions/workflows/py-lint.yml)

## About

font-size is a Python 3.6+ command line executable tool that reports *.otf, *.ttf, *.woff, and *.woff2 file and individual OpenType table sizes in a clean tabular format.

<img width="625" alt="Image of a font-size report in the terminal" src="https://user-images.githubusercontent.com/4249591/118226931-ae095880-b455-11eb-9fb9-f1d5a5fb928b.png">

## Installation

`font-size` requires a Python 3.6+ interpreter.

Installation in a [Python3 virtual environment](https://docs.python.org/3/library/venv.html) is recommended as dependencies are pinned to versions that are confirmed to work with this project.

Use any of the following installation approaches:

### pip install from PyPI

```
$ pip3 install font-size
```

### pip install from source

```
$ git clone https://github.com/source-foundry/font-size.git
$ cd font-size
$ pip3 install .
```

### Developer install from source

The following approach installs the project and associated optional developer dependencies so that source changes are available without the need for re-installation.

```
$ git clone https://github.com/source-foundry/font-size.git
$ cd font-size
$ pip3 install --ignore-installed -r requirements.txt -e ".[dev]"
```

## Usage

```
$ font-size [FONT PATH 1] [FONT PATH 2] ... [FONT PATH ...]
```

## Issues

Please report issues on the [project issue tracker](https://github.com/source-foundry/font-size/issues).

## Contributing

Contributions are welcome. A development dependency environment can be installed in editable mode with the developer installation documentation above.

Please use the standard Github pull request approach to propose source changes.

### Source file linting

Python source files are linted with `flake8`. See the Makefile `test-lint` target for details.


### Testing

The project runs continuous integration testing on GitHub Actions runners with the `pytest` testing toolchain. Test modules are located in the `tests` directory of the repository.

Local testing by Python interpreter version can be performed with the following command executed from the root of the repository:

```
$ tox -e [PYTHON INTERPRETER VERSION]
```

Please see the `tox` documentation for additional details.

### Test coverage

Unit test coverage is executed with the `coverage` tool. See the Makefile `test-coverage` target for details.

## Acknowledgments

`font-size` is built with the fantastic [fontTools free software library](https://github.com/fonttools/fonttools).

## License

Copyright 2021 Source Foundry Authors and Contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.