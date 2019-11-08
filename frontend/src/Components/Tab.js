import React from 'react';
import {Link} from 'react-router-dom';


function Tab(props){
  return(
    <Link to={props.path}>{props.pagename}    </Link>
  );
}

export default Tab;