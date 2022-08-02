# redfish-vmedia-test
A simple tool which can validate virtual media attachment and detachment via Redfish using sushy library

Usage:

Dell R640:
python vmedia-attach.py --username [username] --password [password] --bmc_url https://[bmc_ip]/redfish/v1 --manager_url v1/Managers/iDRAC.Embedded.1 --image_url [URL, e.g. https://example.com/my.iso] --type dvd

HP e910:
python vmedia-attach.py --username [username] --password [password] --bmc_url https://[bmc_ip]/redfish/v1 --manager_url v1/Managers/1 --image_url [URL, e.g. https://example.com/my.iso] --eject true --type usb

Supermicro 5039MS:
python vmedia-attach.py --username [username] --password [password] --bmc_url https://[bmc_ip]/redfish/v1 --manager_url v1/Managers/1/VM1/CfgCD --image_url [URL, e.g. https://example.com/my.iso]

# bootseq-update
A simple tool which can validate boot order changes via Redfish using sushy library

Usage:

Dell R640:
python change_bootseq.py --username [username] --password [password] --bmc_url https://[bmc_host] --system_url /redfish/v1/Systems/System.Embedded.1 --boot_device hdd

HP DL360 G9
python change_bootseq.py --username [username] --password [password] --bmc_url https://[bmc_host] --system_url /redfish/v1/Systems/1/ --boot_device hdd

