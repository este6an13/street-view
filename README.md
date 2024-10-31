# Interactive Google Map with Street View

This Gradio app displays a Google Map and Street View based on user-provided latitude and longitude.

## Requirements

- Gradio
- Python-dotenv

## Installation

1. Clone the repository.

2. Install the required packages:

   ```bash
   pip install gradio python-dotenv
   ```

3. Obtain a Google Maps API key from the [Google Cloud Console](https://developers.google.com/maps/documentation/javascript/get-api-key#create-api-keys).

4. Create a `.env` file in the project directory and add your API key:

   ```plaintext
   GOOGLE_MAPS_API_KEY=your_api_key_here
   ```

## Running the Project

Run the application:

```bash
gradio app.py
```

Open your browser at `http://127.0.0.1:7860/` to access the app.

## Usage

1. Enter a latitude and longitude.
2. Click **Initialize Map** to display the location on the map and in Street View.
