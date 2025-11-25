from flask import Flask,jsonify,request,render_template
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


#initialize Flask app
app=Flask(__name__)
#set your OpenAI API key
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_img',methods=['POST'])
def generate_img():
    #get the prompt from the json payload of post request
    prompt=request.json.get('prompt')

    #call OpenAI's image generation API
    response=client.images.generate(
        model="gpt-image-1-mini", #specify the image generation model
        prompt=prompt, #specify the prompt for image generation
        n=1,           #number of images to generate 
        size="1024x1024"  #size of the generated image
    )

    image_url=response['data'][0]['url'] #extract the image URL from the response

    return jsonify({'image_url':image_url}) #return the image URL as a JSON response

if __name__=='__main__':
    app.run(debug=True) 