import subprocess
import sys
import time

server_env = {
    'FLASK_APP': 'invisible_flow/app.py',
    'ENVIRONMENT': 'local',
}
python_executable = 'venv/bin/python'
# start the server
server_process = subprocess.Popen(f'{python_executable} -m flask run', shell=True, env=server_env)
# Give the server time to start
time.sleep(2)

# Run the tests
test_process = subprocess.run('pytest api_tests/', shell=True, capture_output=True, text=True)

print('-----------------Test output')
print(test_process.stdout)

server_process.terminate()
sys.exit(test_process.returncode)
