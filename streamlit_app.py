import streamlit as st
import requests
from bs4 import BeautifulSoup
import time

def scrape_product_data(webpage_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    
    while True:
        session = requests.Session()
        time.sleep(2)
        response = session.get(webpage_url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            scraped_data = {
                'title': None,
                'price': "Price not available",
                'rating': "Rating not available",
                'availability': "Availability not available",
                'reviews': ["No reviews available"]
            }

            # Get title
            try:
                title = soup.find("span", attrs={"id": 'productTitle'})
                title_value = title.text
                title = title_value.strip()
                if title != "Title not available":
                    scraped_data['title'] = title
            except Exception:
                pass

            # Get price
            try:
                price_whole = soup.find("span", class_='a-price-whole').text.strip()
                price_fractional = soup.find("span", class_='a-price-fraction').text.strip()
                price_currency = soup.find("span", class_='a-price-symbol').text.strip()
                scraped_data['price'] = f"{price_currency}{price_whole}.{price_fractional}"
            except Exception:
                pass

            # Get rating
            try:
                rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()
                scraped_data['rating'] = rating
            except Exception:
                try:
                    rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
                    scraped_data['rating'] = rating
                except:
                    pass

            # Get availability
            try:
                available = soup.find("div", attrs={'id': 'availability'})
                available = available.find("span").string.strip()
                scraped_data['availability'] = available
            except Exception:
                pass

            # Get reviews
            reviews = []
            review_elements = soup.find_all("div", class_="a-row a-spacing-small review-data")

            for i, element in enumerate(review_elements[:10]):
                review_text = element.find("span", class_="a-size-base review-text").text.strip()
                review_lines = review_text.split('\n')
                for line in review_lines:
                    if line.strip():
                        reviews.append(f"{i + 1}. {line.strip()}")
                        
            if scraped_data['title'] and scraped_data['price'] != "Price not available" and scraped_data['rating'] != "Rating not available" and scraped_data['availability'] != "Availability not available":
                return scraped_data
        else:
            continue

def main():
    st.title("Scrapify Assistant")
    st.write("Enter the URL of the product page:")
    
    webpage_url = st.text_input("URL")
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    
    user_input = st.text_area("You:", value=st.session_state.user_input)
    
    if st.button("Send"):
        st.session_state.user_input = user_input.lower()
        st.session_state.chat_history.append(f"You: {st.session_state.user_input}")
        
        try:
            scraped_data = scrape_product_data(webpage_url)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return
        
        st.success("Data successfully scraped!")
        st.header("Scraped Product Data")
        st.write(f"Title: {scraped_data['title']}")
        
        for key, value in scraped_data.items():
            response = f"The {key} of the product is: {value}"
            st.session_state.chat_history.append(response)
            
        st.session_state.user_input=""
        
    st.text_area("Chat History", value="\n".join(st.session_state.chat_history), height=200)

if __name__ == "__main__":
    main()
