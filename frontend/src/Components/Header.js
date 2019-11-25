import React from 'react';
import Menu from './Menu'

class Header extends React.Component{
    render(){
        return (
            <header className="Header-Box">
                <div className="Citizens-Police-Data"><h3 className="Site-Title">Citizens Police Data Project</h3></div>
                <Menu className="Menu"/>
            </header>
        )
    }

}

export default Header;