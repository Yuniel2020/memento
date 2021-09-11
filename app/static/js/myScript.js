// SIDENAV MENU 
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
/* ===================================================================*/

// FULLWRITE MODUS 
// Open
var elFullWrite = document.getElementById('FullWrite-icon-buttom');
elFullWrite.addEventListener('click', function() {
  document.getElementById('app-layout-board').style.display = 'none';
  // Showing the editor-toolbar-button
  /* document.getElementById('editor-toolbar-button').style.display = 'block'; */
  // Showing the journal-toolbar-back
  document.getElementById('journal-toolbar-back').style.display = 'block';
}, false);
 
// Close
var elFullWriteClose = document.getElementById('journal-toolbar-back');
elFullWriteClose.addEventListener('click', function() {
  // Showing left-side board
  document.getElementById('app-layout-board').style.display = 'block';
  // Hiding journal-toolbar-back and editor-toolbar-button
  document.getElementById('journal-toolbar-back').style.display = 'none';
}, false);
/* ====================================================================== */

// GENERAL-ACTION MENU
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

// CREATING JOURNAL ITEMS (LIST-AREA)
// Code journal-editor
// Getting the 'add journal button' 
var elListIconBton = document.getElementById('list-icon-bton');
// Getting the <ul> element
var list = document.getElementById('list-of-journals');
// Adding a eventListener to the button element
elListIconBton.addEventListener('click', function() {
  // Showing the editor area
  document.getElementById('journal-editor-area').style.display = 'block';
  // Showing the editor-toolbar-button
  /*document.getElementById('editor-toolbar-button').style.display = 'block'*/
  // Hiding the editor-area-logo 
  document.getElementById('logo-holder').style.display = 'none'
  // Changing class attribute od div container 
  document.getElementById('list-is-empty').className = 'journal-list is-not-empty';
  // Hiding list-area-logo
  document.getElementById('journal-list-theme').style.display = 'none'

  // ADDING ITEMS TO THE START OF LIST
  // Create element: <li>
  var newItemFirstLi = document.createElement('li');
  // Adding class to li node
  newItemFirstLi.className = 'text-content';
  // Create element: <button>
  var newItemFirstBton = document.createElement('button');
  // Create element: <div>
  var selectableDiv = document.createElement('div');
  // Create text node 
  var newItemFirstText = document.createTextNode('New Entry...');
  // Adding text node to element
  newItemFirstLi.appendChild(newItemFirstText);
  // Adding <li> element to button node
  newItemFirstBton.appendChild(newItemFirstLi);
  // Adding <button> node to div element
  selectableDiv.appendChild(newItemFirstBton);
  // Adding class to div node
   selectableDiv.className = 'selectable-journal-item';
  // Adding element to the list
  list.insertBefore(selectableDiv, list.firstChild);
}, false);

// // CREATING JOURNAL ITEMS (EDITOR-TOOLBAR-AREA)
/* Code journal-editor */
// Getting the 'add journal button' 
var elEdtorBarBton = document.getElementById('editor-toolbar-button');
elEdtorBarBton.addEventListener('click', function() {
  
  // ADDING ITEMS TO THE START OF LIST
  // Create element: <li>
  var newItemFirstLi = document.createElement('li');
  // Adding class to li node
  newItemFirstLi.className = 'text-content';
  // Create element: <button>
  var newItemFirstBton = document.createElement('button');
  // Create element: <div>
  var selectableDiv = document.createElement('div');
  // Create text node 
  var newItemFirstText = document.createTextNode('New Entry...');
  // Adding text node to element
  newItemFirstLi.appendChild(newItemFirstText);
  // Adding <li> element to button node
  newItemFirstBton.appendChild(newItemFirstLi);
  // Adding <button> node to div element
  selectableDiv.appendChild(newItemFirstBton);
  // Adding class to div node
   selectableDiv.className = 'selectable-journal-item';
  // Adding element to the list
  list.insertBefore(selectableDiv, list.firstChild);
}, false);
/* ====================================================== */

// SELECTING JOURNAL-ITEMS
// Get <ul> element
var elList = document.getElementById('list-of-journals');
// Get HTMLCollections of <ul> element children 
var itemList = document.getElementsByTagName('ul')[0].children; 

elList.addEventListener('click', function(e) {                       // Add click event listener and pass event object (event delegation) 
  target = e.target;                                                 // Get event object target: where the click happened 
  for (var items = 0; items < itemList.length; items++) {            // Iterate over the list
    if (itemList[items] == target) {                                 // If target == element in list
      itemList[items].className = 'selected-item';                   // Set class to: 
    } else {                                                         // Otherwise
      itemList[items].className = 'selectable-journal-item';         // Set to: 
    }
  }
}, false);

elList.addEventListener('DOMNodeInserted', function() {               // Add event listener to DOM modification (insertion) 
  itemList[0].className = 'selected-item';                            // Set class attribute of new node
  if (itemList.length > 1) {                                          // If list is greater than 1, 
    for (var items = 1; items < itemList.length; items++) {           // Iterate over the list, and 
      itemList[items].className = 'selectable-journal-item';          // set class attribute of rest of list to selectable-journal-item
    }
  }
}, false);

/* ====================================================== */

// WRITING TITlE

// Getting title node
var elTitle = document.getElementById('journal-editor-header');
var selectedEntry = document.getElementsByClassName('selected-item')
var textEntered;

elTitle.addEventListener('keyup', function(e) {
  target = e.target;
  textEntered = target.innerText;
  // selectedEntry.contentEditable = 'true';
  selectedEntry[0].textContent = textEntered;
}, false);

/* ====================================================== */
 // GETTING DATA FROM THE EDITORS
 $('.save-button').on('click', function() {
  // Get content of the header (title) editor:
  var elTitle = tinymce.get('journal-editor-header').getContent();
  // Get content of the body editor:
  var elBody = tinymce.get('journal-editor-body').getContent();
  // 
  $.ajax({
    url:'save_journal',
    type: 'POST',
    data: {
     elTitle: elTitle,
     elBody: elBody
    }
  });
});
 


