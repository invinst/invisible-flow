import React from 'react';
import {Link} from 'react-router-dom';


function Tab(props){
  return(
     <Link className="Active-Tab" to={props.path}>{props.pagename} </Link>
  );
}

export default Tab;