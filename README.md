# PyAI
 
# Installation

Install [Rye](https://rye-up.com/), then navigate to the directory where this is installed. Run `rye sync ; rye run PyAI -h` to sync packages and display options.

Currently exploring:

Using chatgpt to summarize its own chat log to reduce incoherency
Use marqo to narrow the context provided instead of using the entire chat log.

# Installation of Local Model/DB

Need a huggingface API key to download the model. The default model is google/gemma-2b-it, so you will need to accept the t&c of that model as well.

You will need a docker db running [Marqo](https://github.com/marqo-ai/marqo)