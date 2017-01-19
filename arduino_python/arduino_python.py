import pyfirmata
from time import sleep
import os
import web

class Arduino:
    db = web.database(dbn='mysql', host='localhost', db='arduino', user='root', pw='toor')
    def setup(self):
        self.port = '/dev/ttyACM0'
        self.board = pyfirmata.Arduino(self.port)
        self.it	=	pyfirmata.util.Iterator(self.board)
        self.it.start()
        self.A5	= self.board.get_pin('a:5:i')
        self.D13 = self.board.get_pin('d:13:o')

    def	pause(self, ptime, message):
        print message
        sleep(ptime)

    
    def getValueA5(self):
        return self.A5.read()
    
    def setValueD13(self, value):
        self.D13.write(value)

    def update(self, id, value):
        try:
            self.db.update('data', where='id=$id', vars=locals(), value=value)
        except Exception, e:
            print "Error ", e

    def insert(self, value):
        try:
            self.db.insert('data', value=value)
        except Exception, e:
            print "Error ", e
    
    def select(self):
        try:
            values = self.db.select('data')
            for value in values:
                print value.id, value.value, value.update_time
        except Exception, e:
            print "Error ", e

    def selectControl(self):
        value = self.db.select('control', order='id DESC', limit=1)[0]
        return value.value

arduino_uno = Arduino()
print 'Setup init'
arduino_uno.setup()
arduino_uno.pause(3,'Setup finish')

try:
    while True:
        if arduino_uno.selectControl() == 1:
            arduino_uno.setValueD13(1)
        else:
            arduino_uno.setValueD13(0)
        arduino_uno.update(1, arduino_uno.getValueA5())
        arduino_uno.pause(1, 'Guardando')
except	KeyboardInterrupt:
    arduino_uno.board.exit()
    os._exit(1)
