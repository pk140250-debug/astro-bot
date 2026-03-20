from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/astro', methods=['POST'])
def astro():
    data = request.json

    prompt = f"""
    Ты профессиональный астролог.

    Данные:
    {data}

    Сделай анализ, совет и прогноз.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({
        "answer": response.choices[0].message.content
    })

if name == '__main__':
    app.run(port=5000)
    
