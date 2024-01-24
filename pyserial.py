# # import serial

# # def parse_gpgll(gpgll_data):
# #     # Split the $GPGLL sentence into fields
# #     fields = gpgll_data.split(',')

# #     # Check if the sentence is valid
# #     if len(fields) >= 6 and fields[0] == '$GPGLL':
# #         latitude = fields[1]
# #         longitude = fields[3]

# #         return f"Latitude: {latitude}, Longitude: {longitude}"

# #     return None

# # def main():
# #     # Open a serial port (replace 'COM3' with the appropriate port on your system)
# #     ser = serial.Serial('/dev/ttyACM0', 9600)

# #     try:
# #         while True:
# #             # Read a line from the serial port
# #             line = ser.readline().decode('utf-8').strip()

# #             # Check if the line starts with '$GPGLL'
# #             if line.startswith('$GPGLL'):
# #                 # Parse and display the $GPGLL values
# #                 result = parse_gpgll(line)
# #                 if result:
# #                     print(result)

# #     except KeyboardInterrupt:
# #         # Close the serial port when the program is interrupted
# #         ser.close()

# # if __name__ == "__main__":
# #     main()
# import serial

# def parse_gpgll(gpgll_data):
#     # Print the raw NMEA sentence for debugging
#     print(f"Raw NMEA Sentence: {gpgll_data}")

#     # Split the $GPGLL sentence into fields
#     fields = gpgll_data.split(',')

#     # Check if the sentence is valid
#     if len(fields) >= 6 and fields[0] == '$GPGLL':
#         latitude = fields[1]
#         longitude = fields[3]

#         return f"Latitude: {latitude}, Longitude: {longitude}"

#     return None

# def main():
#     # Open a serial port (replace 'COM3' with the appropriate port on your system)
#     ser = serial.Serial('/dev/ttyACM0', 9600)

#     try:
#         while True:
#             # Read a line from the serial port
#             line = ser.readline().decode('utf-8', errors='replace').strip()

#             # Check if the line starts with '$GPGLL'
#             if line.startswith('$GPGLL'):
#                 # Parse and display the $GPGLL values
#                 result = parse_gpgll(line)
#                 if result:
#                     print(result)

#     except KeyboardInterrupt:
#         # Close the serial port when the program is interrupted
#         ser.close()

# if __name__ == "__main__":
#     main()
# import serial

# def parse_gpgll(gpgll_data):

#     # Split the $GPGLL sentence into fields
#     fields = gpgll_data.split(',')

#     # Check if the sentence is valid
#     if len(fields) >= 6 and fields[0] == '$GPGLL' and fields[1] and fields[3]:
#         # Divide latitude and longitude by 100
#         latitude = float(fields[1]) / 100
#         longitude = float(fields[3]) / 100

#         return f"Latitude: {latitude}, Longitude: {longitude}"

#     return None

# def main():
#     # Open a serial port (replace 'COM3' with the appropriate port on your system)
#     ser = serial.Serial('/dev/ttyACM0', 9600)

#     try:
#         while True:
#             # Read a line from the serial port
#             line = ser.readline().decode('utf-8', errors='replace').strip()

#             # Check if the line starts with '$GPGLL'
#             if line.startswith('$GPGLL'):
#                 # Parse and display the $GPGLL values
#                 result = parse_gpgll(line)
#                 if result:
#                     print(result)

#     except KeyboardInterrupt:
#         # Close the serial port when the program is interrupted
#         ser.close()

# if __name__ == "__main__":
#     main()

import serial
import rospy
from std_msgs.msg import Float64

def parse_gpgll(gpgll_data):
    # Print the raw NMEA sentence for debugging
    print(f"Raw NMEA Sentence: {gpgll_data}")

    # Split the $GPGLL sentence into fields
    fields = gpgll_data.split(',')

    # Check if the sentence is valid
    if len(fields) >= 6 and fields[0] == '$GPGLL' and fields[1] and fields[3]:
        # Divide latitude and longitude by 100
        latitude = float(fields[1]) / 100
        longitude = float(fields[3]) / 100

        return latitude, longitude

    return None

def main():
    # Initialize ROS node
    rospy.init_node('gps_publisher')

    # Create ROS publishers for latitude and longitude
    latitude_pub = rospy.Publisher('latitude', Float64, queue_size=10)
    longitude_pub = rospy.Publisher('longitude', Float64, queue_size=10)

    # Open a serial port (replace 'COM3' with the appropriate port on your system)
    ser = serial.Serial('/dev/ttyACM0', 9600)

    try:
        while not rospy.is_shutdown():
            # Read a line from the serial port
            line = ser.readline().decode('utf-8', errors='replace').strip()

            # Check if the line starts with '$GPGLL'
            if line.startswith('$GPGLL'):
                # Parse the $GPGLL values
                result = parse_gpgll(line)
                if result:
                    # Publish latitude and longitude on respective topics
                    latitude_pub.publish(result[0])
                    longitude_pub.publish(result[1])

    except KeyboardInterrupt:
        # Close the serial port when the program is interrupted
        ser.close()

if __name__ == "__main__":
    main()
