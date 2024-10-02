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

### Running the App

#### Windows

1. Open Command Prompt or PowerShell
2. Navigate to the project directory:
   ```
   cd path\to\FAL-AI-FLux
   ```
3. Set the API key as an environment variable:
   ```
   set FAL_KEY=your-api-key-here
   ```
4. Run the Gradio app:
   ```
   python flux_gradio_app.py
   ```

#### macOS and Linux

1. Open Terminal
2. Navigate to the project directory:
   ```
   cd path/to/FAL-AI-FLux
   ```
3. Set the API key as an environment variable:
   ```
   export FAL_KEY=your-api-key-here
   ```
4. Run the Gradio app:
   ```
   python3 flux_gradio_app.py
   ```

After running the app, you'll see a URL where you can access the interface in your web browser.

### Using the App

1. Enter a text prompt describing the image you want to generate.
2. Adjust the parameters as needed:
   - Image Size: Choose from predefined aspect ratios
   - Number of Inference Steps: Higher values may produce better quality but take longer
   - Guidance Scale: How closely the model should follow the prompt
   - Number of Images: Generate up to 4 images at once
   - Enable Safety Checker: Option to filter out potentially unsafe content
3. Click "Submit" to generate the image(s).

## Troubleshooting

- If you encounter a "ModuleNotFoundError", make sure you've installed the required packages using pip.
- If you get an authentication error, check that you've correctly set the FAL_KEY environment variable with your fal.ai API key.
- For Windows users: If you're using PowerShell and the `set` command doesn't work, try using `$env:FAL_KEY = "your-api-key-here"` instead.

## Contributing

Feel free to fork this repository and submit pull requests with any improvements or additional features you'd like to add to the Gradio app or the project in general.

## License

This project is open-source and available under the MIT License.
