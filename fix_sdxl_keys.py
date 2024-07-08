import os
import requests
import importlib.util

# Note that this is meant to work IN TANDEM with the colab notebook, you'll need the installation of kohya-ss FIRST. in tandem meaning this is just the PY file that works seperate to the colab, and this works just as wel las the other.

def check_and_download_script(script_name, script_url):
    if not os.path.exists(script_name):
        response = requests.get(script_url)
        with open(script_name, 'wb') as f:
            f.write(response.content)

def fix_sdxl_model_keys(model_data):
    text_encoder1, text_encoder2, vae, unet = model_data

    # Fix keys in text_encoder1
    fixed_text_encoder1 = {}
    for k, v in text_encoder1.state_dict().items():
        new_k = k.replace('first_stage_model.', '')
        fixed_text_encoder1[new_k] = v

    # Fix keys in text_encoder2
    fixed_text_encoder2 = {}
    for k, v in text_encoder2.state_dict().items():
        new_k = k.replace('first_stage_model.', '')
        fixed_text_encoder2[new_k] = v

    # Fix keys in vae
    fixed_vae = {}
    for k, v in vae.state_dict().items():
        new_k = k.replace('first_stage_model.', '')
        fixed_vae[new_k] = v

    # Fix keys in unet
    fixed_unet = {}
    for k, v in unet.state_dict().items():
        new_k = k.replace('first_stage_model.', '')
        fixed_unet[new_k] = v

    return fixed_text_encoder1, fixed_text_encoder2, fixed_vae, fixed_unet

def main():
    script_name = "convert_sdxl_to_diffusers.py"
    script_url = "https://raw.githubusercontent.com/Linaqruf/sdxl-model-converter/main/convert_sdxl_to_diffusers.py"
    check_and_download_script(script_name, script_url)

    # Load the downloaded script
    spec = importlib.util.spec_from_file_location("convert_sdxl_to_diffusers", script_name)
    convert_sdxl_to_diffusers = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(convert_sdxl_to_diffusers)

    # Modify the convert_model function to use fix_sdxl_model_keys
    def convert_model(args):
        load_dtype = torch.float16 if args.fp16 else None
        save_dtype = get_save_dtype(args)

        is_load_checkpoint = determine_load_checkpoint(args.model_to_load)
        is_save_checkpoint = not is_load_checkpoint  # reverse of load model

        loaded_model_data = load_sdxl_model(args, is_load_checkpoint, load_dtype)
        fixed_model_data = fix_sdxl_model_keys(loaded_model_data)
        convert_and_save_sdxl_model(args, is_save_checkpoint, fixed_model_data, save_dtype)

    # Call the modified convert_model function
    convert_sdxl_to_diffusers.convert_model(args)  # Replace args with the required arguments

if __name__ == "__main__":
    main()
