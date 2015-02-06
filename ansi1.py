#!/usr/bin/env python
#coding:utf-8
import ansible.runner
import ansible.inventory
import json
def AnsibleApi(AnsibleModuleName,AnsibleInventory,AnsibleCommand):
	ReturnMsg = {}
	runner = ansible.runner.Runner(
		module_name = AnsibleModuleName,
		inventory = AnsibleInventory,
		module_args = AnsibleCommand,
		environment = {'LANG':'zh_CN.UTF-8','LC_CTYPE':'zh_CN.UTF-8'},	
	)
	ReturnValue = runner.run()
	if ReturnValue is None:
		ReturnMsg['code'] = "-1"
		ReturnMsg['msg'] = "hosts not found"
	for (hostname,result) in ReturnValue['contacted'].items():
		if result['rc'] == "0":
			ReturnMsg['code'] = "0"
			ReturnMsg['msg'] = result['stdout']
		else:
			ReturnMsg['code'] = str(result['rc'])
			ReturnMsg['msg'] = result['stdout']
	for (hostname,result) in ReturnValue['dark'].items():
		ReturnMsg['code'] = "-3"
		ResturnMsg['msg'] = result
	return json.dumps(ReturnMsg)
def checklog():
#	hosts = ["127.0.0.1"]
	hosts = ["211.237.12.88"]
	AnsibleModuleName = "command"
	AnsibleInventory = ansible.inventory.Inventory(hosts)
	AnsibleCommand = "tail -n 20 /var/log/messages"
	AnsibleResult = AnsibleApi(AnsibleModuleName,AnsibleInventory,AnsibleCommand)
	print AnsibleResult
checklog()
