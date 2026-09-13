from SoupGetData import ZillowScraper
from GoogleForm import GoogleForm
from dotenv import load_dotenv
import os
load_dotenv()
scraper = ZillowScraper(os.environ["ZILLOW_URL"])
data = scraper.get_properties()
form = GoogleForm(os.environ["FORM_URL"])
for property in data:

    form.open()

    for property in data.values():

        form.fill_form(
            address=property["address"],
            price=property["price"],
            url=property["url"]
        )

        form.submit()
        form.next_form()

    form.close()
