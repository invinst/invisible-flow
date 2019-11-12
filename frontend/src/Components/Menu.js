import React from 'react';
import Tab from './Tab'


function Menu(){
  return(
    <div className="Menu">
                    <Tab path="/" pagename="Home"/>
                    <Tab path="/scrapeStatus" pagename="Scraping Status"/>
    </div>
  );
}

export default Menu;