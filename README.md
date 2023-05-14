<!DOCTYPE html>
<html lang="en">

<body>
  
<h1>Amazon Scraper</h1>
  
<p>This is a web scraping project using Scrapy to scrape product data from Amazon.com.</p>

<h2>Features</h2>
  
<ul>
        <li>Scrapes product data from Amazon.com</li>
        <li>Extracts product names, prices, and ASINs</li>
        <li>Supports pagination to scrape multiple pages</li>
        <li>Automatically follows links to individual product pages</li>
        <li>Uses Scrapy's built-in features for web scraping</li>
</ul>

<h2>Requirements</h2>
  
<ul>
        <li>Python 3.6+</li>
        <li>Scrapy 2.5.1</li>
</ul>

<h2>Installation</h2>
  
<p>Clone the repository and install the required dependencies using pip:</p>
  
<code>git clone https://github.com/akinyolci/scraping_amazon_products.git 
cd amazon-scraper 
pip install -r requirements.txt</code>

<h2>Usage</h2>
  
<p>Run the scraper with the following command:</p>
<code>scrapy crawl bot</code>

<h2>Customization</h2>
<p>You can customize the scraper by modifying the <code>BotSpider</code> class in the <code>bot.py</code> file. For example, you can change the starting URL, adjust pagination settings, and modify the data extraction logic.</p>

<h2>Output</h2>
<p>The scraper outputs the scraped data in JSON format. The extracted data includes product names, prices, and ASINs, which are stored in the <code>AmazonItem</code> item class. You can customize the output format by modifying the <code>items.py</code> file.</p>

<h2>Contributing</h2>
<p>If you'd like to contribute to this project, please open an issue or submit a pull request on GitHub: <a href="https://github.com/yourusername/amazon-scraper">https://github.com/yourusername/amazon-scraper</a></p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more information.</p>
</body>
</html>
