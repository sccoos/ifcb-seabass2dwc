# IFCB2DwC file conversion tool
* Converts SeaBASS-formatted IFCB `.sb` files into Darwin Core Archive submission files.
* A metadata template workbook, `METADATA-TEMPLATE_ifcb-seabass2dwc.xlsx`, is included with this repository for optional `eml.xml` generation.

### Before running script
* Review the input `.sb` file or file set before conversion.
* Fill out the metadata template workbook before running the script if you want `eml.xml`.

### Installation:
* install directly from a local source checkout
* `pip install .`
* requires-python = ">=3.9"
* refer to `pyproject.toml` for package requirements
* after installation the tool can be run from the terminal with `ifcb-seabass2dwc`

### Example run:
`ifcb-seabass2dwc /path/to/seabass-files --output-dir generated-files --metadata-template scripts/METADATA-TEMPLATE_ifcb-seabass2dwc.xlsx`
* The metadata template workbook is optional, but required for `eml.xml`.
* Add `--disable-taxonomy-lookup` to skip WoRMS lookups.
