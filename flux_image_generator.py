import gradio as gr
import fal_client
import os
import tempfile
import shutil
import uuid
import requests
import base64
from io import BytesIO

# Print initial working directory
print(f"Initial working directory: {os.getcwd()}")

# Ensure you have set the FAL_KEY environment variable
if "FAL_KEY" not in os.environ:
    raise ValueError("Please set the FAL_KEY environment variable")

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    return None

def base64_to_temp_file(base64_string):
    if not base64_string:
        return None
    try:
        image_data = base64.b64decode(base64_string.split(',')[1])
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        temp_file.write(image_data)
        temp_file.close()
        return temp_file.name
    except Exception as e:
        print(f"Error creating temp file: {str(e)}")
        return None

def generate_image(prompt, image_size, num_inference_steps, guidance_scale, num_images, enable_safety_checker, seed=None, sync_mode=False):
    try:
        handler = fal_client.submit(
            "fal-ai/flux/dev",
            arguments={
                "prompt": prompt,
                "image_size": image_size,
                "num_inference_steps": num_inference_steps,
                "guidance_scale": guidance_scale,
                "num_images": num_images,
                "enable_safety_checker": enable_safety_checker,
                "seed": seed,
                "sync_mode": sync_mode
            },
        )
        
        result = handler.get()
        image_urls = [image["url"] for image in result["images"]]
        
        # Download images and convert to base64
        base64_images = []
        for url in image_urls:
            image_data = download_image(url)
            if image_data:
                base64_image = base64.b64encode(image_data.getvalue()).decode('utf-8')
                base64_images.append(f"data:image/png;base64,{base64_image}")
            else:
                base64_images.append("")
        
        # Convert base64 images to temporary files
        temp_files = [base64_to_temp_file(img) for img in base64_images]
        
        # Pad the list with None if less than 4 images are generated
        while len(temp_files) < 4:
            temp_files.append(None)
        
        return tuple(temp_files[:4])  # Return exactly 4 items (file paths or None) as a tuple
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return (None, None, None, None)  # Return 4 None values in case of an error

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Dropdown(["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"], label="Image Size", value="landscape_4_3"),
        gr.Slider(1, 50, value=28, step=1, label="Number of Inference Steps"),
        gr.Slider(1, 20, value=3.5, step=0.1, label="Guidance Scale"),
        gr.Slider(1, 4, value=1, step=1, label="Number of Images"),
        gr.Checkbox(label="Enable Safety Checker", value=True),
        gr.Number(label="Seed (optional)", precision=0),
        gr.Checkbox(label="Sync Mode", value=False)
    ],
    outputs=[gr.Image(type="filepath") for _ in range(4)],
    title="FLUX.1 [dev] Image Generator",
    description="Generate images using the FLUX.1 [dev] model from fal.ai"
)

if __name__ == "__main__":
    try:
        # Launch the interface with debugging enabled
        iface.launch(share=True, debug=True)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Clean up temporary files
        temp_dir = tempfile.gettempdir()
        for filename in os.listdir(temp_dir):
            if filename.endswith('.png'):
                file_path = os.path.join(temp_dir, filename)
                try:
                    os.unlink(file_path)
                except Exception as e:
                    print(f"Error deleting temporary file {file_path}: {str(e)}")
