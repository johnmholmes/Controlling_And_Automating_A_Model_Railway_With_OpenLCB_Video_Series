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
        self.S403  = sensors.provideSensor("S403")
        self.S404 = sensors.provideSensor("S404")
        self.S407  = sensors.provideSensor("S407")

        # get loco address. For long address change "False" to "True"
        self.throttle = self.getThrottle(10, False)  # Jinty

        return

    def handle(self):
        # handle() is called repeatedly until it returns false.
        print "Inside handle(self)"
        
        turnouts.getTurnout("T4").setState(CLOSED)
        turnouts.getTurnout("T3").setState(CLOSED)
        
        sensors.provideSensor("SL608").setState(ACTIVE)
        self.waitMsec(100)
        sensors.provideSensor("SL602").setState(ACTIVE)
        self.waitMsec(80)
        sensors.provideSensor("SL401").setState(ACTIVE)
        self.waitMsec(90)
        sensors.provideSensor("SL402").setState(ACTIVE)
        self.waitMsec(100)
        sensors.provideSensor("SL403").setState(ACTIVE)
        self.waitMsec(80)
        sensors.provideSensor("SL404").setState(ACTIVE)
        self.waitMsec(90)
        sensors.provideSensor("SL405").setState(ACTIVE)
        self.waitMsec(100)
        sensors.provideSensor("SL406").setState(ACTIVE)
        self.waitMsec(90)
        sensors.provideSensor("SL407").setState(ACTIVE)
        self.waitMsec(100)
        sensors.provideSensor("SL408").setState(ACTIVE)
        self.waitMsec(90)
        sensors.provideSensor("SL409").setState(ACTIVE)
        self.waitMsec(100)
        
        print "Turnout Set"
        self.waitMsec(1000)
        sensors.provideSensor("SH1R").setState(INACTIVE)
        sensors.provideSensor("SH6R").setState(ACTIVE)
        
        self.waitMsec(500)
        sensors.provideSensor("SH1G").setState(ACTIVE)

        # set loco to forward
        print "Set Loco Forward"
        self.throttle.setIsForward(True)

        # wait 1 second for layout to catch up, then set speed
        self.waitMsec(1000)
        print "Set Speed"
        self.throttle.setSpeedSetting(0.25)
        
        #speed up
        self.waitSensorActive(self.S403)
        self.throttle.setSpeedSetting(0.3)
        self.waitMsec(1500)
        self.throttle.setSpeedSetting(0.25)
        self.waitSensorActive(self.S404)
        self.throttle.setSpeedSetting(0.2)
        
        sensors.provideSensor("SH1G").setState(INACTIVE)
        sensors.provideSensor("SH1R").setState(ACTIVE)

        # wait for sensor in forward direction to trigger, then stop
        print "Wait for Forward Sensor"
        self.waitSensorActive(self.S407)
        print "Set Speed Stop"
        self.throttle.setSpeedSetting(0)

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 8 seconds"
        self.waitMsec(8000)          # wait for 8 seconds
        
        sensors.provideSensor("SH6R").setState(INACTIVE)
        sensors.provideSensor("SH6G").setState(ACTIVE)

        print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(1000)                 # wait 1 second for Xpressnet to catch up
        print "Set Speed"
        self.throttle.setSpeedSetting(0.2)
        self.waitSensorActive(self.S403)
        
        sensors.provideSensor("SH6G").setState(INACTIVE)
        sensors.provideSensor("SH6R").setState(ACTIVE)
        

        # wait for sensor in reverse direction to trigger
        print "Wait for Reverse Sensor"
        self.waitSensorActive(self.S402)
        print "Set Speed Stop"
        self.waitMsec(10)
        self.throttle.setSpeedSetting(0)
        
        sensors.provideSensor("SL608").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL602").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL401").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL402").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL403").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL404").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL405").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL406").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL407").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL408").setState(INACTIVE)
        self.waitMsec(20)
        sensors.provideSensor("SL409").setState(INACTIVE)
        self.waitMsec(20)

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 20 seconds"
        self.waitMsec (20000)          # wait for 20 seconds
        
        

        # and continue around again
        print "End of Loop"
        return 1
        # (requires JMRI to be terminated to stop - caution
        # doing so could leave loco running if not careful)

# end of class definition

# start one of these up
LCCTest().start()