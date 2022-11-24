#Perintah dibawah untuk import list command yang mau diambil per device dari file dan list ip

with open("list_command.txt", "r") as file_list_command:
    list_command=file_list_command.read().split("\n")
    print(f"List Command yang ingin di ambil {list_command}")

with open("list_ip.txt", "r") as file_list_ip:
    list_ip=file_list_ip.read().split("\n")
    print(f"List Perangkat yang ingin di capture {list_ip}")

##Perintah untuk mendapatkan input user dan password
username = input("Masukan Username ?")
password = input("Masukan password ?")
secret = input("Masukan secret ?")