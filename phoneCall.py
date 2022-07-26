# from __future__ import division
import sys
import io
import proto
import serial
import serial.tools.list_ports

# device_name = 'USB-SERIAL'
stop_signal = False

def connect_SIM800C(device_name):
    port_list = list(serial.tools.list_ports.comports())

    if len(port_list) == 0:
        print("\nno port can be used :(")
        exit(0)
    
    # find the correct port for data transmission
    for i in port_list:
        if str(i).find(device_name) != -1: # plz modify the device name if needed
            s = serial.Serial(i.device, 115200, timeout=0)
    sio = io.TextIOWrapper(io.BufferedRWPair(s, s))
    sio.write(f'AT+DDET=1\nATS0=0\nATE1\nAT+COLP=1\nAT+CLIP=1\n')
    # sio.write(f'ATE1\nAT+COLP=1\n')
    sio.flush()
    return sio

def calling(phonenum, SIM800C):
        global stop_signal
        stop_signal = False
        
        SIM800C.write(f'ATD{str(phonenum)};\n')
        ''' 
        ATE1: 用於設置開啓回顯模式，檢測Module與串口是否連通，能否接收AT命令
        開啓回顯，有利於調試
        
        AT+COLP=1: 開啓被叫號碼顯示，即成功撥通的時候（被叫接聼電話），模塊會
        返回被叫號碼      
        
        ATD電話號碼;:用於撥打電話號碼
        '''

        SIM800C.flush()
        print("Calling (If it cannot work for long, please use XCOM V2.0 to check)....")
        while not stop_signal:
            try:
                x = "".join(SIM800C.readlines())
            except Exception:
                print("\nError occurs accidentally, check the port or other devices :(")
                exit()

            # Dailed
            if x.find('+COLP: \"') != -1:
                print("\ndialed")            

            if x.find('NO CARRIER') != -1:
                print("\nRing off")
                break

            if (x.find('BUSY') != -1) | (x.find('NO ANSWER') != -1):
                print("\nHe/She hangs up")
                break

            if (x.find('ERROR') != -1): 
                print("\nErrors occurr in SIM card (it's not China Mobile card or it arrears), \nor in other devices, \nor Card installation error")
                break
        print("break")

def cut_off(SIM800C):
    global stop_signal
    SIM800C.write(f'ATH\n')
    SIM800C.flush()
    stop_signal = True
    print("Cut off the phone")

def accept_call(SIM800C):
    global stop_signal
    stop_signal = False
    SIM800C.write(f'ATA\n')
    SIM800C.flush()
    print("Accept the call")
    while not stop_signal:
        try:
            x = "".join(SIM800C.readlines())
        except Exception:
            print("\nError occurs accidentally, check the port or other devices :(")
            exit()

        if x.find('NO CARRIER') != -1:
            print("\nRing off")
            break

        if (x.find('BUSY') != -1) | (x.find('NO ANSWER') != -1):
            print("\nHe/She hangs up")
            break

        if (x.find('ERROR') != -1): 
            print("\nErrors occurr in SIM card (it's not China Mobile card or it arrears), \nor in other devices, \nor Card installation error")
            break
    print("break")
    
def main():
    print("calling to " + sys.argv[1])
    calling(str(sys.argv[1])) # Fill your telephone number
    
    print("Done")
    exit()

if __name__ == "__main__":
    main()