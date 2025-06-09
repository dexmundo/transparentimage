# main.py
from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route("/remove_background", methods=["POST"])
def remove_background_route():
    if "image" not in request.files:
        return "No image uploaded", 400

    image_file = request.files["image"]
    try:
        input_image = Image.open(image_file)
        output_image = remove(input_image)
        
        # Save the image to a BytesIO object
        img_byte_arr = io.BytesIO()
        output_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        return send_file(img_byte_arr, mimetype='image/png')

    except Exception as e:
        return f"Error processing image: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
