import gitwrapper
import pathlib
import sys
import subprocess

cpath="config/"

def get_requirements(konops_id, token, headers):
    requirement_file_path = cpath + konops_id + "_requirements.txt"
    response , requirement_content_json = gitwrapper.get_file_contents(self.token, self.headers, config_file_path)

current_path = str(pathlib.Path(__file__).parent.absolute())
requirements_file_path = current_path + "\libs.txt"

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file_path])