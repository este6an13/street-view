import gradio as gr
from dotenv import load_dotenv
import os

# Load environment variables from a .env file if it exists
load_dotenv()
api_key = os.getenv("GOOGLE_MAPS_API_KEY")

# JavaScript code to initialize Google Maps and Street View using coordinates from Gradio inputs
js_code = f"""
function initializeMap(lat, lng) {{
    // Define the coordinates based on user input
    const coordinates = {{ lat: parseFloat(lat), lng: parseFloat(lng) }};

    // Remove existing map and panorama containers if they already exist
    const existingMap = document.getElementById('map');
    const existingPano = document.getElementById('pano');
    if (existingMap) existingMap.remove();
    if (existingPano) existingPano.remove();

    // Create new containers for map and panorama
    const mapContainer = document.createElement('div');
    mapContainer.id = 'map';
    mapContainer.style.height = '400px';
    mapContainer.style.width = '100%';

    const panoContainer = document.createElement('div');
    panoContainer.id = 'pano';
    panoContainer.style.height = '400px';
    panoContainer.style.width = '100%';

    // Insert containers into the Gradio app
    const gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.appendChild(mapContainer);
    gradioContainer.appendChild(panoContainer);

    const script = document.createElement('script');
    script.src = "https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initialize";
    script.async = true;
    document.head.appendChild(script);

    // Initialize the map and panorama
    window.initialize = function() {{
        const map = new google.maps.Map(mapContainer, {{
            center: coordinates,
            zoom: 14,
        }});

        const panorama = new google.maps.StreetViewPanorama(panoContainer, {{
            position: coordinates,
        }});

        map.setStreetView(panorama);
    }};

    return 'Map and panorama initialized at provided coordinates';
}}
"""


# Gradio function to display a message
def load_message():
    return "Enter latitude and longitude values and press 'Initialize Map' to view the location."


# Set up Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Interactive Google Map with Street View Panorama")
    lat_input = gr.Textbox(
        label="Latitude", placeholder="Enter latitude (e.g., 42.345573)"
    )
    lng_input = gr.Textbox(
        label="Longitude", placeholder="Enter longitude (e.g., -71.098326)"
    )
    message = gr.Textbox(value=load_message(), label="Instructions", interactive=False)
    button = gr.Button("Initialize Map").click(
        None,
        inputs=[lat_input, lng_input],
        outputs=message,
        js=js_code,
    )

if __name__ == "__main__":
    demo.launch()
