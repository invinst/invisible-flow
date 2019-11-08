import React from 'react';
import Tab from './Tab'

class Header extends React.Component{
    render(){
        return (
            <header className="Header-Box">
                <h3 className="Citizens-Police-Data">Citizens Police Data Project</h3>
                <Tab path="/" pagename="Home"/>
                <Tab path="/scrapeStatus" pagename="Scraping Status"/>
            </header>
        )
    }

}

export default Header;