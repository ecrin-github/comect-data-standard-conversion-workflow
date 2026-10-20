# CoMeCT Data Standard Conversion Workflow Deliverable Supplementary Material
git clone with `--recurse-submodules` to get input dataset used for Carrot 
## Content
- `carrot`
  - `input`: [CDISC SDTM example dataset from CDISC](https://github.com/cdisc-org/sdtm-adam-pilot-project) (as a submodule)
  - `preprocess_dm.py`: sample Python script for CDISC SDTM preprocessing
  - `rules.json`: sample transformation rules file output from Carrot Mapper
- `FHIR2ODM`
  - `questionnaire-example-bluebook-R4.json`: sample FHIR questionnaire resource, [from HL7's website](https://hl7.org/fhir/R4/questionnaire-example-bluebook.json.html)
  - `questionnaire-example-bluebook-CDISC-ODM.xml`: output XML from FHIR2ODM using the aforementioned FHIR questionnaire file
