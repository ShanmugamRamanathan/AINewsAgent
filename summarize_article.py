import os
import requests

def summarize_article(article):
    api_key = os.environ.get('GEMINI_API_KEY')
    # print("API Key inside summarize_article:", api_key)

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": f"""Summarize the following article and provide key highlights:

{article['content']}"""}
                ]
            }
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        # print("Response - ",response)
        response.raise_for_status()
        summary = response.json()['candidates'][0]['content']['parts'][0]['text']
        # print(summary)
        return summary
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except (KeyError, TypeError) as e:
        print(f"Error parsing response: {e}")
        return None