import React from 'react';
import {NavLink} from 'react-router-dom';

function Tab(props){
  return (
    <NavLink to={props.path} exact className='Nav-Tab' activeClassName='Active-Tab'>
      {props.pagename}
    </NavLink>
  );
}

export default Tab;
