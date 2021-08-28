
/* Code Sidenav Menu */
// Opening 
var elSettingNav = document.getElementById('SettingNav');
elSettingNav.addEventListener('click', function() {
  document.getElementById("app-menu-sidenav").style.display="block";
}, false);

// Closing
var elNavClose = document.getElementById('app-menu-sidenav');
elNavClose.addEventListener('mouseleave', function() {
  document.getElementById("app-menu-sidenav").style.display = "none";
}, false);

/* Code FullWrite Modus Open*/
var elFullWrite = document.getElementById('FullWrite-icon-buttom');
elFullWrite.addEventListener('click', function() {
  document.getElementById('app-layout-board').style.display = 'none';
  document.getElementById('editor-toolbar_column-left').style.display = 'block';
}, false);

/* Code FullWrite Modus Close*/
var elFullWriteClose = document.getElementById('journal-toolbar-back');
elFullWriteClose.addEventListener('click', function() {
  document.getElementById('app-layout-board').style.display = 'block';
  document.getElementById('editor-toolbar_column-left').style.display = 'none';
}, false);

/* Code general-action-menu*/
// Opening
var elLogout = document.getElementById('logout-button');
elLogout.addEventListener('click', function() {
  document.getElementById('general-action-menu').style.display = 'block';
}, false);

// Closing
var elNavClose = document.getElementById('general-action-menu');
elNavClose.addEventListener('mouseleave', function() {
  document.getElementById("general-action-menu").style.display = "none";
}, false);

/* Code journal-editor */
// Getting the 'add journal button'
var elListIconBton = document.getElementById('list-icon-bton');
// Getting the <ul> element
var list = document.getElementById('list-of-journals');
// Adding a eventListener to the button element
elListIconBton.addEventListener('click', function() {
  // Showing the editor area
  document.getElementById('journal-editor-area').style.display = 'block';
  // Hiding the editor-area-logo 
  document.getElementById('logo-holder').style.display = 'none'
  // Changing class attribute od div container 
  document.getElementById('list-is-empty').className = 'journal-list is-not-empty';
  // Hiding list-area-logo
  document.getElementById('journal-list-theme').style.display = 'none'
  // ADDING ITEMS TO THE START OF LIST
  // Create element
  var newItemFirst = document.createElement('li');
  // Create node
  var newTextFirst = document.createTextNode('Item 1');
  // Adding text node to element
  newItemFirst.appendChild(newTextFirst);
  // Adding element to the list
  list.insertBefore(newItemFirst, list.firstChild);
}, false);

/* journal-list-theme */
/* <button>
<div id="journal-list-item" style="border: solid 1px; width: 280px; display: flex; ">
   <span id="item-num">Item </span>
</div>
</button> 

<button aria-label="New Entry • Ctrl+Shift+I" accesskey="i" class="icon-button" type="button" id="editor-toolbar-button">
  <svg class="icon-new-journal" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24"><rect x="0" fill="none" width="24" height="24"></rect>
     <path d="M9.707 12.879L19.59 3 21 4.41l-9.879 9.883L9 15 9.707 12.879zM18 18H6V6h7V4H6.002C4.896 4 4 4.896 4 6.002v11.996C4 19.104 4.896 20 6.002 20h11.996C19.104 20 20 19.104 20 17.998V11h-2V18z"></path>
  </svg>
</button>*/



