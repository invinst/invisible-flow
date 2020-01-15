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
    console.log('child event on parent');
    console.log('before: ' + this.state.isScraping);
    this.setState({isScraping: !this.state.isScraping}, () => {
        console.log(this.state.isScraping);
    });
  }

  render() {
    if(this.state.isScraping){
        return(
            <div className='MainPage'>
              <h1>LOADING</h1>
            </div>
        );

    } else{
        return(
        <div className='MainPage'>
          <StartScrapeButton toggleLoading={this.toggleLoading}/>
        </div>
      );
    }
  }

}

export default MainPage;
