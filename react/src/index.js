import React from 'react';
import ReactDOM from 'react-dom';

// In the default template, body is empty. We must
// create a div to mount the app.
if(!document.getElementById('app')) {
  const divElem = document.createElement('div');
  divElem.id = 'app';
  document.body.appendChild(divElem);
}

const title = 'My Minimal React Webpack Babel Setup !!!';

ReactDOM.render(
  <div>{title}</div>,
  document.getElementById('app')
);

module.hot.accept();