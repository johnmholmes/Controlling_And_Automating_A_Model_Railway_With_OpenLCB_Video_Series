import jmri

class LCCTest(jmri.jmrit.automat.AbstractAutomaton):

    def init(self):
        print("LCCTest: init()")

        # --- Layout sensors (cached once) ---
        self.S402 = sensors.provideSensor("S402")   # reverse end
        self.S403 = sensors.provideSensor("S403")   # intermediate
        self.S404 = sensors.provideSensor("S404")   # intermediate
        self.S407 = sensors.provideSensor("S407")   # forward end

        # --- Signal / aspect sensors (also cached) ---
        self.SH1R = sensors.provideSensor("SH1R")
        self.SH1G = sensors.provideSensor("SH1G")
        self.SH6R = sensors.provideSensor("SH6R")
        self.SH6G = sensors.provideSensor("SH6G")

        # --- Throttle ---
        self.throttle = self.getThrottle(4, False)  # short address 4 = Jinty
        if self.throttle is None:
            print("ERROR: Could not acquire throttle for address 4")
            return

        # Optional: give the automaton a nice name in the thread monitor
        self.setName("LCCTest - Jinty shuttle")

    def handle(self):
        print("=== Starting forward run ===")

        # Set signals for forward
        self.SH1R.setKnownState(INACTIVE)
        self.SH6R.setKnownState(ACTIVE)
        self.waitMsec(300)
        self.SH1G.setKnownState(ACTIVE)

        # Direction + speed
        self.throttle.setIsForward(True)
        self.waitMsec(800)                      # allow direction to settle
        self.throttle.setSpeedSetting(0.5)

        # Speed profile on the way
        self.waitSensorActive(self.S403)
        self.throttle.setSpeedSetting(0.8)

        self.waitSensorActive(self.S404)
        self.throttle.setSpeedSetting(0.5)

        # Approach signal change
        self.SH1G.setKnownState(INACTIVE)
        self.SH1R.setKnownState(ACTIVE)

        # Stop at far end
        self.waitSensorActive(self.S407)
        self.throttle.setSpeedSetting(0.0)
        print("Stopped at S407 – waiting for inertia")
        self.waitMsec(8000)

        # ---------- Reverse run ----------
        print("=== Starting reverse run ===")

        self.SH6R.setKnownState(INACTIVE)
        self.SH6G.setKnownState(ACTIVE)

        self.throttle.setIsForward(False)
        self.waitMsec(800)
        self.throttle.setSpeedSetting(0.4)

        self.waitSensorActive(self.S403)

        # Signal change while moving
        self.SH6G.setKnownState(INACTIVE)
        self.SH6R.setKnownState(ACTIVE)

        # Stop at near end
        self.waitSensorActive(self.S402)
        self.waitMsec(300)                      # short coast
        self.throttle.setSpeedSetting(0.0)
        print("Stopped at S402 – waiting for inertia")
        self.waitMsec(8000)

        print("=== End of loop – repeating ===")
        return True                             # keep running

# ------------------------------------------------------------------
# Create and start
a = LCCTest()
a.start()
