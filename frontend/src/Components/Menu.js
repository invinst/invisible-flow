import React from 'react';
import Tab from './Tab';

function Menu(){
  return(
    <div className='Menu'>
      <Tab path='/' pagename='COPA Scrape'/>
      <Tab path='/FOIA' pagename='FOIA Upload'/>
    </div>
  );
}

export default Menu;
