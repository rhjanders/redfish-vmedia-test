import logging
import sushy
from sushy import auth
from sushy import exceptions
import urllib3
urllib3.disable_warnings()
import argparse
import sys
import time

LOG = logging.getLogger('sushy')
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler())

parser = argparse.ArgumentParser()
parser.add_argument("--username")
parser.add_argument("--password")
parser.add_argument("--bmc_url")
parser.add_argument("--system_url")
parser.add_argument("--boot_device")
args = parser.parse_args()

if args.boot_device == "pxe":
    bootdev = sushy.BOOT_SOURCE_TARGET_PXE
if args.boot_device == "hdd":
    bootdev = sushy.BOOT_SOURCE_TARGET_HDD

basic_auth = auth.BasicAuth(username=args.username, password=args.password)
s = sushy.Sushy(args.bmc_url, verify=False, auth=basic_auth)

system = s.get_system(args.system_url)
try:
    system.set_system_boot_options(bootdev, sushy.BOOT_SOURCE_ENABLED_ONCE)
    print("Setting boot device succeeded")
except sushy.exceptions.SushyError as exc:
    print("Setting boot device failed:", str(exc))
