import socket
import threading
import requests
import ipaddress

class IpInfo:
    def __init__(self):
        self.ip = input('\n IP Для Сканирования\n $> ')

        try:
            ipaddress.ip_address(self.ip)
        except ValueError:
            raise ValueError('IP адресс введён неверно')

        self.output()

    def default_info(self):
        r = requests.get(f'http://ip-api.com/json/{self.ip}').json()
        host = socket.getnameinfo((self.ip, 0), socket.NI_NUMERICHOST)

        out = {
            'api': r,
            'host': host
        }

        return out

    def open_ports(self):
        open_ports_list = []

        def scan_port(ip, port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            try:
                sock.connect((ip, port))
                open_ports_list.append(str(port))
                sock.close()
            except:
                pass

        for i in range(65535):
            thread_ = threading.Thread(target=scan_port, args=(self.ip, i))
            thread_.start()

        return open_ports_list

    def output(self):

        def len_design():
            return 14

        default = self.default_info()
        api = default['api']
        host = default['host']

        open_ports = self.open_ports()

        print(' ' + "=" * len_design() + f'''
  IP adress:   {self.ip}
  Country:     {api["country"]}
  Region:      {api["region"]}\n  Region Name: {api["regionName"]}
  City:        {api["city"]}\n  Zip:         {api["zip"]}
  Latinude:    {api["lat"]}\n  Longitude:   {api["lon"]}
  Timezone:    {api["timezone"]}\n  ISP:         {api["isp"]}
  Org:         {api["org"]}\n  As:          {api["as"]}
  Host:        {host[0]}\n  Open ports:  {', '.join(open_ports)}
 ''' + "=" * len_design())

        input()

def bssid_info():
    print('\n Введите BSSID')
    query = input(f' $> ')
    try:
        response = requests.get(
            "https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=" + query)
        data = response.json()
        status = data["result"]
        if status == 200:
            lat = data["data"]["lat"]
            lon = data["data"]["lon"]

            print('\n=============================')
            print(f' BSSID: {query}\n Latinude: {lat}\n  Longitude: {lon}')
            print(' =============================')
        else:
            error_code = data["message"]
            error_message = data["desc"]
            print('\n=============================')
            print(f' BSSID: {query}\n Error code: {error_code}\n Error message: {error_message}')
            print('=============================')
    except:
        print(f' НАПИШИ ВЕРНО!')
    input()
