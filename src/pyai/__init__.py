import os
import argparse
from dotenv import load_dotenv, find_dotenv
from huggingface_hub import login
from .localModel import installAndRunModel, inputText

def query_user_yesno(question: str) -> bool:
    print(question)
    whileinput = True
    response = False
    while(whileinput):
        varinput = input()
        match varinput:
            case 'y' | 'Y' | 'yes' | 'Yes':
                response = True
                whileinput = False
            case 'n' | 'N' | 'no' | 'No':
                response = False
                whileinput = False
            case _:
                print("Please provide a yes or no (y/n) response.")
    return response

def query_user_dynamic(question: str) -> str:
    print(question)
    return input()
        
def main() -> int:
    verbose = False

    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--init", action="store_true", help="run the initialization process to configure what model/API PyAI is using.")
    parser.add_argument("-g","--gpt", action="store_true", help="uses your openai api key to access their text generation generation models.")
    parser.add_argument("-l","--local", action="store_true", help="uses your local hardware to run a text generation model.")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity.")
    args = parser.parse_args()
    load_dotenv(find_dotenv())
    if(args.verbose):
        verbose = True
    if(args.init):
        '''
            This should establish a new .env file, if there is not one already existing.
            If one already exists, ask the user if they want to overwrite it then replace the values.
        '''
        openai = query_user_yesno('Do you want to use the openai chatgpt API? y/n')
        pass
    elif(args.gpt):
        '''
            This should use the gptConnection file to connect to the OpenAI API and use their text generation model.
        '''
        if os.getenv("OPENAI_API_KEY") is None:
            raise AttributeError("OpenAI API key not found")
        print("OpenAI API key found...")
        print("Hello from PyAI!")
    elif(args.local):
        '''
            This should use the configured text generation model.
        '''
        if os.getenv("MODEL_NAME") is None:
            print("No Model Name found.")
            if os.getenv("HF_TOKEN") is not None:
                print("HF_Token found - Using 'google/gemma-2b-it'")
                tokenizer, model = installAndRunModel("google/gemma-2b-it")
                inputText(tokenizer=tokenizer, model=model, verbose=verbose)
            else:
                print("using ''")
        else:
            installAndRunModel(os.getenv("Model Name"))

            
    return 0