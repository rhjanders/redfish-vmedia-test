import sushy
from sushy import auth
from sushy import exceptions
import urllib3
urllib3.disable_warnings()
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--username")
parser.add_argument("--password")
parser.add_argument("--bmc_url")
parser.add_argument("--manager_url")
parser.add_argument("--image_url")
parser.add_argument("--eject")
parser.add_argument("--type")
args = parser.parse_args()

basic_auth = auth.BasicAuth(username=args.username, password=args.password)
s = sushy.Sushy(args.bmc_url, verify=False, auth=basic_auth)
mgr_inst = s.get_manager(args.manager_url)
vmedia_list = mgr_inst.virtual_media.get_members()

for vmedia in vmedia_list:
    if args.type in vmedia.media_types:
        if args.eject:
            vmedia.eject_media()
        vmedia.refresh()
        print("vmedia state prior to attempting attach: media_types:", vmedia.media_types, "image:" , vmedia.image, "inserted:", vmedia.inserted)
        vmedia.insert_media(args.image_url, inserted=True, write_protected=True)
        vmedia.refresh()
        print("vmedia state after attempting attach: media_types:", vmedia.media_types, "image:" , vmedia.image, ",inserted:", vmedia.inserted)
