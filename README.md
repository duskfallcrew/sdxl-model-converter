# sdxl-model-converter

**⚠️ IMPORTANT: Google Colab Support Ended & AUP Warning ⚠️**

COLAB USERS: https://github.com/duskfallcrew/SDXL_COLAB_DIFFUSERS_CONVERT

Effective December 2024, this repository's Google Colab notebooks for SD 1.5 and SDXL model conversion are **no longer actively supported or maintained.** Due to persistent and unresolvable issues with Google Colab's Acceptable Use Policy (AUP), which disproportionately affects Stable Diffusion-related tools, we can no longer guarantee the functionality or stability of these notebooks on the Colab platform. For a comprehensive explanation of these issues, please refer to my article on Civitai: [https://civitai.com/articles/10080](https://civitai.com/articles/10080)

**Key Changes:** The Colab-based notebooks for converting both SD 1.5 and SDXL models to `diffusers` format have been **removed** from this repository. However, the **Jupyter (non-Colab) notebook and the classic Python script versions remain available** for local execution.

**Please Note:** While the non-Colab versions are still available for download and local use, we can no longer offer any support for issues specifically arising from usage on Google Colab, and this **includes all `diffusers` conversion tools.** Using the notebooks on Google Colab carries a significant risk of AUP violations.

**Reason for Discontinuation:** Extensive testing and analysis have demonstrated that even when using a basic `diffusers` approach (without `kohya-ss` or other training-related tools), Google Colab's AUP appears to flag any code processing SDXL models. This is due to the unique mathematical operations, data dictionaries, and data structures involved in handling SDXL models, as well as the tendency of the AUP to flag anything that appears to be related to Stable Diffusion. The system also appears to flag keywords related to "distributed compute" and "NSFW." These issues, combined with the arbitrary and unpredictable nature of AUP enforcement, make it impossible to provide a consistent user experience on Google Colab.

This situation is not due to any fault in the original code itself, but rather the result of Google Colab's system-level rules and restrictions that are beyond our control.

**Legal Disclaimer:** Therefore, we cannot be held responsible for any legal or other issues arising from the use of this code, especially when used in violation of the Google Colab Acceptable Use Policy. Users who choose to use these tools, whether on Colab or elsewhere, do so at their own risk, with the understanding that we offer no support for Colab-specific issues. **Please note that it is impossible for any tool on Google Colab to guarantee it will not violate the AUP, and using Colab for SD or AI model manipulation is likely to be problematic.**

---

This repository was originally created using a patched version of Linaqruf's code and Kohya-SS base scripts (for SDXL) and was intended for converting your SDXL base architecture checkpoints to Diffusers format. It was not designed for training or fine-tuning models, and as such, using it for that purpose may increase the likelihood of AUP violations.

As of June 24th, the Notebook was found to be in PRIVATE mode. This issue has been resolved. If you still cannot access the repository, please open an issue. We will not be accepting "EDITOR" requests on the base repository. If you are interested in contributing, please fork the project or download the relevant files directly. This policy is in place to ensure stability, prevent vandalism and address access issues. All content on this repository is available for download without needing to link to it.

June 29th Changelog:
The TPUv2 runtime was included on Colab. Beyond this, there is no further support for Google Colab and the resources for this repository have shifted to local execution. The code is designed to function in a variety of environments (including AWS), as it is not directly tied to your Google Drive.

| Link Name| Description | Link |
| --- | --- | --- |
| [Huggingface Backup](https://colab.research.google.com/github/kieranxsomer/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb) | backup checkpoints! | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/kieranxsomer/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb)
|Discord| E&D Discord |[Invite](https://discord.gg/5t2kYxt7An)
|CivitAi| Duskfallcrew @ Civitai |[Duskfallcrew](https://civitai.com/user/duskfallcrew/)
|Huggingface| E&D Huggingface |[Earth & Dusk](https://huggingface.co/EarthnDusk)
|Ko-Fi| Kofi Support |[![ko-fi](https://img.shields.io/badge/Support%20me%20on%20Ko--fi-F16061?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/Z8Z8L4EO)
|Github| Duskfallcrew Github |[Duskfallcrew](https://github.com/duskfallcrew)
| Youtube: | Duskfall Music|[Duskfall Music & More](https://www.youtube.com/channel/UCk7MGP7nrJz5awBSP75xmVw)
| Spotify: | E&D Royalty Free| [PLAYLIST](https://open.spotify.com/playlist/00R8x00YktB4u541imdSSf?si=57a8f0f0fe87434e)
|DA Group | AI Group| [DeviantArt Group](https://www.deviantart.com/diffusionai)
| Reddit | Earth & Dusk| [Subreddit](https://www.reddit.com/r/earthndusk/)

> ## Collaboration

We are not programmers by nature; we patch together code with the limited knowledge we possess. If you would like to help improve this project, please feel free to submit a pull request.

>## About

We are a system of over 300 alters, proudly navigating life with Dissociative Identity Disorder, ADHD, Autism, and CPTSD. We believe in the potential of AI to break down barriers and enhance aspects of mental health, even as it presents challenges. Our creative journey is an ongoing exploration of identity and expression, and we invite you to join us in this adventure.

>Future ideas:

- Looking to port PT to safetensors into the same notebook.
- Exploring methods to save conversion results to Google Drive to allow for more storage options.
- Considering porting to alternative platforms such as VastAi/Runpod.

>Cancelled Ideas that don't make sense for this product:
- Looking to incorporate inference testing into the notebook. - This is not required for this tool as it was intended for model conversion only, and not training or validation.
- Exploring ways to convert different VAE files. This proved to be ineffective.

>## Credits:

| Patched Origin | Description | Link |
| --- | --- | --- |
|Patched from| ARCHIVED |[SDXL - Linaqruf](https://colab.research.google.com/github/Linaqruf/sdxl-model-converter/blob/main/sdxl_model_converter.ipynb)
|***Linaqruf @ Github***: |https://github.com/Linaqruf
|Linaqruf Ko-Fi | [![](https://dcbadge.vercel.app/api/shield/850007095775723532?style=flat)](https://lookup.guru/850007095775723532) [![ko-fi](https://img.shields.io/badge/Support%20me%20on%20Ko--fi-F16061?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/linaqruf)
| Linaqruf Saweria |<a href="https://saweria.co/linaqruf"><img alt="Saweria" src="https://img.shields.io/badge/Saweria-7B3F00?style=flat&logo=ko-fi&logoColor=white"/></a>
