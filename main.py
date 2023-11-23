import scraper, os,time
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.getenv('WEBHOOK_URL')


query = {
    "style_id": "4436_4679_893", 
    "size": "00 Short"
}

def main(query):
    data = scraper.main(query['style_id'])
    for size in data:
        if size['size'] == query['size']:
            if size['stock'] == 0:
                webhook = DiscordWebhook(url=WEBHOOK_URL, content=f"Now in stock (size: {query['size']})! [AE](https://www.ae.com/us/en/p/{query['style_id']})")
                response = webhook.execute()
            else:
                print("Not in stock")
                
    print("Sleeping for 12 hours then checking again...")
    time.sleep(43200)



while True:
    main(query)