from modbus_tk import modbus_rtu
import serial

socket2 = serial.Serial(port='/dev/ttyS1', baudrate=9600, bytesize=8, parity='N', stopbits=1,
                        timeout=1, xonxoff=0)
master = modbus_rtu.RtuMaster(socket2)
master.set_timeout(1.0)
try:
    result = master.execute(slave=1, function_code=3, starting_address=0x007D,
                            quantity_of_x=1, output_value=13)
    print("dsp version: ", result)
    result1 = master.execute(slave=1, function_code=3, starting_address=0x0083,
                             quantity_of_x=1, output_value=13)
    print("arm version: ", result1)
except Exception as e:
    print(e)
