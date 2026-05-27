# IFCB SeaBASS2DwC file conversion tool
* Converts SeaBASS-formatted IFCB `.sb` files into Darwin Core Archive submission files.
* A metadata template workbook, `METADATA-TEMPLATE_ifcb-seabass2dwc.xlsx`, is included with this repository for optional `eml.xml` generation.
* Functionality depends on valid .sb files containing the expected fields for a SeaBASS plankton data submission, as well as the usage of taxonomic definitions derived from the World Register of Marine Species.
* Contact/author: ibrunjes@ucsd.edu

## Project incentive
* The tool is created in the interest of extending FAIR access of IFCB data collected and formatted for SeaBASS, PACE's validation data repository. The maintainers, SCCOOS/CalCOFI, are a particpant of the Pace Validation Science Teams. Our data is collected underway on quarterly cruises along the California coast, but the tool should be usable by any teams producing validated plankton & particles datasets for SeaBASS.
* You can preview that data on our IFCB dashboard located here: https://ifcb.caloos.org/timeline?dataset=calcofi-cruises-underway
<img width="3456" height="2316" alt="Screenshot 2026-05-26 at 11-06-07 CalCOFI Cruises (underway)" src="https://github.com/user-attachments/assets/3ddd0f30-97b8-4e04-8664-5a5b269992ce" />

## Installation:
* install directly from a local source checkout
* `pip install .`
* requires-python = ">=3.9"
* refer to `pyproject.toml` for package requirements
* after installation the tool can be run from the terminal with `ifcb-seabass2dwc`

### Example run:
`ifcb-seabass2dwc /path/to/seabass-files --output-dir generated-files --metadata-template scripts/METADATA-TEMPLATE_ifcb-seabass2dwc.xlsx`
* The metadata template workbook is optional (recommended), but required for `eml.xml`, see usage below.
* CLI option `--include-taxonomic-coverage` enables WoRMS taxonomy enrichment to include `taxonomicCoverage` in `eml.xml`.

## Metadata template usage
* The metadata template workbook should be provided to generate `eml.xml` metadata file, and is required in a Darwin Core submission.
* Without the metadata template, the script can still generate `event.csv`, `occurrence.csv`, and `meta.xml`, but not a complete `eml.xml`.

* The metadata template workbook must include these sheets:

| Sheet | Use |
| --- | --- |
| `general` | key/value metadata used for `eml.xml` and `occurrence.csv` |
| `personnel` | table of people used to populate EML party sections |

* Required `general` fields:

| Field | Use |
| --- | --- |
| `title` | dataset title written to `eml.xml` |
| `abstract` | abstract text written to `eml.xml` |
| `geographicDescription` | text description for EML geographic coverage |
| `identificationReferences` | citation or workflow reference written to `occurrence.csv` |
| `publisherOrganization` | publisher organization name |
| `publisherEmail` | publisher contact email |
| `publisherURL` | publisher URL |

* Expected `personnel` columns:

| Column | Use |
| --- | --- |
| `givenName` | person's given name |
| `middleInitial` | optional middle initial |
| `surName` | person's surname |
| `organizationName` | person's organizational affiliation |
| `electronicMailAddress` | person's email |
| `positionName` | person's position or title |
| `role` | an EML defined role, see usage below |

* Required `personnel` roles:

| Role | Requirement |
| --- | --- |
| `creator` | at least one creator required |
| `provider` | at least one provider required |
| `contact` | at least one contact required |

## File output and validation:
* The tool will output to the specified output directory the following files: occurrence.csv, event.csv, meta.xml, and conditionally eml.xml
* A zipped archive of these files, which is the expected package type for submission is also created
* Validation of the .zip archive package is recommended using this tool: https://www.gbif.org/tool/81281/gbif-data-validator
