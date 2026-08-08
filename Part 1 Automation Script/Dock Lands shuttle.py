import jarray
import jmri
class LCCTest(jmri.jmrit.automat.AbstractAutomaton) :
    def init(self):
        # init() is called exactly once at the beginning to do
        # any necessary configuration.
        print "Inside init(self)"
        # set up sensor numbers
        # fwdSensor is reached when loco is running forward
        self.S402 = sensors.provideSensor("S402")
        self.S403 = sensors.provideSensor("S403")
        self.S404 = sensors.provideSensor("S404")
        self.S407 = sensors.provideSensor("S407")
        # get loco address. For long address change "False" to "True"
        self.throttle = self.getThrottle(4, False) # Jinty
        return
    def handle(self):
        # handle() is called repeatedly until it returns false.
        print "Inside handle(self)"

        # set loco to forward
        print "Set Loco Forward"
        self.throttle.setIsForward(True)
        # wait 1 second for layout to catch up, then set speed
        self.waitMsec(1000)
        print "Set Speed"
        self.throttle.setSpeedSetting(0.5)
       
        #speed up
        self.waitSensorActive(self.S403)
        self.throttle.setSpeedSetting(0.8)
       
        self.waitSensorActive(self.S404)
        self.throttle.setSpeedSetting(0.5)
       
        # wait for sensor in forward direction to trigger, then stop
        print "Wait for Forward Sensor"
        self.waitSensorActive(self.S407)
        print "Set Speed Stop"
        self.throttle.setSpeedSetting(0)
        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 8 seconds"
        self.waitMsec(8000) # wait for 8 seconds

        print "Set Loco Reverse"
        self.thrott