import subprocess
import time

import requests


def wait_for_server_to_start():
    for i in range(50):
        print(f'waited {i * 2} seconds for server...')
        r = requests.get('http://127.0.0.1:5000/status')
        if r.status_code == 200:
            return
        time.sleep(2)
    print("Server took too long to start")


server_env = {
    'FLASK_APP': 'invisible_flow/app.py',
    'ENVIRONMENT': 'local',
}
python_executable = 'venv/bin/python'
# start the server
server_process = subprocess.Popen(f'{python_executable} -m flask run', shell=True, env=server_env)

wait_for_server_to_start()

# Run the tests
test_process = subprocess.run('pytest api_tests/', shell=True, capture_output=True, text=True)

print('-----------------Test output')
print(test_process.stdout)

server_process.terminate()
# sys.exit(test_process.returncode)
