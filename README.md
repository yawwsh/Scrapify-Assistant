# Scrapify Assistant

Scrapify Assistant is a web scraping chatbot that simplifies the process of retrieving data from web pages. It allows users to input the URL of a product page, and it scrapes and provides information about the product, such as its title, price, rating, availability, and a selection of reviews. Users can interact with the chatbot, making it a versatile tool for data extraction.

## Features
- Scrapes data from Amazon product pages.
- Provides information on product title, price, rating, availability, and reviews.
- Supports user interaction, allowing users to ask questions about the product data.
- Displays a chat history to keep track of the conversation.

## Getting Started
Click the link below

(OR)

To run Scrapify Assistant on local machine, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip`:

   ```bash
   pip install streamlit requests beautifulsoup4
1 Open a terminal and navigate to the project directory.

2 Run the chatbot using Streamlit:
```streamlit run chatbot.py```

##Usage
1 Enter the URL of an Amazon product page.
2 Click the "Send" button to scrape product data.
3 Interact with the chatbot by asking questions or making requests.
4 The chat history will be displayed below the input area.

##Example Conversations
User: "What is the price of the product?"

Chatbot: "The price of the product is $X.XX."
User: "Tell me the availability."

Chatbot: "The product is available."
User: "Show me the title."

Chatbot: "The title of the product is 'Product Title'."

##Note
The chatbot is configured to work with Amazon product pages, and the HTML structure of other websites may require adjustments.

##Contributions
Contributions to Scrapify Assistant are welcome. If you encounter any issues or have ideas for improvements, please create an issue or submit a pull request.
