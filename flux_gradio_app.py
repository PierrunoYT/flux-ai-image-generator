import gradio as gr
import fal_client
import os

# Ensure you have set the FAL_KEY environment variable
if "FAL_KEY" not in os.environ:
    raise ValueError("Please set the FAL_KEY environment variable")

def generate_image(prompt, image_size, num_inference_steps, guidance_scale, num_images, enable_safety_checker):
    try:
        handler = fal_client.submit(
            "fal-ai/flux/dev",
            arguments={
                "prompt": prompt,
                "image_size": image_size,
                "num_inference_steps": num_inference_steps,
                "guidance_scale": guidance_scale,
                "num_images": num_images,
                "enable_safety_checker": enable_safety_checker
            },
        )
        
        result = handler.get()
        return [result["images"][i]["url"] for i in range(num_images)]
    except Exception as e:
        return str(e)

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Dropdown(["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"], label="Image Size", value="landscape_4_3"),
        gr.Slider(1, 50, value=28, step=1, label="Number of Inference Steps"),
        gr.Slider(1, 20, value=3.5, step=0.1, label="Guidance Scale"),
        gr.Slider(1, 4, value=1, step=1, label="Number of Images"),
        gr.Checkbox(label="Enable Safety Checker", value=True)
    ],
    outputs=[gr.Image(type="filepath") for _ in range(4)],  # Support up to 4 images
    title="FLUX.1 [dev] Image Generator",
    description="Generate images using the FLUX.1 [dev] model from fal.ai"
)

if __name__ == "__main__":
    iface.launch()