
| Area | Original | Improved version |
|------|----------|------------------|
| **Sensor access** | Repeated `sensors.provideSensor(...)` calls throughout `handle()` | All sensors cached once in `init()` |
| **Speed values** | Magic numbers scattered in the code | Four named speed constants at the top of `init()` |
| **Throttle safety** | No check if throttle was acquired | Explicit `None` check with error message |
| **Code clarity** | `return 1` and repeated sensor lookups | `return True`, consistent `setKnownState()`, clear section comments |
| **Maintainability** | Hard to tune speeds or change sensor names | All configuration in one place |
| **Thread identification** | Anonymous thread | Named thread visible in JMRI Thread Monitor |
| **Direction settling** | Short / inconsistent waits | Consistent 800 ms direction-settling delay |

---

## Key features

- **Four configurable speeds**
  ```python
  self.speedStop   = 0.0
  self.speedSlow   = 0.4
  self.speedMedium = 0.5
  self.speedFast   = 0.8
  ```
- Cached sensors for both layout detection and signal aspects
- Clean forward / reverse cycle with intermediate speed changes
- Signal aspect control (red/green style sensors)
- Inertia wait after stopping at each end
- Easy to extend (add more sensors, turnouts, functions, etc.)

---

## Requirements

- JMRI (PanelPro or equivalent)
- A locomotive decoder that responds to the configured address
- The following sensors defined in the Sensor Table:
  - Layout: `S402`, `S403`, `S404`, `S407`
  - Signals: `SH1R`, `SH1G`, `SH6R`, `SH6G`

---

## How to use

1. Copy the script into a `.py` file (e.g. `LCCTest.py`).
2. Adjust the speed values and sensor names in `init()` if needed.
3. In JMRI: **Scripting → Run Script…** and select the file  
   **or** add it as a start-up action.
4. The script will loop indefinitely.  
   Stop it via the Thread Monitor or by terminating JMRI (the throttle is released on JMRI shutdown).

---

## Customisation tips

- Change locomotive address:
  ```python
  self.throttle = self.getThrottle(4, False)   # short address
  # self.throttle = self.getThrottle(1234, True)  # long address
  ```




