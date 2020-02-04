import rclone, pprint

cfg_path = r'/home/nfonseca/.config/rclone/rclone.conf'

with open(cfg_path) as f:
   cfg = f.read()

result = rclone.with_config(cfg).listremotes()

rclone.with_config(cfg).run_cmd(command='sync', extra_args=["-v", "--ignore-checksum", "mygoogledrive2:/", "mys3:/noel-fonseca-bucket-1"])

pprint.pprint(rclone.with_config(cfg).run_cmd(command='ls', extra_args=["-v", "mys3:/noel-fonseca-bucket-1"]))