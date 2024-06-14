**INTRODUCTION**

Parking management has become a critical aspect of urban infrastructure, requiring innovative solutions to improve efficiency and convenience for motorists. This project presents a Parking Management System designed to inform drivers about the availability of parking spaces without the need to enter the parking lot. The system employs an OLED display, a laser module, a photoresistor, and a servo motor, all controlled by a Raspberry Pi Pico. By detecting the approach of vehicles and managing the entry and exit gates accordingly, the system ensures seamless access control and accurate tracking of available parking spaces.

**COMPONENTS**

The project utilizes several key components to achieve its functionality:
Raspberry Pi Pico: Acts as the central control unit, processing inputs from sensors and controlling outputs like the OLED display and servo motor.
OLED Display: Provides real-time information on the number of available parking spaces, ensuring that motorists are informed before entering the parking lot.
Laser Module: Emits a laser beam that, when interrupted, indicates the presence of a vehicle.
Photoresistor: Detects the laser beam; its state changes when the beam is blocked by an approaching vehicle, triggering the system to respond.
Servo Motor: Controls the opening and closing of the parking lot gate based on signals from the Raspberry Pi Pico.
Power Supply: Provides necessary power to all components, ensuring reliable operation.

**DISCUSSION**

The system operates by monitoring the state of the laser beam and the photoresistor at both the entrance and exit of the parking lot. Here’s how the process works in detail:

Vehicle Detection: 
When a vehicle approaches the entrance, it blocks the laser beam, causing the photoresistor to detect a change in light intensity. This triggers the photoresistor to send a low signal to the Raspberry Pi Pico.
Availability Check: 
Upon receiving the signal, the Raspberry Pi Pico checks the current count of available parking spaces.
If spaces are available, the Raspberry Pi Pico sends a signal to the servo motor to open the gate, allowing the vehicle to enter. Simultaneously, the available spaces count is decremented by one.
If no spaces are available, the gate remains closed, and the OLED display shows that the parking lot is full.
Exit Process: 
When a vehicle approaches the exit, it similarly blocks the laser beam at the exit point. The photoresistor detects this change and sends a signal to the Raspberry Pi Pico, which then opens the exit gate and increments the count of available spaces by one.
Display Updates: 
The OLED display continuously shows the number of available parking spaces. This information is updated in real-time based on the entry and exit of vehicles, providing accurate and timely information to motorists.

**CONCLUSION**

The Parking Management System successfully demonstrates an effective way to manage parking space availability and gate control using a combination of sensors and a microcontroller. By providing real-time information and automating the entry and exit processes, the system enhances the convenience for motorists and improves the efficiency of parking lot management. The integration of an OLED display, laser module, photoresistor, and servo motor, all orchestrated by the Raspberry Pi Pico, showcases the potential of embedded systems in solving everyday urban challenges.

**RECOMMENDATION**

For future improvements, several enhancements can be considered:

Enhanced Security: 
Implement additional security measures such as license plate recognition to prevent unauthorized access and improve safety.
Mobile App Integration: 
Develop a mobile application that provides real-time updates on parking space availability and allows users to reserve spots in advance.
Scalability: 
Adapt the system to manage larger parking lots by incorporating multiple entry and exit points and integrating additional sensors for more accurate vehicle detection.
Energy Efficiency: 
Optimize the power consumption of the system by incorporating energy-efficient components and implementing power-saving modes.
Weather Protection: 
Ensure that all outdoor components, particularly the laser module and photoresistor, are adequately protected against weather conditions to maintain reliable operation.
