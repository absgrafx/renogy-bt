# ABSGRAFX Renogy Device Discovery 
## Goal
- Remotely connect to all 3 (or more) Renogy devices via BLE/BT RS485 interfaces 
- Collect data on a regular basis 
- Send data to a central server for processing (ie: Grafana)

## Renogy Devices (in order of importance and liklihood of interrogation)

- **Main Smart Shunt 300** - connected via BLE 
    - Local Name: RTMShunt30017000621
    - Peripheral Id: 696A6318-82C6-B188-E78C-071F1182CE5A
    - Manufacturer Data: 4ce1745195ae001e0001 (is this mac id plus? 4c:e1:74:51:95:ae 001e0001)
    - Service UUID (shows the most promise for data extraction): 0000D0FF-3C17-D293-8E48-14FE2E4DA212

- **Rover 60 MPPT via BT-2** - Solar Charge Controller connected via BT-2 
    - Local Name: BT-TH-481BA07C    
    - Peripheral Id: 43101FBA-0B09-6E4F-E832-11A1801BD3F4
    - Manufacturer Data: f855481ba07c (is this mac ID? f8:55:48:1b:a0:7c)
    - Service UUID (most promise): 0000D0FF-3C17-D293-8E48-14FE2E4DA212

- **Inverter Smart Shunt 300** - connected via BLE 
    - not online yet, but expect similar to Main Smart Shunt 300

- **3KW Inverter/Converter via BT-2** - Connected via BT-2 BLE (experimental...unknown if it will work)
    - Local Name: BT-TH-481A66B7    
    - Peripheral Id: 7047E314-4EA4-BE0C-5A55-E0D3D9527C85
    - Manufacturer Data: f855481a66b7 (is this mac ID? f8:55:48:1a:66:b7)

- **CoreOne** - WiFi Hub that will interface with https://one.renogy.com and remote, mobile apps 
    - Local Name: RNGONECore44001004
    - Peripheral Id: 2940ECAC-4DB5-2A41-4740-6DB04C2F6DCE
    - Manufacturer Data: 4ce17446ce2e (is this mac ID? 4c:e1:74:46:ce:2e)
    - Service UUID (most promise): 0000D0FF-3C17-D293-8E48-14FE2E4DA212

## Challenges 
1. interrogate all BT devices and determine how to extract/subscribe to data 
2. decompose data stream to meaningful sections 
3. convert meaningful sections to proper units/formatting (hex to ascii for temp for example)
4. store data in proper formatted data structure for measure and display 
5. measure and display 

