# PowerFactory - Useful Scripts and Tools

Welcome to the PowerFactory Scripts and Tools repository! These scripts were created for my thesis and are used to mainly receive geoinformation from OpenStreetMap and integrate them into different PowerFactory elements. The code may contain AI generated parts.

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
python osm_to_kml.py
```

## Scripts

- **[kml_to_powerfactory.py](kml_to_powerfactory.py)** : Compares the elements (*ElmLne,*ElmSite...) with the Paths and Points in the kml file and updates all the coordinates based on a identifier defined through input parameters in PowerFactory.

- **[osm_to_kml.py](osm_to_kml.py)** : Exports all the power grid elements from OpenStreetMap of a country to a .kml file. Make sure to define the right tags and change the country based on your needs.

## Contributing

Contributions are welcome! If you have any ideas for new scripts or improvements to existing ones, please open an issue or submit a pull request.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Social Networks
<p>
  <a href="https://www.linkedin.com/in/aqoraj" rel="nofollow noreferrer">
    <img src="https://i.sstatic.net/gVE0j.png" alt="linkedin"> LinkedIn
  </a> &nbsp; 
  <a href="https://github.com/aqoraj" rel="nofollow noreferrer">
    <img src="https://i.sstatic.net/tskMh.png" alt="github"> Github
  </a>
</p>
