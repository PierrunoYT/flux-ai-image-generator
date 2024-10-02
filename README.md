# FAL AI Flux

This project is dedicated to exploring and implementing AI flux concepts using the FLUX.1 [dev] model from fal.ai.

## FLUX.1 [dev] Image Generator

This project includes a Gradio app that allows you to generate images using the FLUX.1 [dev] model from fal.ai.

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/FAL-AI-FLux.git
   cd FAL-AI-FLux
   ```

2. Install the required packages:
   ```
   pip install gradio fal-client
   ```

3. Set up your fal.ai API key:
   - Sign up for an account at [fal.ai](https://fal.ai)
   - Obtain your API key from the dashboard
   - Set the API key as an environment variable:
     ```
     export FAL_KEY="your-api-key-here"
     ```

### Running the App

To run the Gradio app, execute the following command in your terminal:

```
python flux_gradio_app.py
```

The app will start, and you'll see a URL where you can access the interface in your web browser.

### Using the App

1. Enter a text prompt describing the image you want to generate.
2. Adjust the parameters as needed:
   - Image Size: Choose from predefined aspect ratios
   - Number of Inference Steps: Higher values may produce better quality but take longer
   - Guidance Scale: How closely the model should follow the prompt
   - Number of Images: Generate up to 4 images at once
   - Enable Safety Checker: Option to filter out potentially unsafe content
3. Click "Submit" to generate the image(s).

## Contributing

Feel free to fork this repository and submit pull requests with any improvements or additional features you'd like to add to the Gradio app or the project in general.

## License

This project is open-source and available under the MIT License.
