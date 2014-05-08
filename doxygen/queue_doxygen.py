#!/usr/bin/env python

# This script adds a set of doxygen creation commands to the queue system based
# on the CIG codes described in the ../cig_codes.py module. It can create
# documentation for release or repository code for single or all codes.

from __future__ import print_function
import sys
sys.path.append("..")
import cig_codes
import os
import subprocess

def main():
    if len(sys.argv) != 3:
        print("syntax:", sys.argv[0], "[code_name|all] [release|dev]")
        exit(1)

    # Parse input arguments
    req_name = sys.argv[1]
    code_type = sys.argv[2]
    if code_type != "release" and code_type != "dev":
        print("Unknown type (must be release or dev)")
        exit(1)

    # Go through all the recorded CIG codes
    for code_name in cig_codes.code_db.codes():
        if req_name != "all" and req_name != code_name: continue
        cmd_dict = {}
        cmd_dict["queue_cmd"] = "../queue/queue_daemon.sh backend_queue"
        cmd_dict["code_name"] = code_name
        cmd_dict["full_name"] = cig_codes.code_db.full_name[code_name]
        if code_type == "release" and cig_codes.code_db.doxygen_params[code_name].release_dox:
            cmd_dict["code_url"] = cig_codes.code_db.release_src[code_name]
            cmd_dict["code_version"] = cig_codes.code_db.release_version[code_name]
            sys_cmd = "{queue_cmd} \"cd `pwd` ; ./generate_doxygen.sh url {code_url} {code_version} \\\"{full_name}\\\" {code_name}\" &".format(**cmd_dict)
            os.system(sys_cmd)
        elif code_type == "dev" and cig_codes.code_db.doxygen_params[code_name].dev_dox:
            cmd_dict["repo_url"] = cig_codes.code_db.repo_url[code_name]
            cmd_dict["repo_type"] = cig_codes.code_db.repo_type[code_name]
            # Determine the latest revision number of the repository
            if cig_codes.code_db.repo_type[code_name] == "git":
                cmd_dict["repo_version"] = subprocess.check_output("git ls-remote {repo_url}".format(**cmd_dict).split()).split()[0]
            else:
                print("Unknown repository type for", code_name, "(must be git)")
                exit(1)
            sys_cmd = "{queue_cmd} \"cd `pwd` ; ./generate_doxygen.sh {repo_type} {repo_url} {repo_version} \\\"{full_name}\\\" {code_name}\" &".format(**cmd_dict)
            os.system(sys_cmd)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        cig_codes.send_cig_error_email("Doxygen queueing error", str(e))

