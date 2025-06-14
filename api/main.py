from flask import Flask, request, jsonify
from rembg import remove
ImageFile.LOAD_TRUNCATED_IMAGES = True
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/remove_background', methods=['POST'])
def remove_background_api():
    try:
        image_file = request.files['image']
        image = Image.open(image_file)
        output_image = remove(image)

        buffered = BytesIO()
        output_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        response = make_response(img_str)
        response.headers['Content-Type'] = 'image/png'
        return response
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
