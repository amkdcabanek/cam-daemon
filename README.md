# Raspberry Pi Camera Stream

This project allows you to stream live video from the Raspberry Pi Camera Module V3 over Wi-Fi. The video feed can be accessed from any web browser on the same network by entering the Raspberry Pi's IP address.

## Project Structure

```
raspberry-pi-camera-stream
├── cam_daemon.py         # Main logic for streaming video
├── templates
│   └── index.html       # HTML template for video display
├── static
│   └── style.css        # CSS styles for the web interface
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Requirements

Before running the project, ensure you have the following installed:

- Python 3
- Flask
- OpenCV

You can install the required Python packages using the following command:

```
pip install -r requirements.txt
```

## Setup Instructions

1. **Connect the Camera Module**: Ensure that the Camera Module V3 is properly connected to the Raspberry Pi.

2. **Clone the Repository**: Clone this repository to your Raspberry Pi.

3. **Install Dependencies**: Navigate to the project directory and install the required packages using the command mentioned above.

4. **Run the Stream**: Execute the following command to start the video stream:

   ```
   python cam_daemon.py
   ```

5. **Access the Stream**: Open a web browser on another device connected to the same network and enter the Raspberry Pi's IP address followed by `:8000`. For example:

   ```
   http://192.168.1.100:8000
   ```

## Customization

- You can modify the video resolution and frame rate in the `cam_daemon.py` file if needed.
- The overlay text "wideo-feed" can also be changed by editing the relevant section in the same file.

## Troubleshooting

- Ensure that the camera is enabled in the Raspberry Pi configuration settings.
- Check the network connection if you cannot access the stream from another device.
- Review the console output for any error messages when running the stream.

## License

This project is open-source and available under the MIT License.
