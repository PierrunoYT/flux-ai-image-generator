# FAL AI Flux Image Generator

This project utilizes the FLUX.1 [dev] model from fal.ai to generate images based on text prompts.

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/PierrunoYT/flux-ai-image-generator.git
   cd flux-ai-image-generator
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
   pip install fal-client
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

The main script for image generation is `flux_image_generator.py`. You can run it from the command line with various parameters to customize the image generation process.

Example usage:

```
python flux_image_generator.py --prompt "A serene landscape with mountains and a lake" --size 1024x1024 --num_images 2
```

Available parameters:
- `--prompt`: The text description of the image you want to generate (required)
- `--size`: Image size in the format widthxheight (default: 1024x1024)
- `--num_inference_steps`: Number of denoising steps (default: 50)
- `--guidance_scale`: How closely the model should follow the prompt (default: 7.5)
- `--num_images`: Number of images to generate (default: 1)
- `--enable_safety_checker`: Whether to enable the safety filter (default: True)

## Troubleshooting

- If you encounter a "ModuleNotFoundError", make sure you've activated the virtual environment (if used) and installed the required packages using pip.
- If you get an authentication error, check that you've correctly set the FAL_KEY environment variable with your fal.ai API key.
- For Windows users: 
  - If you're using PowerShell and the `set` command doesn't work, try using `$env:FAL_KEY = "your-api-key-here"` instead.
  - If you've used `setx` to set the environment variable, remember to restart your command prompt for the changes to take effect.

## Contributing

Feel free to fork this repository and submit pull requests with any improvements or additional features you'd like to add to the image generator or the project in general.

## License

This project is open-source and available under the [MIT License](LICENSE).
