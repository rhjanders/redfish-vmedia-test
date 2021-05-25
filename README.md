# redfish-vmedia-test
A simple tool which can validate virtual media attachment and detachment via Redfish using sushy library

Usage:

Dell R640:
python vmedia-attach.py --username [username] --password [password] --bmc_url https://[bmc_ip]/redfish/v1 --manager_url v1/Managers/iDRAC.Embedded.1 --image_url [URL, e.g. https://example.com/my.iso]

HP e910:
python vmedia-attach.py --username [username] --password [password] --bmc_url https://[bmc_ip]/redfish/v1 --manager_url v1/Managers/1 --image_url [URL, e.g. https://example.com/my.iso] --eject true

Supermicro 5039MS:
python vmedia-attach.py --username [username] --password [password] --bmc_url https://[bmc_ip]/redfish/v1 --manager_url v1/Managers/1/VM1/CfgCD --image_url [URL, e.g. https://example.com/my.iso]
