import gradio as gr
import fal_client
import os
import tempfile

# Ensure you have set the FAL_KEY environment variable
if "FAL_KEY" not in os.environ:
    raise ValueError("Please set the FAL_KEY environment variable")

def generate_image(prompt, image_size, num_inference_steps, guidance_scale, num_images, enable_safety_checker, seed=None, sync_mode=False):
    """
    Generate images using the FLUX.1 [dev] model from fal.ai.

    Args:
        prompt (str): The prompt to generate an image from.
        image_size (str): The size of the generated image.
        num_inference_steps (int): The number of inference steps to perform.
        guidance_scale (float): The CFG (Classifier Free Guidance) scale.
        num_images (int): The number of images to generate.
        enable_safety_checker (bool): If set to true, the safety checker will be enabled.
        seed (int, optional): The seed for image generation. If None, a random seed will be used.
        sync_mode (bool, optional): If set to true, the function will wait for the image to be generated and uploaded before returning.

    Returns:
        tuple: A tuple of up to 4 image URLs or empty strings.
    """
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
        
        # Pad the list with empty strings if less than 4 images are generated
        while len(image_urls) < 4:
            image_urls.append("")
        
        return tuple(image_urls[:4])  # Return exactly 4 items (URLs or empty strings) as a tuple
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return ("", "", "", "")  # Return 4 empty strings in case of an error

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
        # Create a temporary directory that we know we have permission to access
        with tempfile.TemporaryDirectory() as temp_dir:
            print(f"Using temporary directory: {temp_dir}")
            iface.launch(share=True, temp_dir=temp_dir)
    except PermissionError as pe:
        print(f"PermissionError: {pe}")
        print("Please ensure you have the necessary permissions to run this script.")
        print("You may need to run it with administrator privileges.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")