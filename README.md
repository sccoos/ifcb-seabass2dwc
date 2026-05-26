# IFCB SeaBASS2DwC file conversion tool
* Converts SeaBASS-formatted IFCB `.sb` files into Darwin Core Archive submission files.
* A metadata template workbook, `METADATA-TEMPLATE_ifcb-seabass2dwc.xlsx`, is included with this repository for optional `eml.xml` generation.

# Project incentive
* The tool is created in the interest of extending FAIR access of IFCB data collected and formatted for SeaBASS, PACE's validation data repository. The maintainers, SCCOOS/CalCOFI, are a particpant of the Pace Validation Science Teams. Our data is collected underway on quarterly cruises along the California coast.
* You can preview that data on our IFCB dashboard located here: https://ifcb.caloos.org/timeline?dataset=calcofi-cruises-underway
<img width="3456" height="2316" alt="Screenshot 2026-05-26 at 11-06-07 CalCOFI Cruises (underway)" src="https://github.com/user-attachments/assets/3ddd0f30-97b8-4e04-8664-5a5b269992ce" />


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
* Add `--include-taxonomic-coverage` to include `taxonomicCoverage` in `eml.xml`.
