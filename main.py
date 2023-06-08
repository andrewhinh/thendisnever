# Import the necessary libraries
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer

# Setup the model
model_name = "Fredithefish/ScarletPajama-3B-HF" # Or whatever model you want
model = AutoModelForCausalLM.from_pretrained(model_name)
max_length = 500 # Or the model's max length or whatever you want
tokenizer = AutoTokenizer.from_pretrained(model_name)
streamer = TextStreamer(tokenizer)

# Setup the conversation loop
prompt = "THE END IS NEVER THE END IS NEVER THE END IS NEVER " # Or whatever you want
while True:
    inputs = tokenizer([prompt], return_tensors="pt")
    prompt += model.generate(**inputs, 
                             streamer=streamer, 
                             max_length=max_length,
                             num_return_sequences=1, # To return only one response
                             pad_token_id=tokenizer.eos_token_id, # To remove warning message in console
                             # Below params inspired by this:
                             # https://huggingface.co/docs/transformers/generation_strategies#multinomial-sampling
                             # Check out this for more info:
                             # https://huggingface.co/docs/transformers/generation_strategies#text-generation-strategies
                             do_sample=True, 
                             num_beams=1)
    if prompt[-1] == tokenizer.eos_token: # To remove the last token if it is an <eos> token
        prompt = prompt[:-1]
    if len(prompt) > 1000: # To remove the first `max_length`` tokens to prevent memory issues
        prompt = prompt[-max_length:]