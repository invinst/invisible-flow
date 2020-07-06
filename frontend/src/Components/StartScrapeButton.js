// import React from 'react';
// import {useHistory} from 'react-router-dom';
//
// function StartScrapeButton(props) {
//     let history = useHistory();
//
//     async function goToScrapeStatus() {
//         await props.toggleLoading();
//         const request = new XMLHttpRequest();
//         request.open('GET', '/copa_scrape', true);
//         request.send();
//
//         request.onload = async () => {
//             await new Promise(resolve => setTimeout(resolve, 2000));
//             props.toggleLoading();
//             if (request.status === 200) {
//                 history.push('/scrapeStatus');
//             }
//         };
//     }
//
//     return (
//         <button className='Scrape-Button' onClick={goToScrapeStatus}>
//             Initiate scrape
//         </button>
//     );
// }
//
// export default StartScrapeButton;
