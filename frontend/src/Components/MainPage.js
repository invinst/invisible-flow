import React from 'react';
import StartScrapeButton from './StartScrapeButton';

class MainPage extends React.Component{
  constructor(props){
    super(props);
    this.state = {
        isScraping: false
    };
    this.toggleLoading = this.toggleLoading.bind(this);
  }

  toggleLoading() {
    this.setState({isScraping: !this.state.isScraping});
  }

  render() {
    if(this.state.isScraping){
        return(
            <div className='MainPageLoading'>
              <h1>COPA Scrape</h1>
              <div class="spinner-box">
                <div class="spinner"></div>
                <p>Scraping...</p>
              </div>
            </div>
        );

    } else{
        return(
        <div className='MainPage'>
          <h1>COPA Scrape</h1>
          <StartScrapeButton toggleLoading={this.toggleLoading}/>
        </div>
      );
    }
  }

}

export default MainPage;
