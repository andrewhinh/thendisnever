def isnever():
    from transformers import (
        AutoTokenizer, # To tokenize the prompt
        AutoModelForCausalLM, # To generate the response
        TextStreamer # To stream the response
    ) # To import the necessary classes

    # Setup the model
    model_name = "Fredithefish/ScarletPajama-3B-HF" # Or whatever model you want
    model = AutoModelForCausalLM.from_pretrained(model_name) # To load the model
    tokenizer = AutoTokenizer.from_pretrained(model_name) # To load the tokenizer
    streamer = TextStreamer(tokenizer) # To create the streamer

    # Setup the conversation loop
    prompt = "THE END IS NEVER THE END IS NEVER " # Or whatever you want
    max_length = model.config.max_length # To get the max length of the model
    max_memory = max_length * 0.5 # Or whatever you want (sets the # of most recent tokens in prompt to keep for the model's memory)
    while True: # To loop the conversation
        inputs = tokenizer(
            [prompt], # wrapping prompt as a list since inputs are usually a batch
            return_tensors="pt" # To return PyTorch tensors
        ) # To tokenize the prompt
        response = model.generate(
            **inputs, # **inputs unpacks the dictionary into keyword arguments
            streamer=streamer, # To stream the response
            max_length=max_length, # To limit the response length
            num_return_sequences=1, # To return only one response
            pad_token_id=tokenizer.eos_token_id, # To remove warning message in console
            # Below params inspired by this:
            # https://huggingface.co/docs/transformers/generation_strategies#multinomial-sampling
            # Check out this for more info:
            # https://huggingface.co/docs/transformers/generation_strategies#text-generation-strategies
            do_sample=True, # To use multinomial sampling
            num_beams=1 # To disable beam search
        ) # To generate the response
        prompt += tokenizer.decode(
            response[0], # response is a list since inputs are usually a batch
            skip_special_tokens=True # To remove special tokens like <eos>
        ) # To decode the response from tokens to text
        prompt = prompt[-max_memory:] # To remove the oldest tokens for the next loop