import netmiko
import os.path
import datetime
import concurrent
import device_data



def target_router (ip):

    try: #Test, kalo berhasil = disimpen, kalo gagal -> lempar exception
        date_now = datetime.now() #get waktu sekarang
        time_stamp = date_now.strftime("%d-%m-%y_%H_%M_%S")
        #Library yang akan dipakai untuk attempt connect ke device.
        device = {
            'device_type': 'cisco_ios',
        }
        device['host'] = ip
        device ['username'] = device_data.username
        device['password'] = device_data.password
        print(device) #printout informasi perangkat yang sedang dieksekusi
        #initiating connection
        connect_to_device = netmiko.ConnectHandler(**device)
        connect_to_device.enable()

        #Define hostname (ngambil informasi hostname perangkat dari cli)
        get_hostname = connect_to_device.send_command('show run | in hostname')
        split_hostname = get_hostname.split()

        #define file name & path lokasi penyimpanan dari output .log
        file_path = "OutputFileCapture/"
        hostname_n_date= split_hostname[1] + '-' + time_stamp + '.log'
        file_name = os.path.join(file_path, hostname_n_date)

        #Looping command (sequential) dari file device_data (yang ngambil command dari file list_command)

        for command in device_data.list_command:
            output_command = connect_to_device.send_command(f"{command}")
            print(output_command)
            with open(file_name, 'a') as file:
                file.write(f'''\n{command}\n{output_command}\n\n''')

    except netmiko.NetmikoTimeoutException:
        print(f"Gagal mencapture Device {ip} in {time_stamp} Karena Connection Timeout ")
        with open("list_failed_capture.txt", 'a') as file_list_failed_capture:
            file_list_failed_capture.write(
                f'''\nGagal mencapture Device {ip} in {time_stamp} Karena Connection Timeout\n''')
    except netmiko.NetmikoAuthenticationException:
        print(f"Gagal mencapture Device {ip} in {time_stamp} Karena Gagal Authentikasi ")
        with open("list_failed_capture.txt", 'a') as file_list_failed_capture:
            file_list_failed_capture.write(
                f'''\nGagal mencapture Device {ip} in {time_stamp} Karena Gagal Authentikasi\n''')
