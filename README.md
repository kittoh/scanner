# SCANNER

__SCANNER__ (Tentative name 😅)

This is a basic multi-part security scanning pipeline.

_The FLOW_

The pipeline starts from running an OWASP Zap Scan to any target. ZAP Scan is ran from a Docker Image.
Then the output file (.json file) is parsed using a Python script. The parsed output will then be
attached to an issue created in JIRA, also via a Python script.

_The SEQUENCE_

1. ZAP Scan - Baseline
2. JSON Parser
3. Jira Issue Creator




