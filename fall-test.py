import fal

result = fal.apps.run("110602490-lora", arguments={
    "model_name": "stabilityai/stable-diffusion-xl-base-1.0",
    "prompt": "a photo of girl who writes python code",
})
print(result["images"][0]["url"])