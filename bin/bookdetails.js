const amazonScraper = require('../lib');

(async () => {
    try {
        // Parse command line arguments to get the target name
        const targetAsin = process.argv[2];

        // Collect 50 reviews from a product ID B01GW3H3U8  with rating between 1-2 stars
        const product_details = await amazonScraper.asin({ asin: targetAsin });
        // console.log(product_details);
        console.log(JSON.stringify(product_details));

        // If the review is found, print it
    } catch (error) {
        // console.log(error);
        console.log(JSON.stringify({ error: error.message }));
    }
})();
