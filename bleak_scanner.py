import asyncio
from bleak import BleakScanner, BleakClient

# Replace with your device's MAC address and UUIDs
# DEVICE_MAC = "f8:55:48:1b:a0:7c"
DEVICE_MAC = "F8:55:48:1B:A0:7C"
# SERVICE_UUID = "43101FBA-0B09-6E4F-E832-11A1801BD3F4"
SERVICE_UUID = "0000D0FF-3C17-D293-8E48-14FE2E4DA212"
# CHARACTERISTIC_UUID = "F000FFD1-0451-4000-B000-000000000000"
CHARACTERISTIC_UUID = "FFD1"

async def main():
    # Scan for devices
    devices = await BleakScanner.discover()
    for device in devices:
        print(device)

    # Connect to device
    async with BleakClient(DEVICE_MAC) as client:
        print(f"Connected: {client.is_connected}")

        # Discover services and characteristics
        services = await client.get_services()
        for service in services:
            print(service)

        # Write to a characteristic
        await client.write_gatt_char(CHARACTERISTIC_UUID, b'\x01\x02')

        # Register for notifications
        def notification_handler(sender, data):
            print(f"Notification from {sender}: {data}")

        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        # Keep the program running to receive notifications
        await asyncio.sleep(30)

        # Stop notifications when done
        await client.stop_notify(CHARACTERISTIC_UUID)

asyncio.run(main())