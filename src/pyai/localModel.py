from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv, find_dotenv

def installAndRunModel(model_name: str):
    '''
    If the model is not installed, this will attempt to retrieve a model with the model_name provided
    from huggingface. Once/If the model is installed, it will load it and query it to test that it works.
    '''
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    input_text = "Write me a poem about Machine Learning."
    input_ids = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(**input_ids, max_new_tokens=600)
    print(tokenizer.decode(outputs[0]))
    print("successfully loaded '" + model_name + "'")
    return (tokenizer, model)

def inputText(tokenizer, model, db_context=None, verbose=False) -> int:
    '''
    Takes the provided tokenizer and model and repeatedly takes user input to query the model.
    '''
    running = True
    max_new_tokens=9999
    history = []
    while running:
        print("\nAsk your model a question: (Type quit or q to exit or type // for additional options.)")
        input_text = input().strip()
        if(input_text.lower() == "quit" or input_text.lower() == "q"):
            break
        #editing variables.
        if(input_text == '//'):
            awaiting = True
            while awaiting:
                print("\nType quit or q to exit")
                print("type clear or c to clear chat history")
                print("type display or d to show full chat history")
                print("type [variable]:[value] to adjust a model variable.")
                print("type help or h to see editable model variables")
                print("if a value is successfully edited, you should see [valuename] changed to [value]")
                input_text_inner = input().strip()
                if(input_text_inner.lower() == "quit" or input_text_inner.lower() == "q"):
                     awaiting = False
                     break
                elif(input_text_inner.lower() == "display" or input_text_inner.lower() == "d"):
                    for value in history:
                        print(value)
                    continue
                elif(input_text_inner.lower() == "help" or input_text_inner.lower() == "h"):
                    print("max_new_tokens:[int]")
                    continue
                elif(input_text_inner.lower() == "clear" or input_text_inner.lower() == "c"):
                    history = []
                    print('chat history cleared')
                    continue
                else:
                    #this should probably be a function.
                    input_list = input_text_inner.lower().split(':')
                    if (input_list[0] == 'max_new_tokens'):
                        try:
                            value = int(input_list[1])
                        except ValueError:
                            print(ValueError)
                            print("failed to update max_new_tokens")
                        else:
                            max_new_tokens = value
                            print("max_new_tokens changed to " + input_list[1])
            continue
                            



        #question block
        history.append({'role':'user', 'content': input_text})
        if(verbose):
            print(history)
        input_text = tokenizer.apply_chat_template(conversation=history, tokenize=False, return_tensors='pt')
        if(verbose):
            print('\n\nconversation templated\n\n',input_text,'\n\n')
        input_ids = tokenizer(input_text, return_tensors="pt")
        #print('inputs:',input_text)
        #print('inputs tokenized?', tokenizer(input_text, return_tensors="pt"))
        #input_ids = tokenizer(input_text, return_tensors="pt")

        outputs = model.generate(**input_ids,max_new_tokens=max_new_tokens)
        #print('outputs are:',outputs)
        for token in outputs:
            value = tokenizer.decode(token)
            if(verbose):
                print('\n\nraw value\n',value,'\n\n')
            statements = value.split("<end_of_turn>")
            #for statement in statements:
            #    print(statement)
            print(statements[-1].replace('<eos>','').replace('<bos>',''))
            history.append({'role':'assistant','content': statements[-1].replace('<eos>','').replace('<bos>','')})
        
    print("Exiting...")
    return 0