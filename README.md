# PowerFactory - Useful Scripts and Tools

Welcome to the PowerFactory Scripts and Tools repository! These scripts were created for the master's thesis and are used to mainly receive gis information from OpenStreetMap and to integrate them into PowerFactory.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Scripts](#scripts)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use these scripts, clone the repository to your local machine:

```bash
git clone https://github.com/aqoraj/PowerFactory.git
```

Ensure you have DIgSILENT PowerFactory installed and properly configured on your system.

## Usage

Each script is designed to perform a specific task within PowerFactory. Refer to the individual script documentation for detailed usage instructions.

Example:

```bash
python kml_to_powerfactory.py
```

## Scripts

- **[kml_to_powerfactory.py](kml_to_powerfactory.py)** : Compares the elements (*ElmLne,*ElmSite...) with the Paths and Points in the kml file and updates all the coordinates based on a identifier defined through input parameters in PowerFactory.


## Contributing

Contributions are welcome! If you have any ideas for new scripts or improvements to existing ones, please open an issue or submit a pull request.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.
