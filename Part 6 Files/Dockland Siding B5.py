import jarray
import jmri

class LCCTest(jmri.jmrit.automat.AbstractAutomaton) :

    def init(self):
        # init() is called exactly once at the beginning to do
        # any necessary configuration.
        print "Inside init(self)"

        # set up sensor numbers
        
        # Route 5 Sensors
        self.S402 = sensors.provideSensor("S402")   # P2 end
        self.S403 = sensors.provideSensor("S403")   # P2 Ent
        self.S404 = sensors.provideSensor("S404")   # Siding Ent
        self.S407 = sensors.provideSensor("S407")   #Siding End
        
        # Route 1 Sensors
        #self.S402 = sensors.provideSensor("S402")  # P2 end
        #self.S403 = sensors.provideSensor("S403")  # P2 Ent
        self.S405 = sensors.provideSensor("S405")   # T3 T4 crossover
        self.S604 = sensors.provideSensor("S604")   # Dockland Approach T3 end
        self.S603 = sensors.provideSensor("S603")   # Dockland Approach T2 end
        self.S601 = sensors.provideSensor("S601")   # Peel Approach T2 end
        self.S705 = sensors.provideSensor("S705")   # Peel Approach T1 end
        self.S702 = sensors.provideSensor("S702")   # Peel P2 Ent
        self.S704 = sensors.provideSensor("S704")   # Peel P2 end end

        # get loco address. For long address change "False" to "True"
        self.throttle = self.getThrottle(10, False)  # Black 5

        return
    
    def handle(self):
        # handle() is called repeatedly until it returns false.
        
        print "Set signals and Turnouts For Star Of Day"
        
        sensors.provideSensor("SH1R").setState(ACTIVE)
        sensors.provideSensor("SH2R").setState(ACTIVE)
        sensors.provideSensor("SH3R").setState(ACTIVE)
        sensors.provideSensor("SH4R").setState(ACTIVE)
        sensors.provideSensor("SH5R").setState(ACTIVE)
        sensors.provideSensor("SH6R").setState(ACTIVE)
        sensors.provideSensor("SH7R").setState(ACTIVE)
        sensors.provideSensor("SH8R").setState(ACTIVE)
        sensors.provideSensor("SH9R").setState(ACTIVE)
        
        self.waitMsec(1000)
        turnouts.getTurnout("T4").setState(CLOSED)
        self.waitMsec(1000)
        turnouts.getTurnout("T3").setState(CLOSED)
        self.waitMsec(1000)
        turnouts.getTurnout("T2").setState(CLOSED)
        self.waitMsec(1000)
        turnouts.getTurnout("T1").setState(CLOSED)
        self.waitMsec(1000)
        
        print "Prepare for start of automation"
        sensors.provideSensor("SH6R").setState(INACTIVE)
        sensors.provideSensor("SH6G").setState(ACTIVE)
        
        print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(1000)
        
        print "Start the move to Dock Lands P2"
        self.throttle.setSpeedSetting(0.30)
        self.waitSensorActive(self.S403)
        sensors.provideSensor("SH6G").setState(INACTIVE)
        sensors.provideSensor("SH6R").setState(ACTIVE)
        self.throttle.setSpeedSetting(0.20)
        self.waitSensorActive(self.S402)
        self.throttle.setSpeedSetting(0.0)
        
        print "Start Journey to Peel Platform 2"
        self.throttle.setIsForward(True)
        self.waitMsec(1000)
        turnouts.getTurnout("T4").setState(THROWN)
        turnouts.getTurnout("T3").setState(THROWN)
        self.waitMsec(1000)
        sensors.provideSensor("SH1R").setState(INACTIVE)
        sensors.provideSensor("SH1G").setState(ACTIVE)
        self.waitMsec(1000)
        self.throttle.setSpeedSetting(0.25)
        self.waitSensorActive(self.S405)
        sensors.provideSensor("SH1G").setState(INACTIVE)
        sensors.provideSensor("SH1R").setState(ACTIVE)
        self.waitSensorActive(self.S604)
        self.waitMsec(1000)
        self.throttle.setSpeedSetting(0.0)
        
        print "Waiting for T2 change and signal changes"
        self.waitMsec(5000)
        
        print "Turnout 2 & 1 Set and signals"
        turnouts.getTurnout("T2").setState(THROWN)
        turnouts.getTurnout("T1").setState(THROWN)
        self.waitMsec(1000)
        sensors.provideSensor("SH5R").setState(INACTIVE)
        sensors.provideSensor("SH5G").setState(ACTIVE)
        sensors.provideSensor("SH9R").setState(INACTIVE)
        sensors.provideSensor("SH9G").setState(ACTIVE)
        
        print "Go to Peel P2"
        self.waitMsec(1000)
        self.throttle.setSpeedSetting(0.3)
        self.waitMsec(1000)
        self.throttle.setSpeedSetting(0.4)
        self.waitSensorActive(self.S601)
        sensors.provideSensor("SH5G").setState(INACTIVE)
        sensors.provideSensor("SH5R").setState(ACTIVE)
        self.throttle.setSpeedSetting(0.35)
        self.waitSensorActive(self.S705)
        self.throttle.setSpeedSetting(0.25)
        self.waitSensorActive(self.S702)
        sensors.provideSensor("SH9G").setState(INACTIVE)
        sensors.provideSensor("SH9R").setState(ACTIVE)
        self.throttle.setSpeedSetting(0.2)
        self.waitSensorActive(self.S704)
        self.throttle.setSpeedSetting(0.0)
        
        print "Arrived at Peel Station and waiting"
        
        self.waitMsec(20000)
        
        print "Resetting the scene"
        
        self.throttle.setIsForward(False)
        self.waitMsec(1000)
        sensors.provideSensor("SH7R").setState(INACTIVE)
        sensors.provideSensor("SH7G").setState(ACTIVE)
        sensors.provideSensor("SH3R").setState(INACTIVE)
        sensors.provideSensor("SH3G").setState(ACTIVE)
        self.throttle.setSpeedSetting(0.25)
        self.waitSensorActive(self.S403)
        self.throttle.setSpeedSetting(0.15)
        self.waitSensorActive(self.S402)
        self.throttle.setSpeedSetting(0.0)
        
        sensors.provideSensor("SH7G").setState(INACTIVE)
        sensors.provideSensor("SH3G").setState(INACTIVE)
        sensors.provideSensor("SH7R").setState(ACTIVE)
        sensors.provideSensor("SH3R").setState(ACTIVE)
        
        turnouts.getTurnout("T4").setState(CLOSED)
        turnouts.getTurnout("T3").setState(CLOSED)
        turnouts.getTurnout("T2").setState(CLOSED)
        turnouts.getTurnout("T1").setState(CLOSED)
        
        self.waitMsec(2000)
        
        sensors.provideSensor("SH1R").setState(INACTIVE)
        sensors.provideSensor("SH1G").setState(ACTIVE)
        self.throttle.setIsForward(True)
        self.waitMsec(1000)
        self.throttle.setSpeedSetting(0.2)
        self.waitSensorActive(self.S407)
        self.throttle.setSpeedSetting(0.0)
        
        sensors.provideSensor("SH1G").setState(INACTIVE)
        sensors.provideSensor("SH1R").setState(ACTIVE)
    
        print "End of Loop"
        return 0
        # (requires JMRI to be terminated to stop - caution
        # doing so could leave loco running if not careful)

# end of class definition

# start one of these up
LCCTest().start()
        
        
        
        
        
        