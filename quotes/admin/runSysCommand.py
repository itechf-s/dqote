from dqote import env
import subprocess

scriptPath = env.get('admin', 'SCRIPT_PATH')

def run(cmd, site):
    sudo = 'sudo -S <<< Aircel#1 runuser -u ahmad '
    print('command : ', cmd, ' | site : ', site)
    process = subprocess.run([sudo + scriptPath + cmd, site ], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    
    return (cmd + ' ' + site, process.stdout.decode('utf-8'), process.stderr.decode('utf-8'))
    
