import rclone, pprint

#cfg = """[local]
#type = local
#nounc = true"""
#result = rclone.with_config(cfg).run_cmd(command="lsd", extra_args=["local:/tmp", "-v", "--dry-run"])

mygoogledrive2_cfg = """[mygoogledrive2]
type = drive
scope = drive
token = {"access_token":"ya29.ImC8BzOh02AkahtAhkC8sm3r2MNVJYwRRaJ-u1Cr4uQn3rRANSK_UTWgShIrg1nndaDXJd1H-euzfDrvxOFkxI1A5BDaeI_ab-yU-BN4y2Xti8OeofTLkYnXk53v7NoLnRI","token_type":"Bearer","refresh_token":"1//0e9kfTR1JGbTjCgYIARAAGA4SNwF-L9IrkEnACmem8HG0D2IV0AjEFbb_7IBcvzOn7YZxcweuQZFMnysmIwofmzzmMsmFeXlGSlY","expiry":"2020-02-03T14:12:24.341991966+08:00"}
root_folder_id = 1IMniHYS6wBUG31MWd_4nTIkBgpc-Llrz
"""

mys3_cfg = """[mys3]
type = s3
provider = AWS
env_auth = false
access_key_id = AKIAWXRFORUZI2FU7LXP
secret_access_key = 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
region = us-east-1
"""

result2 = rclone.with_config(mygoogledrive2_cfg).run_cmd(command="sync", extra_args=["mygoogledrive2:/", "-v", "mys3:/noel-fonseca-bucket-1"])

#pprint.pprint(result2)

pprint.pprint(result2.get('out'))
# b'local:\n'
#pprint.pprint(result2.get('code'))
# 0
#pprint.pprint(result2.get('error'))
# b''


#token = {"access_token":"ya29.ImC8BzOh02AkahtAhkC8sm3r2MNVJYwRRaJ-u1Cr4uQn3rRANSK_UTWgShIrg1nndaDXJd1H-euzfDrvxOFkxI1A5BDaeI_ab-yU-BN4y2Xti8OeofTLkYnXk53v7NoLnRI","token_type":"Bearer","refresh_token":"1//0e9kfTR1JGbTjCgYIARAAGA4SNwF-L9IrkEnACmem8HG0D2IV0AjEFbb_7IBcvzOn7YZxcweuQZFMnysmIwofmzzmMsmFeXlGSlY","expiry":"2020-02-03T14:12:24.341991966+08:00"}


