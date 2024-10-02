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
   pip install gradio fal-client
   ```

4. Set up your fal.ai API key:
   - Sign up for an account at [fal.ai](https://fal.ai)
   - Obtain your API key from the dashboard

### Setting Environment Variables

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

### Running the App

#### Windows

1. Open Command Prompt or PowerShell
2. Navigate to the project directory:
   ```
   cd path\to\FAL-AI-FLux
   ```
3. Activate the virtual environment (if you created one):
   ```
   venv\Scripts\activate
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
3. Activate the virtual environment (if you created one):
   ```
   source venv/bin/activate
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

- If you encounter a "ModuleNotFoundError", make sure you've activated the virtual environment (if used) and installed the required packages using pip.
- If you get an authentication error, check that you've correctly set the FAL_KEY environment variable with your fal.ai API key.
- For Windows users: 
  - If you're using PowerShell and the `set` command doesn't work, try using `$env:FAL_KEY = "your-api-key-here"` instead.
  - If you've used `setx` to set the environment variable, remember to restart your command prompt for the changes to take effect.

## Contributing

Feel free to fork this repository and submit pull requests with any improvements or additional features you'd like to add to the Gradio app or the project in general.

## License

This project is open-source and available under the MIT License.
