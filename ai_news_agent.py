
# import os
# from fetch_news import fetch_news
# from summarize_article import summarize_article
# from send_email import send_email
# from send_whatsapp import send_whatsapp
# from dotenv import load_dotenv
# load_dotenv(dotenv_path="env")
# # print("Loaded API Key:", os.environ.get("GEMINI_API_KEY"))


# def main():
#     articles = fetch_news()
#     summaries = []
#     highlights = []

#     for article in articles:
#         print("Before Summarize")
#         summary = summarize_article(article)
#         summaries.append(f"Title: {article['title']}\nLink: {article['link']}\nSummary: {summary}\n")
#         highlights.append(f"- {article['title']}")
#         print("After Summarize")
#         print(summaries)

#     email_body = "\n\n".join(summaries) + "\n\nKey Highlights:\n" + "\n".join(highlights)
#     whatsapp_body = "Daily AI News Summary:\n\n" + "\n\n".join(summaries) + "\n\nKey Highlights:\n" + "\n".join(highlights)

#     send_email("Daily AI News Summary", email_body)
#     send_whatsapp(whatsapp_body)

# if __name__ == "__main__":
#     main()



import os
from fetch_news import fetch_news
from summarize_article import summarize_article
from send_email import send_email
from send_telegram_message import send_telegram_message
from dotenv import load_dotenv
import requests
import json

load_dotenv(dotenv_path="env")

def select_top_articles(articles):
    api_key = os.environ.get("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}

    article_list = ""
    for i, article in enumerate(articles, 1):
        article_list += f"""{i}. Title: {article['title']}
Content: {article['content'][:500]}...

"""

    prompt = f"""You are a news editor. From the following list of articles, choose the 10 most important or impactful ones based on relevance, uniqueness, and global significance. Return only the list of selected article numbers.

Articles:
{article_list}
"""

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        reply = response.json()['candidates'][0]['content']['parts'][0]['text']
        print("LLM Selection Response:\n", reply)

        # Try parsing as JSON list
        try:
            selected_indices = json.loads(reply)
        except json.JSONDecodeError:
            # Fallback: parse numbered lines
            selected_indices = [int(s.strip().strip('.')) for s in reply.splitlines() if s.strip().split('.')[0].isdigit()]

        top_articles = [articles[i - 1] for i in selected_indices if 0 < i <= len(articles)]
        return top_articles

    except Exception as e:
        print(f"Failed to select top articles: {e}")
        return articles[:10]


def main():
    articles = fetch_news()
    print(f"Fetched {len(articles)} articles.")

    # Step 1: Let LLM pick top 10
    top_articles = select_top_articles(articles)
    print(f"Selected {len(top_articles)} top articles.")

    summaries = []
    highlights = []

    for article in top_articles:
        # print("Before Summarize")
        summary = summarize_article(article)
        summaries.append(f"""Title: {article['title']}
Link: {article['link']}
Summary: {summary}
""")
        # highlights.append(f"- {article['title']}")
        # print("After Summarize")

    email_body = "\n\n".join(summaries)
    whatsapp_body = "Daily AI News Summary:\n\n" + "\n\n".join(summaries) + "\n\nKey Highlights:\n" + "\n".join(highlights)

    send_email("Daily AI News Summary", email_body)
    send_telegram_message(whatsapp_body)

if __name__ == "__main__":
    main()