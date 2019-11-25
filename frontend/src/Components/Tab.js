import React from 'react';
import {Link, BrowserRouter} from 'react-router-dom';


function Tab(props){
  return(
    <BrowserRouter>
     <Link className="Active-Tab" to={props.path}>{props.pagename} </Link>
    </BrowserRouter>
  );
}

export default Tab;