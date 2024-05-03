import subprocess

network_name = input("Enter Network Name: ")

wifi = f"""netsh wlan show profile "{network_name}" key=clear """

run = subprocess.run(wifi,shell=True)
print(run)