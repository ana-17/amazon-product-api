const amazonScraper = require('../lib');

(async () => {
    try {
        // Parse command line arguments to get the target name
        const targetName = process.argv[2];
        const targetAsin = process.argv[3];
        const targetStars = process.argv[4];

        // Collect 50 reviews from a product ID B01GW3H3U8  with rating between 1-2 stars
        const reviews_rank = await amazonScraper.reviews({ asin: targetAsin, number: 50, rating: [targetStars, targetStars], name: targetName });
        //console.log(reviews_rank);

        // Find the review with the specific name value
        const targetReview = reviews_rank.result.find(review => review.name === targetName);

        // If the review is found, print it
        if (targetReview) {
            console.log('true');
            console.log('Found review:', targetReview);
            console.log("all reviews ", reviews_rank.result)
        } else {
            console.log('Review with the specified name not found.');
            console.log("all reviews ", reviews_rank)
        }
    } catch (error) {
        console.log(error);
    }
})();

// const amazonScraper = require('../lib');
// (async () => {
//     try {
//         // Collect 50 products from a keyword 'xbox one'
//         // Default country is US
        
//         // Collect 50 reviews from a product ID B01GW3H3U8  with rating between 1-2 stars
//         const reviews_rank = await amazonScraper.reviews({ asin: 'B01GW3H3U8', number: 50, rating: [1, 2], name: 'Marty' });
//         //console.log(reviews_rank);
//         const targetName = 'Marty';

//         // Find the review with the specific name value
//         const targetReview = reviews_rank.result.find(review => review.name === targetName);

//         // If the review is found, print it
//         if (targetReview) {
//             console.log('Found review:', targetReview);
//         } else {
//             console.log('Review with the specified name not found.');
//         }
//     } catch (error) {
//         console.log(error);
//     }
// })();