# FAL AI Flux Dev Image Generator

This project is a Gradio app that utilizes the FLUX.1 [dev] model from fal.ai to generate images based on text prompts. It provides an interactive web interface for easy image generation.

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/PierrunoYT/fal-flux-dev-image-generator.git
   cd fal-flux-dev-image-generator
   ```

2. (Recommended) Create and activate a virtual environment:

   #### Windows
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   #### macOS and Linux
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install fal-client gradio
   ```

4. Set up your fal.ai API key:
   - Sign up for an account at [fal.ai](https://fal.ai)
   - Obtain your API key from the dashboard

## Setting Environment Variables

#### Windows

You can use either `set` or `setx` to set environment variables:

- Using `set` (temporary, for current session only):
  ```
  set FAL_KEY=your-api-key-here
  ```

- Using `setx` (permanent, requires restarting the command prompt):
  ```
  setx FAL_KEY "your-api-key-here"
  ```
  After using `setx`, close and reopen your command prompt for the changes to take effect.

#### macOS and Linux

```
export FAL_KEY=your-api-key-here
```

## Usage

The main script for the Gradio app is `flux_image_generator.py`. You can run it from the command line to start the web interface.

To launch the Gradio app:

```
python flux_image_generator.py
```

Once the app is running, you'll see a URL in the console. Open this URL in your web browser to access the Gradio interface.

In the Gradio interface, you can:

1. Enter a text prompt describing the image you want to generate.
2. Adjust various parameters:
   - Image Size: Choose from predefined aspect ratios
   - Number of Inference Steps: Higher values may produce better quality but take longer
   - Guidance Scale: How closely the model should follow the prompt
   - Number of Images: Generate up to 4 images at once
   - Enable Safety Checker: Option to filter out potentially unsafe content
3. Click "Submit" to generate the image(s).

The generated images will be displayed in the interface, and you can download them directly from there.

## Troubleshooting

- If you encounter a "ModuleNotFoundError", make sure you've activated the virtual environment (if used) and installed the required packages using pip.
- If you get an authentication error, check that you've correctly set the FAL_KEY environment variable with your fal.ai API key.
- For Windows users: 
  - If you're using PowerShell and the `set` command doesn't work, try using `$env:FAL_KEY = "your-api-key-here"` instead.
  - If you've used `setx` to set the environment variable, remember to restart your command prompt for the changes to take effect.
- If the Gradio interface doesn't open automatically, try manually copying and pasting the URL from the console into your web browser.

## Contributing

Feel free to fork this repository and submit pull requests with any improvements or additional features you'd like to add to the Gradio app or the project in general.

## License

This project is open-source and available under the [MIT License](LICENSE).
