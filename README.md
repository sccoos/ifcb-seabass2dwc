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
* The metadata template workbook is optional, but required for `eml.xml`, including at least one `creator`, `provider`, and `contact` role in `personnel`.
* Add `--include-taxonomic-coverage` to enable WoRMS taxonomy enrichment and include `taxonomicCoverage` in `eml.xml`.

### Metadata template usage
* The metadata template workbook is required to generate a proper `eml.xml` metadata file.
* `eml.xml` is an expected part of the Darwin Core package produced by this tool.
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
| `middleInitial` | optional middle initial appended to `givenName` |
| `surName` | person's surname |
| `organizationName` | organization written to EML |
| `electronicMailAddress` | email written to EML |
| `positionName` | position or title written to EML when present |
| `role` | determines how the person is mapped into EML |

* Required `personnel` roles:

| Role | Requirement |
| --- | --- |
| `creator` | at least one row required |
| `provider` | at least one row required |
| `contact` | at least one row required |

* `personnel.role` mapping:

| Role value | EML output |
| --- | --- |
| `creator` | `creator` |
| `provider` | `metadataProvider` |
| `contact` | `contact` |
| any other value | `associatedParty` |

* For `associatedParty`, the original `role` value is also written to the EML `<role>` element.
