import React from 'react';
import {Link} from 'react-router-dom';
import Menu from './Menu';

class Header extends React.Component{
    render(){
        return (
            <header className="Header-Box">
                <div className="Citizens-Police-Data"><h3 className="Site-Title"><Link to="/">Citizens Police Data Project</Link></h3></div>
                <Menu className="Menu"/>
            </header>
        )
    }

}

export default Header;